from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery
from support import get_env_data
from database import get_user_by_uid, async_session, ban_user, unban_user, get_all_banned, get_adm_ids, get_user_by_tg_id
from keyboards import admin_panel_main, get_user_actions_kb, return_to_main
import hashlib
import os

router = Router()


class GetUserByUid(StatesGroup):
    uid = State()


class GetUserByTgId(StatesGroup):
    tg_id = State()


class AdminAuth(StatesGroup):
    password = State()


@router.callback_query(F.data == "admin_panel")
async def admin_get_pass(callback: CallbackQuery, state: FSMContext):
    await state.set_state(AdminAuth.password)
    await callback.message.answer(text="Введите пароль")
    # hash_ = hashlib.new('sha256')
    # hash_.update(credentials.password.encode())
    # hashed_password = hash_.hexdigest()


@router.message(AdminAuth.password)
async def admin_auth(message: Message, state: FSMContext):
    await message.delete()
    await state.update_data(password=message.text)
    if int(os.getenv("ADM_PASS")) == int(message.text):
        await state.clear()
        return await message.answer(text='+', reply_markup=admin_panel_main)
    else:
        await state.clear()


@router.message(F.text == "get user by uid")
async def adm_get_uid(message: Message, state: FSMContext):
    await message.delete()
    await state.set_state(GetUserByUid.uid)
    await message.answer('Введите id пользователя')


@router.message(GetUserByUid.uid)
async def adm_get_user_by_uid(message: Message, state: FSMContext):
    await state.update_data(uid=message.text)
    adm_ids = await get_adm_ids(async_session=async_session)
    await state.clear()
    if message.from_user.id in adm_ids:
        user = await get_user_by_uid(async_session=async_session, uid=int(message.text))
        if user is None:
            return await message.answer(text=f'Пользователь с id: {message.text} не найден')
        reply_text = f'id: {user.id}\n username: {user.username}\n tg_id: {user.tg_id}\n is_active: {user.is_active}'
        return await message.answer(
            text=reply_text,
            reply_markup=await get_user_actions_kb(is_active=user.is_active, tg_id=user.tg_id)
        )


@router.message(F.text == "get user by tg uid")
async def adm_get_uid(message: Message, state: FSMContext):
    await message.delete()
    await state.set_state(GetUserByTgId.tg_id)
    await message.answer('Введите tg id пользователя')


@router.message(GetUserByUid.uid)
async def adm_get_user_by_uid(message: Message, state: FSMContext):
    await state.update_data(uid=message.text)
    adm_ids = await get_adm_ids(async_session=async_session)
    await state.clear()
    if message.from_user.id not in adm_ids:
        await state.clear()
        return 0
    user = await get_user_by_tg_id(
        async_session=async_session, tg_id=int(message.text)
    )
    if user is None:
        return await message.answer(text=f'Пользователь с tg_id: {message.text} не найден')
    reply_text = f'id: {user.id}\n username: {user.username}\n tg_id: {user.tg_id}\n is_active: {user.is_active}'
    return await message.answer(
        text=reply_text,
        reply_markup=await get_user_actions_kb(is_active=user.is_active, tg_id=user.tg_id)
    )


@router.callback_query(F.data.startswith('ban_'))
async def adm_ban_user(callback: CallbackQuery):
    adm_ids = await get_adm_ids(async_session=async_session)
    tg_id = callback.data.split('_')[1]
    if callback.from_user.id in adm_ids:
        response = await ban_user(async_session=async_session, tg_id=int(tg_id))
        return callback.message.answer(text=response, reply_markup=return_to_main)


@router.callback_query(F.data.startswith('unban_'))
async def adm_unban_user(callback: CallbackQuery):
    adm_ids = await get_adm_ids(async_session=async_session)
    tg_id = callback.data.split('_')[1]
    if callback.from_user.id in adm_ids:
        response = await unban_user(async_session=async_session, tg_id=int(tg_id))
        return callback.message.answer(text=response, reply_markup=return_to_main)


@router.message(F.text == "get all banned users")
async def adm_get_all_banned(message: Message):
    adm_ids = await get_adm_ids(async_session=async_session)
    if message.from_user.id in adm_ids:
        users = await get_all_banned(async_session=async_session)
        mes = ''
        if users is None:
            return await message.answer(text='Список пуст')
        for user in users:
            mes += f'id: {user.id}; tg_id: {user.tg_id}; username: {user.username}\n'
        return await message.answer(text=mes, reply_markup=return_to_main)

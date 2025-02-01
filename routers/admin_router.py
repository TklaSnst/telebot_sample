from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery
from support import get_env_data
from database import get_user_by_uid, async_session, ban_user, unban_user
from keyboards import admin_panel_main, get_user_actions_kb, return_to_main
import hashlib
import os

router = Router()


async def get_adm_ids():
    env_data = await get_env_data()
    return map(int, env_data["ADM_IDS"].split(','))


class GetUserByUid(StatesGroup):
    uid = State()


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


@router.message(F.text == "get user by uid")
async def adm_get_uid(message: Message, state: FSMContext):
    await message.delete()
    await state.set_state(GetUserByUid.uid)
    await message.answer('Введите id пользователя')


@router.message(GetUserByUid.uid)
async def adm_get_user_by_uid(message: Message, state: FSMContext):
    await state.update_data(uid=message.text)
    adm_ids = await get_adm_ids()
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


@router.callback_query(F.data.startswith('ban_'))
async def adm_ban_user(callback: CallbackQuery):
    adm_ids = await get_adm_ids()
    tg_id = callback.data.split('_')[1]
    if callback.from_user.id in adm_ids:
        response = await ban_user(async_session=async_session, tg_id=int(tg_id))
        return callback.message.answer(text=response, reply_markup=return_to_main)


@router.callback_query(F.data.startswith('unban_'))
async def adm_unban_user(callback: CallbackQuery):
    adm_ids = await get_adm_ids()
    tg_id = callback.data.split('_')[1]
    if callback.from_user.id in adm_ids:
        response = await unban_user(async_session=async_session, tg_id=int(tg_id))
        return callback.message.answer(text=response, reply_markup=return_to_main)

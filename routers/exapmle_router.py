from aiogram import Router, F
from database import create_user, async_session
from aiogram.filters.command import Command
from aiogram.types import Message, CallbackQuery
from database import UserAddSchema, get_user_by_tg_id
from keyboards import start_kb, start_kb_admin
from support import get_env_data

router = Router()


@router.message(Command("start"))
@router.message(F.text == "Вернуться на главную")
async def start(message: Message):
    await message.delete()
    try:
        user = UserAddSchema(tg_id=message.from_user.id, username=message.from_user.username)
        await create_user(async_session=async_session, user_add=user)
    except Exception as ex:
        raise ex
    env_data = await get_env_data()
    adm_ids = map(int, env_data["ADM_IDS"].split(','))
    if message.from_user.id in adm_ids:
        return await message.answer(text=f'Hello, {message.from_user.username}!', reply_markup=start_kb_admin)
    return await message.answer(text=f'Hello, {message.from_user.username}!', reply_markup=start_kb)


# @router.message()
# async def echo(message: Message):
#     await message.answer(text=f'{message.text}🤓🤓🤓')
#     # await message.answer(text=f'{message}🤓🤓🤓')
#

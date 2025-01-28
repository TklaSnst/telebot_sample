from aiogram import Router
from database import create_user, async_session
from aiogram.filters.command import Command
from aiogram.types import Message, CallbackQuery
from database import UserAddSchema
from keyboards import start_kb

router = Router()


@router.message(Command("start"))
async def start(message: Message):
    await message.answer(text=f'Hello, {message.from_user.username}!', reply_markup=start_kb)
    try:
        user = UserAddSchema(tg_id=message.from_user.id, username=message.from_user.username)
        await create_user(async_session=async_session, user_add=user)
    except Exception as ex:
        raise ex


@router.message()
async def echo_def(message: Message):
    await message.answer(text=f'{message.text}🤓🤓🤓')

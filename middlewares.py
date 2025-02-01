from aiogram import BaseMiddleware
from typing import Callable, Dict, Any, Awaitable
from aiogram.types import Message
from database import get_user_by_tg_id, async_session


class AuthMiddleware(BaseMiddleware):
    async def __call__(self,
                       handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
                       event: Message,
                       data: Dict[str, Any]) -> Any:
        tg_id = event.from_user.id
        user = await get_user_by_tg_id(async_session=async_session, tg_id=tg_id)
        if user.is_active:
            result = await handler(event, data)
            return result

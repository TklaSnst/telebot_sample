from sqlalchemy.ext.asyncio import AsyncSession
from .models import User
from .schemas import UserAddSchema
from sqlalchemy import select


async def create_user(async_session: AsyncSession, user_add: UserAddSchema) -> User:
    async with async_session() as session:
        stmt = select(User).where(User.tg_id == user_add.tg_id)
        result = await session.execute(stmt)
        user = result.scalar()
        if user is None:
            user_create = User(**user_add.model_dump())
            session.add(user_create)
            await session.commit()
            return user_create
            # await session.refresh(user_create)
        return user


async def get_user_by_uid(async_session: AsyncSession, uid: int):
    async with async_session() as session:
        stmt = select(User).where(User.id == uid)
        result = await session.execute(stmt)
        user = result.scalar()
        return user


async def get_user_by_tg_id(async_session: AsyncSession, tg_id: int):
    async with async_session() as session:
        stmt = select(User).where(User.tg_id == tg_id)
        result = await session.execute(stmt)
        user = result.scalar()
        return user


async def ban_user(async_session: AsyncSession, tg_id: int):
    async with async_session() as session:
        try:
            stmt = select(User).where(User.tg_id == tg_id)
            result = await session.execute(stmt)
            user = result.scalar()
            user.is_active = False
            await session.commit()
            return "usr banned"
        except Exception as ex:
            return "smthng wrong"


async def unban_user(async_session: AsyncSession, tg_id: int):
    async with async_session() as session:
        try:
            stmt = select(User).where(User.tg_id == tg_id)
            result = await session.execute(stmt)
            user = result.scalar()
            user.is_active = True
            await session.commit()
            return "usr unbanned"
        except Exception as ex:
            return "smthng wrong"


async def get_all_banned(async_session: AsyncSession) -> list[User] | None:
    async with async_session() as session:
        try:
            stmt = select(User).where(User.is_active == False)
            result = await session.execute(stmt)
            users = result.scalars()
            return users
        except Exception as ex:
            return None

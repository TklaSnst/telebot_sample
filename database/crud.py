from sqlalchemy.ext.asyncio import AsyncSession
from .models import User
from .schemas import UserAddSchema
from sqlalchemy import select


async def create_user(async_session: AsyncSession, user_add: UserAddSchema):
    async with async_session() as session:
        stmt = select(User).where(User.tg_id == user_add.tg_id)
        result = await session.execute(stmt)
        user = result.scalar()
        if user is None:
            user_create = User(**user_add.model_dump())
            session.add(user_create)
            await session.commit()
            # await session.refresh(user_create)

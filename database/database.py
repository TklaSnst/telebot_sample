from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from .models import Base
from dotenv import load_dotenv
from redis.asyncio import Redis
import os

load_dotenv()

engine = create_async_engine(os.getenv('DB_URL'))
async_session = async_sessionmaker(engine)

redis_client = Redis(host='172.17.0.1', port=6379, db=0, decode_responses=True)


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def drop_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

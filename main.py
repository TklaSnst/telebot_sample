from aiogram.enums import ParseMode
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from routers import router as example_router
from database import create_tables
import asyncio
import os

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
dp = Dispatcher()
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp.include_router(example_router)


async def main():
    await create_tables()
    await dp.start_polling(bot)


if __name__ == "__main__":
    print('start')
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('exit')

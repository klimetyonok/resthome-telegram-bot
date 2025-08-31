import asyncio
import logging

import os
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

load_dotenv()

from app.bot import bot, dp
from app.handlers import routers 
from app.database.base import engine, Base

async def main():
    # Подключаем все роутеры
    for router in routers:
        dp.include_router(router)
    # Создаем таблицы в БД
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    # Запускаем поллинг бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')











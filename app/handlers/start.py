from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from app.keyboards.main_kb import main_menu_kb

router = Router()

# Обработчик команды /start
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Добро пожаловать в эко-отель!\n\n"
                         "Я ваш виртуальный помощник. Чем могу помочь?",
                         reply_markup=main_menu_kb)

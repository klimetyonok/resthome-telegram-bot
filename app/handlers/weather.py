from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from app.services.weather import get_weather

router = Router()

# Команда /weather
@router.message(Command("weather"))
async def cmd_weather(message: Message):
    await message.answer("🌤️ Погода в районе отеля...")
    weather_info = await get_weather()
    await message.answer(weather_info)

# Кнопка "Погода"
@router.message(F.text == "🌤️ Погода")
async def weather_info(message: Message):
    await message.answer("Сейчас +20°C, солнечно ☀️")
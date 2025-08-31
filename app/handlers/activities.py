import random
from aiogram import Router, F
from aiogram.types import Message
from app.keyboards.main_kb import main_menu_kb

router = Router()

ACTIVITIES = [
    "🧩 Сегодня отличный день для настольных игр",
    "🔥 Вечером топим баню. Записывайтесь у администратора",
    "📚 Предлагаем почитать книгу из нашей библиотеки в уютном шезлонге",
    "🚲 Самое время для велосипедных прогулок",
    "🎣 Сегодня отличный день для рыбалки",
]

@router.message(F.text == "🎲 Активность дня")
async def random_activity(message: Message):
    activity = random.choice(ACTIVITIES)
    await message.answer(activity)
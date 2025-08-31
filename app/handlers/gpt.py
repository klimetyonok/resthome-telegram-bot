from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from app.services.yandex_gpt import ask_gpt

router = Router()

# Обработчик команды /gpt
@router.message(Command("gpt", "ask", "вопрос"))
async def cmd_gpt(message: Message):
    await message.answer(
        "🤖 Задайте ваш вопрос о нашем отеле:\n\n"
        "• Бронирование и цены\n"
        "• Услуги и удобства\n"
        "• Развлечения и активность\n"
        "• Любые другие вопросы об отеле"
    )

# Обработчик текстовых сообщений (кроме команд)
@router.message(F.text & ~F.command)
async def handle_gpt_query(message: Message):
    await message.bot.send_chat_action(chat_id=message.chat.id, action="typing")

    # Получаем ответ от GPT
    gpt_response = await ask_gpt(message.text)

    # Отправляем ответ пользователю
    await message.answer(gpt_response)

# Обработчик для кнопки "Задать вопрос"
@router.message(F.text == "❓ Задать вопрос")
async def handle_question_button(message: Message):
    await message.answer(
        "Задайте ваш вопрос о нашем отеле. Например:\n\n"
        "• Какие номера есть в отеле?\n"
        "• Сколько стоит аренда бани?\n"
        "• Есть ли у вас скидки?\n"
        "• Как добраться до отеля?"
    )  
        


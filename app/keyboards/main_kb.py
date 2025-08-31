from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="🏨 Забронировать номер")],
                                             [KeyboardButton(text="ℹ️ Информация об отеле"),
                                              KeyboardButton(text="🌤️ Погода")],
                                              [KeyboardButton(text="🎲 Активность дня"),
                                               KeyboardButton(text="📞 Контакты")],
                                               [KeyboardButton(text="❓ Задать вопрос")]],
                                               resize_keyboard=True,
                                               input_field_placeholder="Выберите пункт меню...")
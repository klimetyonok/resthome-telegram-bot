# Rest Home Telegram Bot 🏔️

Умный чат-бот для телеграм, разработанный для дома отдыха. Бот выполняет функции виртуального администратора, отвечая на вопросы и обрабатывая бронирования.

## ✨ Функционал

- **🤖 Умные ответы:** Интеграция с Yandex GPT для ответов на вопросы гостей.
- **🗓️ Система бронирования:** Бронирование через FSM.
- **🌤️ Информация по погоде:** Информация о погоде на даты бронирования на основе данных OpenWeatherMap.
- **🎲 Активность дня:** Рандомная рекомендация активности для развлечения гостей.

## 🛠️ Технологии

- Python 3.12.10
- Aiogram 3.22.0 
- SQLAlchemy 2.0.43 (ORM)
- AIOHTTP 3.12.15
- Yandex Cloud API (Yandex GPT)
- OpenWeatherMap API

## 🚀 Установка и запуск

1. Клонируйте репозиторий:

```bash
git clone https://github.com/klimetyonok/resthome-telegram-bot.git
cd resthome-telegram-bot
```

2. Создайте виртуальное окружение и установите зависимости:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
.\venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

3. Настройте переменные окружения. Создайте файл .env:

```bash
BOT_TOKEN=your_bot_token
WEATHER_API_KEY=your_weather_key
YANDEX_CLOUD_API_KEY=your_yandex_key
YANDEX_GPT_FOLDER_ID=your_folder_id
ADMIN_IDS=123456789
DATABASE_URL=sqlite+aiosqlite:///./database.db
```

4. Запустите бота:

```bash
python -m app.main
```
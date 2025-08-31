import aiohttp
import os

# Объявление асинхронной функции
async def ask_gpt(user_message: str, context: list = []) -> str:
    prompt = {
        "modelUri": f"gpt://{os.getenv('YANDEX_GPT_FOLDER_ID')}/yandexgpt-lite",
        "completionOptions": {
            "stream": False,
            "temperature": 0.7,
            "maxTokens": 1000
        },
        "messages": [
            {
                "role": "system",
                "text": ("Ты - помощник эко-отеля. Отвечай вежливо. "
                         "Цены: стандарт - 300BYN/сутки. "
                         "У нас есть баня, прокат велосипедов и лодок. "
                         "Услуги: баня (100 BYN/2 часа), прокат велосипедов (20 BYN/час), лодок (50 BYN/час). "
                         "Отвечай ТОЛЬКО на вопросы, связанные с отдыхом, отелем и туризмом. "
                         "Если вопрос не по теме, вежливо откажись отвечать.")
            },
            *context,
            {
                "role": "user",
                "text": user_message}
        ]
    }
    # Отправка HTTP-запроса к API
    async with aiohttp.ClientSession() as session:
        async with session.post(
            "https://llm.api.cloud.yandex.net/foundationModels/v1/completion",
            headers={"Authorization": f"Api-Key {os.getenv('YANDEX_CLOUD_API_KEY')}"},
            json=prompt
        ) as response:
            data = await response.json()
            return data['result']['alternatives'][0]['message']['text']
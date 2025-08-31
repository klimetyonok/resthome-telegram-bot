import aiohttp
import os
from typing import Optional

async def get_weather(city: str = "Минск") -> Optional[str]:
    api_key = os. getenv('WEATHER_API_KEY')
    url = f"ttp://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()

            temp = data['main']['temp']
            feels_like = data['main']['feels_like']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            city_name = data['name']
                
            return (
                f"🌤️ Погода в {city_name}:\n\n"
                f"• Температура: {temp}°C (ощущается как {feels_like}°C)\n"
                f"• Влажность: {humidity}%\n"
                f"• Ветер: {wind_speed} м/с"
            )



# Импортируем все роутеры
from .activities import router as activities_router
from .booking import router as booking_router
from .gpt import router as gpt_router
from .start import router as start_router
from .weather import router as weather_router


# Список всех роутеров
routers = [
    activities_router,
    booking_router,
    gpt_router,
    start_router,
    weather_router
]
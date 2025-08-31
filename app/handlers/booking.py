from aiogram import Router, types, F
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from app.database.base import async_session, create_booking, get_or_create_user
from datetime import datetime

router = Router()

class BookingState(StatesGroup):
    choosing_dates = State()
    entering_name = State()
    entering_phone = State()
    finished = State()

@router.message(F.text == "🏨 Забронировать номер")
async def start_booking(message: types.Message, state: FSMContext):
    await state.set_state(BookingState.choosing_dates)
    await message.answer("Введите даты заезда и выезда в формате ДД.ММ.ГГГГ (через пробел):")

@router.message(BookingState.choosing_dates)
async def process_dates(message: types.Message, state: FSMContext):
    try:
        date_in_str, date_out_str  = message.text.split()
        date_in = datetime.strptime(date_in_str, "%d.%m.%Y").date()
        date_out = datetime.strptime(date_out_str , "%d.%m.%Y").date()
        await state.update_data(date_in=date_in, date_out=date_out)
        await state.set_state(BookingState.entering_name)
        await message.answer("Отлично! Теперь введите ваше ФИО:")
    except:
        await message.answer("Неверный формат. Пример: 25.12.2024 30.12.2024")

@router.message(BookingState.entering_name)
async def process_name(message: types.Message, state: FSMContext):
    name = message.text.strip()
    await state.update_data(name=name)
    await state.set_state(BookingState.entering_phone)
    await message.answer("Теперь введите ваш номер телефона:")

@router.message(BookingState.entering_phone)
async def process_phone(message: types.Message, state: FSMContext):
    phone = message.text.strip()
    await state.update_data(phone=phone)
    await state.set_state(BookingState.finished)
    #await message.answer("Заявка создана! Менеджер свяжется с вами.")
    
    data = await state.get_data()

    async with async_session() as session:
            user = await get_or_create_user(
                session=session,
                tg_id=message.from_user.id,
                fullname=message.from_user.full_name,
                username=message.from_user.username
            )

            booking = await create_booking(
                session=session,
                user=user,
                check_in=data['date_in'],
                check_out=data['date_out'],
                guest_name=data['name'],
                guest_phone=data['phone']
            )
            
            check_in_str = data['date_in'].strftime("%d.%m.%Y")
            check_out_str = data['date_out'].strftime("%d.%m.%Y")
            
            await message.answer(
                f"✅ <b>Заявка на бронирование создана!</b>\n\n"
                f"📅 <b>Даты:</b> {check_in_str} - {check_out_str}\n"
                f"👤 <b>Гость:</b> {data['name']}\n"
                f"📞 <b>Телефон:</b> {data['phone']}\n"
                f"🔢 <b>Номер заявки:</b> #{booking.id}\n\n"
                f"Менеджер свяжется с вами в ближайшее время для подтверждения.",
                parse_mode="HTML"
            )
            await state.clear()
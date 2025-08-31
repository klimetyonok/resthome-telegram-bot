from datetime import date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, Text, Date, Integer, select
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int] = mapped_column(unique=True)
    fullname: Mapped[str] = mapped_column(String(100))
    username: Mapped[str | None] = mapped_column(String(50))
    bookings: Mapped[list["Booking"]] = relationship(back_populates="user")

class Booking(Base):
    __tablename__ = "bookings"
    id: Mapped[int] = mapped_column(primary_key=True)
    check_in: Mapped[date] = mapped_column(Date)
    check_out: Mapped[date] = mapped_column(Date)
    status: Mapped[str] = mapped_column(String(20), default="pending") # pending, confirmed, cancelled
    guest_name: Mapped[str] = mapped_column(String(100))
    guest_phone: Mapped[str] = mapped_column(String(20))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="bookings")

engine = create_async_engine("sqlite+aiosqlite://", echo=True)
async_session = async_sessionmaker(engine, expire_on_commit=False)

# Функция для получения пользователя по tg_id
async def get_or_create_user(
        session: AsyncSession,
        tg_id: int,
        fullname: str,
        username: str | None = None
) -> User:
    result = await session.execute(select(User).where(User.tg_id == tg_id))
    user = result.scalar_one_or_none()
    
    if user is None:
        user = User(tg_id=tg_id, fullname=fullname, username=username)
        session.add(user)
        await session.commit()
        await session.refresh(user)
    return user

# Функция для создания бронирования
async def create_booking(
    session: AsyncSession, 
    user: User,
    check_in: date, 
    check_out: date, 
    guest_name: str, 
    guest_phone: str
) -> Booking:
    booking = Booking(
        user_id=user.id,
        check_in=check_in,
        check_out=check_out,
        guest_name=guest_name,
        guest_phone=guest_phone
    )
    session.add(booking)
    await session.commit()
    await session.refresh(booking)
    return booking
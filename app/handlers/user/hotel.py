from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.config.settings import GROUP_ID
from app.repositories.user_repository import UserRepository

from app.states.hotel import HotelState
from app.keyboards.main_menu import main_menu

router = Router()


@router.message(F.text == "🏨 Hotel / Hostel")
async def hotel_start(
    message: Message,
    state: FSMContext
):
    await state.set_state(
        HotelState.waiting_city
    )

    await message.answer(
        "📍 Qaysi shaharda mehmonxona kerak?\n\n"
        "Masalan: Makka, Madina, Jidda"
    )


@router.message(HotelState.waiting_city)
async def city_handler(
    message: Message,
    state: FSMContext
):
    await state.update_data(
        city=message.text
    )

    await state.set_state(
        HotelState.waiting_checkin
    )

    await message.answer(
        "📅 Kirish sanasini kiriting\n\n"
        "Masalan: 10.08.2026"
    )


@router.message(HotelState.waiting_checkin)
async def checkin_handler(
    message: Message,
    state: FSMContext
):
    await state.update_data(
        checkin=message.text
    )

    await state.set_state(
        HotelState.waiting_checkout
    )

    await message.answer(
        "📅 Chiqish sanasini kiriting\n\n"
        "Masalan: 15.08.2026"
    )


@router.message(HotelState.waiting_checkout)
async def checkout_handler(
    message: Message,
    state: FSMContext
):
    await state.update_data(
        checkout=message.text
    )

    await state.set_state(
        HotelState.waiting_guests
    )

    await message.answer(
        "👥 Necha kishi joylashadi?"
    )


@router.message(HotelState.waiting_guests)
async def guests_handler(
    message: Message,
    state: FSMContext
):
    data = await state.get_data()

    user = await UserRepository.get_by_telegram_id(
        message.from_user.id
    )

    await message.bot.send_message(
        ADMIN_ID,
        f"🏨 Yangi mehmonxona so'rovi\n\n"
        f"👤 Ism: {user.full_name}\n"
        f"📱 Telefon: {user.phone}\n\n"
        f"📍 Shahar: {data['city']}\n"
        f"📅 Kirish: {data['checkin']}\n"
        f"📅 Chiqish: {data['checkout']}\n"
        f"👥 Mehmonlar soni: {message.text}"
    )

    await state.clear()

    await message.answer(
        "✅ So'rovingiz qabul qilindi.\n\n"
        "Operator tez orada siz bilan bog'lanadi.",
        reply_markup=main_menu
    )
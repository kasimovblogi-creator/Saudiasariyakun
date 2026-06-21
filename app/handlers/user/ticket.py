from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.config.settings import GROUP_ID
from app.repositories.user_repository import UserRepository

from app.states.ticket import TicketState
from app.keyboards.main_menu import main_menu

router = Router()


@router.message(F.text == "✈️ Aviabiletlar")
async def ticket_start(
    message: Message,
    state: FSMContext
):

    await state.set_state(
        TicketState.waiting_from_city
    )

    await message.answer(
        "🛫 Qayerdan uchmoqchisiz?\n\n"
        "Masalan: Istanbul"
    )


@router.message(
    TicketState.waiting_from_city
)
async def from_city_handler(
    message: Message,
    state: FSMContext
):

    await state.update_data(
        from_city=message.text
    )

    await state.set_state(
        TicketState.waiting_to_city
    )

    await message.answer(
        "🛬 Qayerga uchmoqchisiz?\n\n"
        "Masalan: Jidda"
    )


@router.message(
    TicketState.waiting_to_city
)
async def to_city_handler(
    message: Message,
    state: FSMContext
):

    await state.update_data(
        to_city=message.text
    )

    await state.set_state(
        TicketState.waiting_date
    )

    await message.answer(
        "📅 Uchish sanasini kiriting\n\n"
        "Masalan: 25.07.2026"
    )


@router.message(
    TicketState.waiting_date
)
async def date_handler(
    message: Message,
    state: FSMContext
):

    data = await state.get_data()

    user = await UserRepository.get_by_telegram_id(
        message.from_user.id
    )

    await message.bot.send_message(
        ADMIN_ID,
        f"✈️ Yangi aviabilet so'rovi\n\n"
        f"👤 Ism: {user.full_name}\n"
        f"📱 Telefon: {user.phone}\n\n"
        f"🛫 Qayerdan: {data['from_city']}\n"
        f"🛬 Qayerga: {data['to_city']}\n"
        f"📅 Sana: {message.text}"
    )

    await state.clear()

    await message.answer(
        "✅ So'rovingiz qabul qilindi.\n\n"
        "Operator tez orada siz bilan bog'lanadi.",
        reply_markup=main_menu
    )
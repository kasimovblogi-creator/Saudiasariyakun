from aiogram import Router, F
from aiogram.types import Message

from app.config.settings import GROUP_ID
from app.repositories.user_repository import UserRepository

from app.keyboards.transport import transport_menu
from app.keyboards.main_menu import main_menu

router = Router()


@router.message(F.text == "🚕 Transport")
async def transport_menu_handler(message: Message):

    await message.answer(
        "🚕 Transport xizmatlari\n\n"
        "Kerakli xizmatni tanlang:",
        reply_markup=transport_menu
    )


@router.message(
    F.text.in_([
        "🚖 Taksi",
        "🚗 Avtomobil ijarasi",
        "🚌 Shaharlararo transport"
    ])
)
async def transport_handler(message: Message):

    user = await UserRepository.get_by_telegram_id(
        message.from_user.id
    )

    await message.bot.send_message(
        ADMIN_ID,
        f"🚕 Yangi transport so'rovi\n\n"
        f"👤 Ism: {user.full_name}\n"
        f"📱 Telefon: {user.phone}\n\n"
        f"🚘 Xizmat turi: {message.text}"
    )

    await message.answer(
        "✅ So'rovingiz qabul qilindi.\n\n"
        "Operator tez orada siz bilan bog'lanadi.",
        reply_markup=main_menu
    )


@router.message(F.text == "🔙 Asosiy menyu")
async def back_to_main_menu(message: Message):

    await message.answer(
        "🏠 Asosiy menyu\n\n"
        "Kerakli xizmatni tanlang:",
        reply_markup=main_menu
    )
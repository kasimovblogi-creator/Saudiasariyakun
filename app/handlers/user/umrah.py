from aiogram import Router, F
from aiogram.types import Message

from app.config.settings import GROUP_ID

from app.repositories.user_repository import UserRepository
from app.repositories.lead_repository import LeadRepository

from app.keyboards.umrah import umrah_menu
from app.keyboards.main_menu import main_menu

router = Router()


@router.message(F.text == "🕋 Umra Paketlari")
async def umrah_menu_handler(message: Message):

    await message.answer(
        "🕋 Umra Paketlari\n\n"
        "Kerakli paketni tanlang:",
        reply_markup=umrah_menu
    )


@router.message(
    F.text.in_([
        "⭐ Standard",
        "💎 Lyuks",
        "👑 VIP"
    ])
)
async def umrah_package_handler(message: Message):

    user = await UserRepository.get_by_telegram_id(
        message.from_user.id
    )

    await LeadRepository.create(
        user_id=user.id,
        service_type="umrah"
    )

    await message.bot.send_message(
        GROUP_ID,
        f"🕋 YANGI UMRA SO'ROVI\n\n"
        f"👤 Ism: {user.full_name}\n"
        f"📱 Telefon: {user.phone}\n"
        f"🆔 Telegram ID: {message.from_user.id}\n\n"
        f"📦 Paket: {message.text}"
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
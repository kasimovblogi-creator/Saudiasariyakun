from aiogram import Router, F
from aiogram.types import Message

from app.config.settings import ADMIN_ID
from app.repositories.user_repository import UserRepository

from app.keyboards.visa import visa_menu
from app.keyboards.main_menu import main_menu

router = Router()


@router.message(F.text == "🛂 Vizalar")
async def visa_menu_handler(message: Message):

    await message.answer(
        "🛂 Viza xizmatlari\n\n"
        "Kerakli viza turini tanlang:",
        reply_markup=visa_menu
    )


@router.message(
    F.text.in_([
        "💼 Biznes vizasi",
        "🕋 Umra vizasi",
        "👩 Singil vizasi",
        "📑 Multiple vizasi"
    ])
)
async def visa_type_handler(message: Message):

    user = await UserRepository.get_by_telegram_id(
        message.from_user.id
    )

    await message.bot.send_message(
        ADMIN_ID,
        f"🛂 Yangi viza so'rovi\n\n"
        f"👤 Ism: {user.full_name}\n"
        f"📱 Telefon: {user.phone}\n\n"
        f"📄 Viza turi: {message.text}"
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
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.config.settings import GROUP_ID
from app.repositories.user_repository import UserRepository

router = Router()


@router.message(F.text == "🎓 Universitetlar")
async def university_menu_handler(message: Message):

    builder = InlineKeyboardBuilder()

    builder.button(
        text="✅ Ha, tayyor",
        callback_data="university_ready"
    )

    builder.button(
        text="❌ Yo'q, hali tayyor emas",
        callback_data="university_not_ready"
    )

    builder.adjust(1)

    await message.answer(
        "🎓 Saudiya universitetlariga hujjat topshirish\n\n"
        "📌 Kerakli hujjatlar:\n\n"
        "✔️ Pasport\n"
        "✔️ Attestat yoki diplom\n"
        "✔️ Sudlanmaganlik ma'lumotnomasi\n"
        "✔️ 086 forma\n"
        "✔️ 4×6 surat\n\n"
        "Hujjatlaringiz tayyormi?",
        reply_markup=builder.as_markup()
    )


@router.callback_query(F.data == "university_ready")
async def university_ready(callback: CallbackQuery):

    user = await UserRepository.get_by_telegram_id(
        callback.from_user.id
    )

    await callback.bot.send_message(
        ADMIN_ID,
        f"🎓 Yangi universitet arizasi\n\n"
        f"👤 Ism: {user.full_name}\n"
        f"📱 Telefon: {user.phone}\n\n"
        f"✅ Hujjatlari tayyor"
    )

    await callback.message.edit_text(
        "✅ Arizangiz qabul qilindi.\n\n"
        "Operator tez orada siz bilan bog'lanadi."
    )

    await callback.answer()


@router.callback_query(F.data == "university_not_ready")
async def university_not_ready(callback: CallbackQuery):

    await callback.message.edit_text(
        "📌 Hujjatlaringiz tayyor bo'lgach qayta murojaat qiling."
    )

    await callback.answer()
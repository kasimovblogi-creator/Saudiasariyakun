from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.config.settings import GROUP_ID
from app.repositories.user_repository import UserRepository

from app.keyboards.inline_universities import (
    universities_page_1
)

router = Router()


@router.message(F.text == "📚 To'liq ma'lumot")
async def university_info_menu(message: Message):
    await message.answer(
        "🏫 Universitetni tanlang:",
        reply_markup=universities_page_1()
    )


@router.callback_query(F.data == "uni_king_khalid")
async def king_khalid_callback(callback: CallbackQuery):

    builder = InlineKeyboardBuilder()

    builder.button(
        text="ℹ️ Universitet haqida",
        callback_data="kku_about"
    )

    builder.button(
        text="🎁 Imtiyozlar",
        callback_data="kku_benefits"
    )

    builder.button(
        text="📄 Hujjatlar",
        callback_data="kku_documents"
    )

    builder.button(
        text="📝 Hujjat topshirish",
        callback_data="kku_apply"
    )

    builder.button(
        text="⬅️ Universitetlar",
        callback_data="back_universities"
    )

    builder.adjust(1)

    await callback.message.edit_text(
        "🏫 King Khalid University\n\n"
        "📍 Abha, Saudi Arabia\n\n"
        "Kerakli bo'limni tanlang:",
        reply_markup=builder.as_markup()
    )

    await callback.answer()


@router.callback_query(F.data == "back_universities")
async def back_universities(callback: CallbackQuery):

    await callback.message.edit_text(
        "🏫 Universitetni tanlang:",
        reply_markup=universities_page_1()
    )

    await callback.answer()


@router.callback_query(F.data == "kku_about")
async def kku_about(callback: CallbackQuery):

    await callback.message.edit_text(
        "🏫 King Khalid University\n\n"
        "📍 Joylashuvi: Abha, Asir viloyati, Saudiya Arabistoni\n\n"
        "📅 Tashkil etilgan: 1998-yil\n\n"
        "King Khalid University Saudiya Arabistonining eng yirik davlat universitetlaridan biridir."
    )

    await callback.answer()


@router.callback_query(F.data == "kku_benefits")
async def kku_benefits(callback: CallbackQuery):

    await callback.message.edit_text(
        "🎁 King Khalid University imtiyozlari\n\n"
        "✔️ Oylik stipendiya\n"
        "✔️ Bepul yotoqxona\n"
        "✔️ Aviabilet\n"
        "✔️ Tibbiy sug'urta\n"
        "✔️ Haj va Umra imkoniyati\n"
        "✔️ Oilani Saudiyaga olib kelish imkoniyati"
    )

    await callback.answer()


@router.callback_query(F.data == "kku_documents")
async def kku_documents(callback: CallbackQuery):

    await callback.message.edit_text(
        "📄 King Khalid University uchun kerakli hujjatlar\n\n"
        "✔️ Pasport\n"
        "✔️ Attestat yoki diplom\n"
        "✔️ Sudlanmaganlik ma'lumotnomasi\n"
        "✔️ 086 forma\n"
        "✔️ 4×6 surat"
    )

    await callback.answer()


@router.callback_query(F.data == "kku_apply")
async def kku_apply(callback: CallbackQuery):

    builder = InlineKeyboardBuilder()

    builder.button(
        text="✅ Ha, tayyor",
        callback_data="kku_apply_yes"
    )

    builder.button(
        text="❌ Yo'q, tayyor emas",
        callback_data="kku_apply_no"
    )

    builder.adjust(1)

    await callback.message.edit_text(
        "📄 Hujjatlaringiz tayyormi?",
        reply_markup=builder.as_markup()
    )

    await callback.answer()


@router.callback_query(F.data == "kku_apply_yes")
async def kku_apply_yes(callback: CallbackQuery):

    user = await UserRepository.get_by_telegram_id(
        callback.from_user.id
    )

    await callback.bot.send_message(
        GROUP_ID,
        f"🎓 YANGI UNIVERSITET SO'ROVI\n\n"
        f"🏫 Universitet: King Khalid University\n"
        f"👤 Ism: {user.full_name}\n"
        f"📱 Telefon: {user.phone}\n"
        f"🆔 Telegram ID: {callback.from_user.id}\n\n"
        f"📄 Hujjatlar tayyor: HA"
    )

    await callback.message.edit_text(
        "✅ So'rovingiz qabul qilindi.\n\n"
        "Operator tez orada siz bilan bog'lanadi."
    )

    await callback.answer()


@router.callback_query(F.data == "kku_apply_no")
async def kku_apply_no(callback: CallbackQuery):

    await callback.message.edit_text(
        "📄 Hujjatlaringiz tayyor bo'lgach qayta murojaat qiling.\n\n"
        "👨‍💼 Operator: @saudia_sari"
    )

    await callback.answer()
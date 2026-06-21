from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

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
        "King Khalid University 1998-yilda Imam Muhammad bin Saud Islamic University va King Saud University filiallari birlashtirilishi natijasida tashkil etilgan.\n\n"
        "Bugungi kunda universitet Saudiya Arabistonining eng yirik davlat universitetlaridan biri hisoblanadi. Unda 50 000 dan ortiq talaba tahsil oladi hamda 26 ta kollej tarkibida 180 dan ortiq ta'lim dasturlari mavjud.\n\n"
        "Universitet Asir mintaqasidagi yetakchi oliy ta'lim muassasalaridan biri bo'lib, bakalavr, magistratura va doktorantura bosqichlarida ta'lim beradi."
    )

    await callback.answer()


@router.callback_query(F.data == "kku_benefits")
async def kku_benefits(callback: CallbackQuery):

    await callback.message.edit_text(
        "🎁 King Khalid University imtiyozlari\n\n"
        "💵 Talabalarga beriladigan imkoniyatlar:\n\n"
        "✔️ Oylik stipendiya\n"
        "✔️ Bepul yotoqxona\n"
        "✔️ Aviabilet\n"
        "✔️ Tibbiy sug'urta\n"
        "✔️ Haj va Umra imkoniyati\n"
        "✔️ Arzon universitet restoranlari\n"
        "✔️ Oilani Saudiyaga olib kelish imkoniyati\n\n"
        "⚠️ Ayrim imtiyozlar fakultet va qabul dasturiga qarab farq qilishi mumkin."
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
        "✔️ 4×6 surat\n\n"
        "⚠️ Qo'shimcha hujjatlar talab qilinishi mumkin."
    )

    await callback.answer()


@router.callback_query(F.data == "kku_apply")
async def kku_apply(callback: CallbackQuery):

    await callback.message.answer(
        "📝 Hujjat topshirish uchun Universitetlar menyusidagi "
        "'📝 Hujjat topshirish' bo'limidan foydalaning."
    )

    await callback.answer()
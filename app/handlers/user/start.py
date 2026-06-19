from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.config.settings import ADMIN_ID

from app.states.register import RegisterState

from app.keyboards.contact import contact_keyboard
from app.keyboards.main_menu import main_menu

from app.repositories.user_repository import UserRepository

from app.utils.subscription import (
    check_subscription,
    subscribe_keyboard
)

router = Router()


@router.message(CommandStart())
async def start_handler(
    message: Message,
    state: FSMContext
):

    is_subscribed = await check_subscription(
        message.bot,
        message.from_user.id
    )

    if not is_subscribed:
        await message.answer(
            "📢 Botdan foydalanish uchun avval kanalimizga obuna bo'ling.\n\n"
            "Obuna bo'lgach qayta /start bosing.",
            reply_markup=subscribe_keyboard()
        )
        return

    user = await UserRepository.get_by_telegram_id(
        message.from_user.id
    )

    if user:
        await message.answer(
            f"🤝 Assalomu alaykum, {user.full_name}!\n\n"
            "🇸🇦 Saudiya Sari platformasiga xush kelibsiz.\n\n"
            "Biz sizga Saudiya Arabistonida:\n\n"
            "🎓 Universitetlarga hujjat topshirish\n"
            "🕋 Umra safarlari\n"
            "🛂 Viza xizmatlari\n"
            "✈️ Aviabiletlar\n"
            "🏨 Mehmonxona va hostel bron qilish\n"
            "🚕 Transport xizmatlari\n\n"
            "shu sohalarda yordam beramiz.\n\n"
            "📌 Kerakli xizmatni menyudan tanlang.",
            reply_markup=main_menu
        )
        return

    await state.set_state(
        RegisterState.waiting_phone
    )

    await message.answer(
        "🇸🇦 Saudiya Sari platformasiga xush kelibsiz!\n\n"
        "Botdan foydalanish uchun telefon raqamingizni yuboring 📱",
        reply_markup=contact_keyboard
    )


@router.message(RegisterState.waiting_phone)
async def phone_handler(
    message: Message,
    state: FSMContext
):

    if not message.contact:
        await message.answer(
            "❗ Iltimos, telefon raqamni tugma orqali yuboring."
        )
        return

    await UserRepository.create_user(
        telegram_id=message.from_user.id,
        full_name=message.from_user.full_name,
        phone=message.contact.phone_number,
        username=message.from_user.username
    )

    user_count = await UserRepository.get_users_count()

    await message.bot.send_message(
        ADMIN_ID,
        f"🆕 Yangi foydalanuvchi qo'shildi\n\n"
        f"👤 Ism: {message.from_user.full_name}\n"
        f"📞 Telefon: {message.contact.phone_number}\n"
        f"👤 Username: @{message.from_user.username if message.from_user.username else 'Mavjud emas'}\n"
        f"🆔 Telegram ID: {message.from_user.id}\n\n"
        f"📊 Umumiy foydalanuvchilar: {user_count}"
    )

    await state.clear()

    await message.answer(
        "✅ Ro'yxatdan o'tish muvaffaqiyatli yakunlandi!\n\n"
        "🤝 Saudiya Sari platformasiga xush kelibsiz.\n\n"
        "📌 Endi quyidagi menyudan xizmat tanlang:",
        reply_markup=main_menu
    )
from aiogram import Router, F
from aiogram.types import CallbackQuery

from app.repositories.user_repository import UserRepository
from app.keyboards.main_menu import main_menu

from app.utils.subscription import (
    check_subscription,
    subscribe_keyboard
)

router = Router()


@router.callback_query(
    F.data == "check_subscription"
)
async def check_sub_callback(
    callback: CallbackQuery
):

    is_subscribed = await check_subscription(
        callback.bot,
        callback.from_user.id
    )

    if not is_subscribed:
        await callback.answer(
            "❌ Siz hali kanalga obuna bo'lmagansiz.",
            show_alert=True
        )
        return

    user = await UserRepository.get_by_telegram_id(
        callback.from_user.id
    )

    if user:
        await callback.message.edit_text(
            f"✅ Obunangiz muvaffaqiyatli tasdiqlandi!\n\n"
            f"🤝 Assalomu alaykum, {user.full_name}!\n\n"
            f"🇸🇦 Saudiya Sari platformasiga xush kelibsiz.\n\n"
            f"📚 Bepul qo'llanmani ko'rish uchun quyidagi havolaga o'ting:\n\n"
            f"🎥 https://youtu.be/RKblPCGf0TQ\n\n"
            f"❓ Savollaringiz bo'lsa administrator bilan bog'laning:\n\n"
            f"👉 @saudia_sari\n\n"
            f"📌 Quyidagi menyudan kerakli xizmatni tanlang."
        )

        await callback.message.answer(
            "🏠 Asosiy menyu",
            reply_markup=main_menu
        )

    await callback.answer()
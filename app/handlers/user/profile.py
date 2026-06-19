from aiogram import Router, F
from aiogram.types import Message

from app.repositories.user_repository import UserRepository

router = Router()


@router.message(F.text == "👤 Profil")
async def profile_handler(message: Message):

    user = await UserRepository.get_by_telegram_id(
        message.from_user.id
    )

    if not user:
        await message.answer(
            "Foydalanuvchi topilmadi."
        )
        return

    text = (
        "👤 Profil\n\n"
        f"🆔 ID: {user.telegram_id}\n"
        f"👨 Ism: {user.full_name}\n"
        f"📱 Telefon: {user.phone}\n"
        f"🔗 Username: @{user.username if user.username else 'Mavjud emas'}"
    )

    await message.answer(text)
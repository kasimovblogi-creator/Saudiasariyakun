from aiogram import Router, F
from aiogram.types import Message

router = Router()


@router.message(F.text == "☎️ Operator")
async def operator_handler(message: Message):

    await message.answer(
        "👨‍💼 Operator bilan bog'lanish\n\n"
        "📩 Telegram:\n"
        "@saudia_sari\n\n"
        "Savollaringiz bo'lsa yoki xizmatlardan foydalanmoqchi bo'lsangiz, operatorimizga murojaat qiling."
    )
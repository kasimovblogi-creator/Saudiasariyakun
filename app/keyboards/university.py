from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton
)

university_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="📚 To'liq ma'lumot"
            )
        ],
        [
            KeyboardButton(
                text="📝 Hujjat topshirish"
            )
        ],
        [
            KeyboardButton(
                text="⬅️ Orqaga"
            )
        ]
    ],
    resize_keyboard=True
)
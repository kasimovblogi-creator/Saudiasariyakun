from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

umrah_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⭐ Standard")
        ],
        [
            KeyboardButton(text="💎 Lyuks")
        ],
        [
            KeyboardButton(text="👑 VIP")
        ],
        [
            KeyboardButton(text="🔙 Asosiy menyu")
        ]
    ],
    resize_keyboard=True
)
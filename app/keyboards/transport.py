from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

transport_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🚖 Taksi")],
        [KeyboardButton(text="🚗 Avtomobil ijarasi")],
        [KeyboardButton(text="🚌 Shaharlararo transport")],
        [KeyboardButton(text="🔙 Asosiy menyu")]
    ],
    resize_keyboard=True
)
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

visa_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💼 Biznes vizasi")],
        [KeyboardButton(text="🕋 Umra vizasi")],
        [KeyboardButton(text="👩 Singil vizasi")],
        [KeyboardButton(text="📑 Multiple vizasi")],
        [KeyboardButton(text="🔙 Asosiy menyu")]
    ],
    resize_keyboard=True
)
from aiogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup
)


contact_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="📱 Telefon raqam yuborish",
                request_contact=True
            )
        ]
    ],
    resize_keyboard=True
)
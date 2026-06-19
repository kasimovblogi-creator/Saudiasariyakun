from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🎓 Universitetlar"),
            KeyboardButton(text="🕋 Umra Paketlari")
        ],
        [
            KeyboardButton(text="🛂 Vizalar"),
            KeyboardButton(text="✈️ Aviabiletlar")
        ],
        [
            KeyboardButton(text="🏨 Hotel / Hostel"),
            KeyboardButton(text="🚕 Transport")
        ],
        [
            KeyboardButton(text="👤 Profil"),
            KeyboardButton(text="☎️ Operator")
        ]
    ],
    resize_keyboard=True
)
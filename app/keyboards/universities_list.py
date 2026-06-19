from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton
)

universities_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🏫 King Khalid University")],
        [KeyboardButton(text="🏫 King Saud University")],
        [KeyboardButton(text="🏫 Umm al-Qura University")],
        [KeyboardButton(text="🏫 King Faisal University")],
        [KeyboardButton(text="🏫 King Abdulaziz University")],
        [KeyboardButton(text="🏫 Islamic University of Madinah")],
        [KeyboardButton(text="🏫 Taibah University")],
        [KeyboardButton(text="🏫 Prince Sattam bin Abdulaziz University")],
        [KeyboardButton(text="🏫 University of Jeddah")],
        [KeyboardButton(text="🏫 Princess Nourah bint Abdulrahman University")],
        [KeyboardButton(text="🏫 Majmaah University")],
        [KeyboardButton(text="🏫 Qassim University")],
        [KeyboardButton(text="🏫 University of Tabuk")],
        [KeyboardButton(text="🏫 Northern Border University")],
        [KeyboardButton(text="🏫 Imam Abdulrahman Bin Faisal University")],
        [KeyboardButton(text="🏫 University of Bisha")],
        [KeyboardButton(text="🏫 Jazan University")],
        [KeyboardButton(text="🏫 Imam Muhammad bin Saud Islamic University")],
        [KeyboardButton(text="🏫 Al-Baha University")],
        [KeyboardButton(text="🏫 University of Hafr Al Batin")],
        [KeyboardButton(text="🏫 Shaqra University")],
        [KeyboardButton(text="🏫 Najran University")],
        [KeyboardButton(text="🏫 Jouf University")],
        [KeyboardButton(text="🏫 University of Hail")],

        [KeyboardButton(text="⬅️ Universitetlar")]
    ],
    resize_keyboard=True
)
from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

from app.config.settings import CHANNEL_USERNAME


async def check_subscription(
    bot,
    user_id: int
):
    member = await bot.get_chat_member(
        CHANNEL_USERNAME,
        user_id
    )

    return member.status in [
        "member",
        "administrator",
        "creator"
    ]


def subscribe_keyboard():

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📢 Kanalga obuna bo'lish",
                    url=f"https://t.me/{CHANNEL_USERNAME.replace('@', '')}"
                )
            ],
            [
                InlineKeyboardButton(
                    text="✅ Obunani tekshirish",
                    callback_data="check_subscription"
                )
            ]
        ]
    )
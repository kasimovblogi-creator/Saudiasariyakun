from aiogram import Router, F
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(F.data == "check_subscription")
async def check_sub_callback(callback: CallbackQuery):

    print("CHECK SUBSCRIPTION BOSILDI")

    await callback.answer(
        "TEST",
        show_alert=True
    )
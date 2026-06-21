from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from app.states.register import RegisterState
from app.keyboards.contact import contact_keyboard

from app.utils.subscription import (
    check_subscription
)

router = Router()


@router.callback_query(F.data == "check_subscription")
async def check_sub_callback(
    callback: CallbackQuery,
    state: FSMContext
):

    is_subscribed = await check_subscription(
        callback.bot,
        callback.from_user.id
    )

    if not is_subscribed:
        await callback.answer(
            "❌ Siz hali kanalga obuna bo'lmagansiz.",
            show_alert=True
        )
        return

    await state.set_state(
        RegisterState.waiting_phone
    )

    await callback.message.edit_text(
        "✅ Obunangiz muvaffaqiyatli tasdiqlandi!\n\n"
        "📱 Endi telefon raqamingizni yuboring."
    )

    await callback.message.answer(
        "Telefon raqamingizni yuborish uchun tugmani bosing 👇",
        reply_markup=contact_keyboard
    )

    await callback.answer()
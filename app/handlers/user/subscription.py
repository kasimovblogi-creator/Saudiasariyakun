@router.callback_query(F.data == "check_subscription")
async def check_sub_callback(callback: CallbackQuery):

    try:
        is_subscribed = await check_subscription(
            callback.bot,
            callback.from_user.id
        )

        print(f"SUBSCRIBED: {is_subscribed}")

        if not is_subscribed:
            await callback.answer(
                "❌ Siz hali kanalga obuna bo'lmagansiz.",
                show_alert=True
            )
            return

        user = await UserRepository.get_by_telegram_id(
            callback.from_user.id
        )

        print(f"USER: {user}")

        await callback.message.answer(
            "TEST MUVAFFAQIYATLI"
        )

        await callback.answer()

    except Exception as e:
        print(f"SUBSCRIPTION ERROR: {e}")

        await callback.answer(
            "Xatolik yuz berdi",
            show_alert=True
        )
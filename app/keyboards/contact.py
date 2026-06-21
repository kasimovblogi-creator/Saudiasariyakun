@router.message(RegisterState.waiting_phone)
async def phone_handler(
    message: Message,
    state: FSMContext
):
    print("PHONE HANDLER ISHLADI")
    print("CONTACT:", message.contact)
    print("TEXT:", message.text)

    if not message.contact:
        await message.answer(
            "❗ Iltimos, telefon raqamni tugma orqali yuboring."
        )
        return

    await message.answer("TEST PHONE QABUL QILINDI")
from aiogram.utils.keyboard import InlineKeyboardBuilder


def universities_page_1():
    builder = InlineKeyboardBuilder()

    builder.button(
        text="🏫 King Khalid University",
        callback_data="uni_king_khalid"
    )

    builder.button(
        text="🏫 King Saud University",
        callback_data="uni_king_saud"
    )

    builder.button(
        text="🏫 Umm al-Qura University",
        callback_data="uni_umm_al_qura"
    )

    builder.button(
        text="🏫 King Faisal University",
        callback_data="uni_king_faisal"
    )

    builder.button(
        text="🏫 King Abdulaziz University",
        callback_data="uni_king_abdulaziz"
    )

    builder.button(
        text="➡️ Keyingi",
        callback_data="page_2"
    )

    builder.adjust(1)

    return builder.as_markup()


def universities_page_2():
    builder = InlineKeyboardBuilder()

    builder.button(
        text="🏫 Islamic University of Madinah",
        callback_data="uni_madinah"
    )

    builder.button(
        text="🏫 Taibah University",
        callback_data="uni_taibah"
    )

    builder.button(
        text="🏫 Prince Sattam bin Abdulaziz University",
        callback_data="uni_psau"
    )

    builder.button(
        text="🏫 University of Jeddah",
        callback_data="uni_jeddah"
    )

    builder.button(
        text="🏫 Princess Nourah University",
        callback_data="uni_pnu"
    )

    builder.button(
        text="⬅️ Oldingi",
        callback_data="page_1"
    )

    builder.button(
        text="➡️ Keyingi",
        callback_data="page_3"
    )

    builder.adjust(1)

    return builder.as_markup()
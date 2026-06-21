from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.config.settings import GROUP_ID

from app.repositories.user_repository import UserRepository
from app.repositories.lead_repository import LeadRepository

router = Router()


@router.message(Command("admin"))
async def admin_stats(message: Message):

    if message.from_user.id != ADMIN_ID:
        return

    users = await UserRepository.get_total()

    university = await LeadRepository.get_by_service(
        "university"
    )

    umrah = await LeadRepository.get_by_service(
        "umrah"
    )

    visa = await LeadRepository.get_by_service(
        "visa"
    )

    ticket = await LeadRepository.get_by_service(
        "ticket"
    )

    hotel = await LeadRepository.get_by_service(
        "hotel"
    )

    transport = await LeadRepository.get_by_service(
        "transport"
    )

    total_leads = await LeadRepository.get_total()

    await message.answer(
        f"📊 Saudiya Sari Statistikasi\n\n"
        f"👥 Foydalanuvchilar: {users}\n\n"
        f"🎓 Universitet: {university}\n"
        f"🕋 Umra: {umrah}\n"
        f"🛂 Vizalar: {visa}\n"
        f"✈️ Aviabiletlar: {ticket}\n"
        f"🏨 Hotel: {hotel}\n"
        f"🚕 Transport: {transport}\n\n"
        f"📈 Jami leadlar: {total_leads}"
    )
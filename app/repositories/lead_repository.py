from sqlalchemy import select, func

from app.database.db import async_session
from app.models.lead import Lead


class LeadRepository:

    @staticmethod
    async def create(
        user_id: int,
        service_type: str
    ):
        async with async_session() as session:

            lead = Lead(
                user_id=user_id,
                service_type=service_type
            )

            session.add(lead)

            await session.commit()

    @staticmethod
    async def get_total():

        async with async_session() as session:

            result = await session.execute(
                select(func.count(Lead.id))
            )

            return result.scalar() or 0

    @staticmethod
    async def get_by_service(
        service_type: str
    ):

        async with async_session() as session:

            result = await session.execute(
                select(func.count(Lead.id))
                .where(
                    Lead.service_type == service_type
                )
            )

            return result.scalar() or 0
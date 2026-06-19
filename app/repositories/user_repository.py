from sqlalchemy import select, func

from app.database.db import async_session
from app.models.user import User


class UserRepository:

    @staticmethod
    async def get_by_telegram_id(
        telegram_id: int
    ):
        async with async_session() as session:

            result = await session.execute(
                select(User).where(
                    User.telegram_id == telegram_id
                )
            )

            return result.scalar_one_or_none()

    @staticmethod
    async def create_user(
        telegram_id: int,
        full_name: str,
        phone: str,
        username: str | None
    ):
        async with async_session() as session:

            user = User(
                telegram_id=telegram_id,
                full_name=full_name,
                phone=phone,
                username=username
            )

            session.add(user)

            await session.commit()

            return user

    @staticmethod
    async def get_total():

        async with async_session() as session:

            result = await session.execute(
                select(func.count(User.id))
            )

            return result.scalar() or 0
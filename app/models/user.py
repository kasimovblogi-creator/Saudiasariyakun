from datetime import datetime

from sqlalchemy import (
    BigInteger,
    DateTime,
    String
)

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.database.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    telegram_id: Mapped[int] = mapped_column(
        BigInteger,
        unique=True
    )

    full_name: Mapped[str] = mapped_column(
        String(255)
    )

    phone: Mapped[str] = mapped_column(
        String(30)
    )

    username: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )
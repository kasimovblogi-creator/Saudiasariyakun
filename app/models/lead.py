from sqlalchemy import (
    Integer,
    String,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from datetime import datetime

from app.database.base import Base


class Lead(Base):
    __tablename__ = "leads"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    service_type: Mapped[str] = mapped_column(
        String(50)
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )
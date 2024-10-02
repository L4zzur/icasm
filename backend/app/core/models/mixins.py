from datetime import datetime, timezone
from uuid import UUID, uuid4

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column


class IdMixin:
    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        unique=True,
        nullable=False,
        default=uuid4,
        comment="Идентификатор",
    )


class CreatedAtMixin:
    created_at: Mapped[datetime] = mapped_column(
        default=datetime.now(timezone.utc),
        server_default=func.now(),
        comment="Время создания",
    )

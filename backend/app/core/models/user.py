from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixins import CreatedAtMixin, IdMixin


class User(Base, IdMixin, CreatedAtMixin):
    tg_id: Mapped[int] = mapped_column(
        nullable=False,
        unique=True,
        comment="Telegram ID пользователя",
    )
    name: Mapped[str] = mapped_column(
        nullable=False,
        comment="Имя пользователя",
    )
    username: Mapped[str] = mapped_column(
        nullable=True,
        comment="Юзернейм пользователя",
    )
    is_premium: Mapped[bool] = mapped_column(
        nullable=False,
        default=False,
        comment="Куплен ли премиум",
    )

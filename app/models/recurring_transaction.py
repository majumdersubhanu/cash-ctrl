import datetime
import uuid
from decimal import Decimal
from typing import TYPE_CHECKING, Optional

from sqlalchemy import Date, ForeignKey, Numeric, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.db.mixins import TimestampMixin, UUIDMixin
from app.utils.enums import TransactionType

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.account import Account
    from app.models.category import Category


class RecurringTransaction(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "recurring_transactions"

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    account_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("accounts.id"))
    category_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        ForeignKey("categories.id")
    )

    amount: Mapped[Decimal] = mapped_column(Numeric(12, 2))
    type: Mapped[TransactionType]


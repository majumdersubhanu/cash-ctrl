import uuid
from typing import TYPE_CHECKING, Optional

from sqlalchemy import ForeignKey, String, Boolean, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.db.mixins import TimestampMixin, UUIDMixin
from app.utils.enums import AccountType

if TYPE_CHECKING:
    from app.models.user import User


class Account(Base, UUIDMixin, TimestampMixin):

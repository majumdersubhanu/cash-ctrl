import datetime
import uuid
from decimal import Decimal
from typing import TYPE_CHECKING, Optional, List

from sqlalchemy import ForeignKey, String, Date, Numeric, Text, Enum, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.db.mixins import TimestampMixin, UUIDMixin
from app.utils.enums import LoanStatus, LoanRepaymentFrequency

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.contact import Contact

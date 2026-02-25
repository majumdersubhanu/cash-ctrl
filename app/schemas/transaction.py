from datetime import date, datetime
from decimal import Decimal
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict

from app.utils.enums import TransactionType


class TransactionCreate(BaseModel):
    account_id: UUID
    category_id: Optional[UUID] = None
    type: TransactionType
    amount: Decimal

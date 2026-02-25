import datetime
from decimal import Decimal
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict
from app.utils.enums import LoanStatus, LoanRepaymentFrequency


class ContactBase(BaseModel):
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None


class ContactCreate(ContactBase):
    linked_user_id: Optional[UUID] = None


class ContactResponse(ContactBase):
    id: UUID
    linked_user_id: Optional[UUID] = None
    trust_score: float
    is_trusted: bool

    model_config = ConfigDict(from_attributes=True)


class LoanAgreementCreate(BaseModel):
    frequency: LoanRepaymentFrequency

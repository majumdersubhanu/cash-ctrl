import uuid
from datetime import date
from typing import Sequence
from dateutil.relativedelta import relativedelta

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.recurring_transaction import RecurringTransaction
from app.services.transaction_service import TransactionService


class RecurringTransactionService:
    def __init__(self):
        self.tx_service = TransactionService()

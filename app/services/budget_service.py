import uuid
from datetime import datetime
from decimal import Decimal
from typing import Sequence

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.budget import Budget
from app.models.transaction import Transaction
from app.utils.enums import TransactionType


class BudgetService:
    async def create_budget(

import uuid
from datetime import datetime
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Dict, Any

from app.models.transaction import Transaction
from app.models.account import Account
from app.models.budget import Budget
from app.utils.enums import TransactionType

class HealthAuditService:
    """Service for performing comprehensive financial health audits for users."""

    async def perform_audit(self, db: AsyncSession, user_id: uuid.UUID) -> Dict[str, Any]:
        """
        Runs a full financial health audit.
        
        Args:
            db: Async database session.
            user_id: The ID of the user to audit.
            
        Returns:
            A dictionary containing health metrics.
        """
        now = datetime.now()
        
        # 1. Monthly Income & Expense
        income_stmt = select(func.sum(Transaction.amount)).where(
            Transaction.user_id == user_id,
            Transaction.type == TransactionType.INCOME,
            func.extract('month', Transaction.transaction_date) == now.month,
            func.extract('year', Transaction.transaction_date) == now.year
        )
        expense_stmt = select(func.sum(Transaction.amount)).where(
            Transaction.user_id == user_id,
            Transaction.type == TransactionType.EXPENSE,
            func.extract('month', Transaction.transaction_date) == now.month,
            func.extract('year', Transaction.transaction_date) == now.year
        )
        
        monthly_income = float((await db.execute(income_stmt)).scalar() or 0.0)
        monthly_expense = float((await db.execute(expense_stmt)).scalar() or 0.0)
        
        # 2. Savings Rate: (Income - Expense) / Income
        savings_rate = 0.0
        if monthly_income > 0:
            savings_rate = (monthly_income - monthly_expense) / monthly_income
            
        # 3. Emergency Fund Progress
        # We define liquidity as accounts of type BANK or CASH
        liquid_stmt = select(func.sum(Account.balance)).where(
            Account.user_id == user_id,
            Account.type.in_(['BANK', 'CASH'])
        )
        total_liquid = float((await db.execute(liquid_stmt)).scalar() or 0.0)
        
        # Calculate avg monthly expense (last 3 months)
        # Assuming we just use the current month if history is short for simplicity in this baseline
        emergency_fund_months = 0.0
        if monthly_expense > 0:
            emergency_fund_months = total_liquid / monthly_expense

        # 4. Budget Adherence
        budget_stmt = select(Budget).where(Budget.user_id == user_id)
        budgets = (await db.execute(budget_stmt)).scalars().all()
        
        over_budget_categories = 0
        for b in budgets:
            cat_exp_stmt = select(func.sum(Transaction.amount)).where(
                Transaction.user_id == user_id,
                Transaction.category_id == b.category_id,
                Transaction.type == TransactionType.EXPENSE,
                func.extract('month', Transaction.transaction_date) == now.month
            )

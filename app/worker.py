import asyncio
from datetime import date
from dateutil.relativedelta import relativedelta

from celery import Celery
from celery.schedules import crontab
from loguru import logger
from sqlalchemy import select

from app.core.config import settings
from app.db.session import SessionLocal
from app.models.loan import Loan, LoanAgreement
from app.models.recurring_transaction import RecurringTransaction
from app.models.transaction import Transaction
from app.models.notification import NotificationType

import uuid
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.api.deps import get_db
from app.core.users import current_active_user
from app.models.user import User
from app.models.loan import Loan
from app.schemas.p2p import LoanResponse


router = APIRouter(tags=["social"])

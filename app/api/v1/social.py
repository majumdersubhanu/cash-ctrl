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


@router.get("/vouch-score")
async def get_my_vouch_score(user: User = Depends(current_active_user)):
    """
    Returns the active authenticated user's Vouch Score.
    """
    return {"vouch_score": user.vouch_score}


@router.get("/contacts/{contact_id}/ledger", response_model=List[LoanResponse])
async def get_contact_public_ledger(
    contact_id: uuid.UUID,
    user: User = Depends(current_active_user),
    db: AsyncSession = Depends(get_db),

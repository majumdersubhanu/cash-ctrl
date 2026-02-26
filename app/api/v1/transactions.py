from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db
from app.core.users import current_active_user
from app.models.user import User
from app.schemas.transaction import (
    TransactionCreate,
    TransactionResponse,
    TransactionFilter,
    TransferCreate,
    BulkDeleteRequest,
)
from app.services.transaction_service import TransactionService

router = APIRouter(tags=["transactions"])


async def get_transaction_service() -> TransactionService:
    return TransactionService()


@router.post("/", response_model=TransactionResponse)
async def create_transaction(
    payload: TransactionCreate,
    user: User = Depends(current_active_user),
    db: AsyncSession = Depends(get_db),
    service: TransactionService = Depends(get_transaction_service),
):
    try:

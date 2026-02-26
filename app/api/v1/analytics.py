from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db
from app.core.users import current_active_user
from app.models.user import User
from app.services.analytics_service import AnalyticsService

router = APIRouter(tags=["analytics"])


async def get_analytics_service() -> AnalyticsService:
    return AnalyticsService()



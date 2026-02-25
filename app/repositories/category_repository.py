import uuid
from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.category import Category
from app.repositories.base_repository import BaseRepository
from app.utils.enums import CategoryType


class CategoryRepository(BaseRepository[Category]):
    def __init__(self):
        super().__init__(Category)


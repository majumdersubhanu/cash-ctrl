import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.category import Category
from app.repositories.category_repository import CategoryRepository
from app.utils.enums import CategoryType


class CategoryService:
    def __init__(self):
        self.repo = CategoryRepository()

    async def create_category(
        self,

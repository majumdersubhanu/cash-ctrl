import uuid
from typing import Sequence
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.goal import Goal


class GoalService:
    async def create_goal(self, db: AsyncSession, user_id: uuid.UUID, payload) -> Goal:
        goal = Goal(
            user_id=user_id,
            account_id=payload.account_id,
            name=payload.name,
            target_amount=payload.target_amount,
            deadline=payload.deadline,
        )
        db.add(goal)
        await db.commit()
        await db.refresh(goal)
        goal.percent_complete = 0.0
        return goal

    async def get_user_goals(
        self, db: AsyncSession, user_id: uuid.UUID
    ) -> Sequence[Goal]:
        stmt = select(Goal).where(Goal.user_id == user_id)
        result = await db.execute(stmt)
        goals = result.scalars().all()

        for goal in goals:

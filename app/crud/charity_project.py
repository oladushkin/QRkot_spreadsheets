# app\crud\charity_project.py
from typing import Optional

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.charity_project import CharityProject


class CRUDCharityProject(CRUDBase):

    async def get_project_id_by_name(
            self,
            project_name: str,
            session: AsyncSession,
    ) -> Optional[int]:
        db_project_id = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == project_name
            )
        )
        db_project_id = db_project_id.scalars().first()
        return db_project_id

    async def get_projects_by_completion_rate(
            self,
            session: AsyncSession
    ):
        close_obj = await session.execute(
            select([
                CharityProject.name,
                (func.julianday(CharityProject.close_date) - func.julianday(CharityProject.create_date)).label('time'),
                CharityProject.description
            ]).where(CharityProject.fully_invested).order_by('time')
        )
        return close_obj.scalars().all()


charity_project_crud = CRUDCharityProject(CharityProject)

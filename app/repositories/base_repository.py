from abc import ABC, abstractmethod
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, select, delete, update

from app.repositories.models import ColumnValue

class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(self, data: dict):
        ...

    @abstractmethod
    async def get_all_data(self):
        ...

    @abstractmethod
    async def delete_by_id(self, id: int):
        ...

    @abstractmethod
    async def update_one(self, column_and_value: ColumnValue, values_to_update: dict):
        ...

class Repository(AbstractRepository):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_one(self, data: dict):
        query = insert(self.model).values(**data).returning(self.model)
        result = await self.session.execute(query)
        return result.scalar_one()

    async def find_one(self, **filters):
        query = select(self.model).filter_by(**filters)
        result = await self.session.execute(query)
        return result.scalar_one()

    async def get_all_data(self):
        query = select(self.model)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def delete_by_id(self, id: int):
        query = delete(self.model).where(self.model.id == id).returning(self.model)
        result = await self.session.execute(query)
        return result.scalar_one()

    async def update_one(self, column_and_value: ColumnValue, values: dict):
        column = getattr(self.model, column_and_value.column_name)
        query = update(self.model).where(column == column_and_value.column_value).values(**values).returning(self.model)
        result = await self.session.execute(query)
        return result.scalar_one()
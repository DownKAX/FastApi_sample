from typing import Any

from app.repositories.models import ColumnValue
from app.utils.UnitOfWork import Uow
from app.api.models.example_models import ExampleModel
from app.services.dependencies.validators import unique_validation, exists_validation

class ExampleService:
    def __init__(self, uow: Uow):
        self.uow = uow

    async def add_one_example(self, data: ExampleModel) -> ExampleModel:
        data = data.model_dump()
        async with self.uow:
            result = await unique_validation(self.uow.example_model.add_one, data,
                                       e_message="Some data is not unique, try something else")
            result: ExampleModel = ExampleModel.model_validate(result.__dict__)
            await self.uow.commit()
            return result

    async def select_all_examples(self, return_value: str | None = None) -> list[ExampleModel] | list[Any]:
        async with self.uow:
            result = await exists_validation(self.uow.example_model.get_all_data, e_message="Example db is empty")
            result: list[ExampleModel] = [ExampleModel.model_validate(r.__dict__) for r in result]
            return result if not return_value else [getattr(x, return_value) for x in result]

    async def delete_data_by_id(self, id: int) -> ExampleModel:
        async with self.uow:
            result = await exists_validation(self.uow.example_model.delete_by_id, id,
                                             e_message="No such example to delete")
            result: ExampleModel = ExampleModel.model_validate(result.__dict__)
            await self.uow.commit()
            return result

    # colum_and_value - колонка и значение, которые используются для поиска записи в бд, которую будем изменять
    # values - одно или несколько значений внутри словаря, которые будут новыми значениями для записи в бд
    async def update_one_example(self, column_and_value: ColumnValue, values: dict) -> ExampleModel:
        async with self.uow:
            result = await unique_validation(self.uow.example_model.update_one, column_and_value, values,
                                             e_message="Some data is not unique, try something else")
            result: ExampleModel = ExampleModel.model_validate(result.__dict__)
            await self.uow.commit()
            return result


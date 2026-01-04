from fastapi import Depends
from typing import Annotated

from app.utils.UnitOfWork import Uow, AbstractUow
from app.services.example_service import ExampleService

async def get_example_service(uow: AbstractUow = Depends(Uow)):
    return ExampleService(uow)

example_dependency = Annotated[ExampleService, Depends(get_example_service)]
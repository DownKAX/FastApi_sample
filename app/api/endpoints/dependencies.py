from fastapi import Depends
from typing import Annotated

from app.utils.UnitOfWork import Uow, AbstractUow
from app.services.user_service import UserService

async def get_service(uow: AbstractUow = Depends(Uow)):
    return Service(uow)

dependency = Annotated[UserService, Depends(service)]
from fastapi import APIRouter

from app.api.endpoints.dependencies import dependency

user_router = APIRouter(prefix='/blank')

@user_router.post('/create_data')
async def create_user(user_service: dependency):
    pass

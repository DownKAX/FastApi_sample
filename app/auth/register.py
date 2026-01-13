import hashlib

import bcrypt
from fastapi import APIRouter, Request, Response, Form, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.auth.dependencies import user_dependency
from app.auth.exceptions import InvalidPasswordException, ExpiredAccessToken, InvalidRefreshToken
from app.auth.models import RegistrationForm, User, Tokens
from app.auth.redis_repository import get_data_from_redis
from app.auth.security import verification_stamp, get_jwt_tokens, validate_access_token, check_session

auth = APIRouter(prefix="/auth")

@auth.post('/signup')
async def register(user_service: user_dependency, credentials: RegistrationForm = Form(...)):
    password_bytes: bytes = credentials.password.encode('utf-8')
    hashed_password: bytes = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    user_data = User(username=credentials.username, password=hashed_password.decode())
    await user_service.add_one_user(user_data)
    return user_data

@auth.post('/login')
async def log_in(user_service: user_dependency, response: Response, credentials: OAuth2PasswordRequestForm = Depends()):
    user: User = await user_service.select_one_user(username = credentials.username)
    if not bcrypt.checkpw(credentials.password.encode("utf-8"), user.password.encode()):
        raise InvalidPasswordException
    await verification_stamp(user.username, response)
    return user

@auth.post("check_token")
async def check_token(request: Request, response: Response) -> dict:
    tokens: Tokens = await get_jwt_tokens(request)
    try:
        payload: dict = await validate_access_token(tokens.access_token)
    except ExpiredAccessToken:
        tokens: Tokens = await update_tokens(request, response)
        payload: dict = await validate_access_token(tokens.access_token)
    return payload

@auth.post('/new_tokens')
async def update_tokens(request: Request, response: Response) -> Tokens:
    tokens: Tokens = await get_jwt_tokens(request)
    hashed_refresh_token = hashlib.sha256(tokens.refresh_token.encode()).hexdigest()
    data_from_redis: dict = await get_data_from_redis(hashed_refresh_token)
    if data_from_redis:
        await check_session(request, data_from_redis['fingerprint'])
        tokens: Tokens = await verification_stamp(data_from_redis['username'], response)
        return tokens
    else:
        raise InvalidRefreshToken

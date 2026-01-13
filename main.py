import uvicorn
from fastapi import FastAPI

from app.api.endpoints.user_endpoints import user_router
from app.auth.register import auth

app = FastAPI()
app.include_router(user_router)
app.include_router(auth)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

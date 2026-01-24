from datetime import datetime
from pydantic import BaseModel, Field


class User(BaseModel):
    col: None
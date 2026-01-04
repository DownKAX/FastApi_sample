from datetime import datetime, UTC, tzinfo
from fastapi import HTTPException

from pydantic import BaseModel, model_validator, Field


class ExampleModel(BaseModel):
    username: str
    register_time: datetime = Field(default_factory=lambda: datetime.now())
    item_id: int

    @model_validator(mode='after')
    def validate_username_len(self):
        if 4 > (l :=len(self.username)) or l > 20:
            raise HTTPException(detail='Username must be between 4 and 20 characters', status_code=400)
        else:
            return self

class ExampleItemModel(BaseModel):
    description: str
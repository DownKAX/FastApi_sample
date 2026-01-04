from fastapi import APIRouter, Depends, Form

from app.api.endpoints.dependencies import example_dependency
from app.api.models.example_models import ExampleModel
from app.repositories.models import ColumnValue

example_router = APIRouter(prefix='/example')

@example_router.post('/create_data')
async def create_data(example_service: example_dependency, example: ExampleModel):
    added_data = await example_service.add_one_example(example)
    return added_data

@example_router.get('/read_data')
async def read_data(example_service: example_dependency):
    data = await example_service.select_all_examples()
    return {'data': data}

@example_router.delete('/delete_data')
async def delete_data(example_service: example_dependency, id: int = Form(...)):
    deleted_data = await example_service.delete_data_by_id(id)
    return deleted_data

@example_router.patch('/update_data')
async def update_data(example_service: example_dependency, column_and_value: ColumnValue = Form(...), values: dict = Form(...)):
    updated_data = await example_service.update_one_example(column_and_value, values)
    return updated_data

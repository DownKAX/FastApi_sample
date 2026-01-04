from app.repositories.base_repository import Repository

from app.database.models import Example, ExampleItems

class ExampleRepository(Repository):
    model = Example

class ItemExampleRepository(Repository):
    model = ExampleItems
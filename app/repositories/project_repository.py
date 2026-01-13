from app.repositories.base_repository import Repository

from app.database.models import Users

class UserRepository(Repository):
    model = Users

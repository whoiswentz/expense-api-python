from app.domain.models.user import UserCreation, UserCreationResponse
from app.infrastructure.repositories.user_repository import UserRepository
from app.utils import password


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def create_user(self, user: UserCreation) -> UserCreationResponse:
        user.password = password.get_password_hash(user.password)
        new_user = await self.user_repository.create(user)
        return UserCreationResponse().from_orm(new_user)

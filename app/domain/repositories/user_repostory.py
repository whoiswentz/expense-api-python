from typing import Protocol

from app.domain.models.user import UserCreation
from app.infrastructure.entities.user import User


class UserRepositoryProtocol(Protocol):
    async def create(self, user: UserCreation) -> User: ...

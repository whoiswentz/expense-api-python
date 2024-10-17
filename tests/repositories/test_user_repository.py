import factory
import pytest
from returns.result import Success

from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreation
from tests.factories.user_factory import UserFactory


@pytest.mark.asyncio
async def test_user_creation(user_repository: UserRepository):
    user_params = UserCreation(**factory.build(dict, FACTORY_CLASS=UserFactory))

    result = await user_repository.create(user_params)

    assert isinstance(result, Success)
    assert isinstance(result.unwrap(), User)

    user = result.unwrap()
    assert user.username == user_params.username
    assert user.email == user_params.email


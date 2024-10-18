import uuid

import factory
from factory.alchemy import SQLAlchemyModelFactory

from app.infrastructure.entities.user import User


class UserFactory(SQLAlchemyModelFactory):
    id = factory.LazyFunction(lambda: uuid.uuid4())
    email = factory.Faker('email')
    username = factory.Faker('user_name')
    password = factory.Faker('password')

    class Meta:
        model = User

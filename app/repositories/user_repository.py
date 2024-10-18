from fastapi import Depends
from returns.result import Success, Failure, Result
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models.user import User
from app.schemas.user import UserCreation
from app.utils import password


class UserRepository:
    def __init__(self, db: AsyncSession = Depends(get_db)):
        self.db = db

    async def create(
            self,
            user: UserCreation,
    ) -> Result[User, Exception]:
        try:
            new_user = User(**user.model_dump())

            self.db.add(new_user)
            await self.db.commit()
            await self.db.refresh(new_user)
            return Success(new_user)
        except Exception as e:
            await self.db.rollback()
            return Failure(e)


    def hash_user_password(self, user: User) -> User:
        hashed_password = password.get_password_hash(user.password)
        user.hashed_password = hashed_password
        return user

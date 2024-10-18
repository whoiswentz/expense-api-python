from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.database import get_db

AsyncSessionDependency: Annotated[AsyncSession, Depends(get_db)] = Depends(get_db)

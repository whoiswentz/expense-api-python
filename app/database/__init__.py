from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI
from sqlalchemy.orm import Session

from app.database.database_session_manager import DatabaseSessionManager
from app.schemas import settings

sessionmanager = DatabaseSessionManager(settings.database_url, {
    "echo": settings.echo_sql
})


async def get_db() -> AsyncGenerator[Session, None]:
    async with sessionmanager.session() as session:
        yield session


@asynccontextmanager
async def lifespan(app: FastAPI) -> None:
    yield
    if sessionmanager.engine is not None:
        await sessionmanager.close()

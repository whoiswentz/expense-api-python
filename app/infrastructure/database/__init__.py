from contextlib import asynccontextmanager
from typing import AsyncGenerator, Any

from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase

from app.domain.models import get_settings
from app.infrastructure.database.database_session_manager import DatabaseSessionManager


class Base(AsyncAttrs, DeclarativeBase):
    ...


settings = get_settings()
string_database_url = str(settings.database_url)
sessionmanager = DatabaseSessionManager(string_database_url, {
    "echo": settings.echo_sql
})


async def get_db() -> AsyncGenerator[AsyncSession, Any]:
    async with sessionmanager.session() as session:
        yield session


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    yield
    if sessionmanager.engine is not None:
        await sessionmanager.close()

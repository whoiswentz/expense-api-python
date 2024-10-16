import asyncio
from contextlib import ExitStack
from typing import AsyncIterator

import pytest
import pytest_asyncio
from fastapi import FastAPI
from fastapi.testclient import TestClient
from httpx import AsyncClient

from app.database import get_db, DatabaseSessionManager
from app.main import app as actual_app
from app.schemas import get_settings
from tests.db_utils import database_exists, drop_database, create_database, override_settings, run_migrations


@pytest.fixture(autouse=True)
def app():
    with ExitStack():
        yield actual_app


@pytest.fixture
def client(app: FastAPI) -> AsyncIterator[TestClient]:
    actual_app.dependency_overrides[get_settings] = override_settings()
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="session")
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session", autouse=True)
async def sessionmanager():
    settings = override_settings()
    string_database_url = str(settings.database_url)

    if await database_exists(string_database_url):
        await drop_database(string_database_url)
    await create_database(string_database_url)

    sessionmanager = DatabaseSessionManager(string_database_url, {
        "echo": settings.echo_sql
    })

    async with sessionmanager.connect() as connection:
        await connection.run_sync(run_migrations)

    yield sessionmanager

    await sessionmanager.close()


# Each test function is a clean slate
@pytest.fixture(scope="function", autouse=True)
async def transactional_session(sessionmanager):
    async with sessionmanager.session() as session:
        try:
            await session.begin()
            yield session
        finally:
            await session.rollback()


@pytest.fixture(scope="function")
async def db_session(transactional_session):
    yield transactional_session


@pytest.fixture(scope="function", autouse=True)
async def session_override(app, db_session):
    async def get_db_session_override():
        yield db_session[0]

    app.dependency_overrides[get_db] = get_db_session_override()


@pytest_asyncio.fixture(scope="function")
async def async_test_app(app: FastAPI) -> AsyncIterator[AsyncClient]:
    async with AsyncClient(app=app) as client:
        yield client

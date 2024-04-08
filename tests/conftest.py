import asyncio
import random
from typing import Generator, Any

import httpx
import pytest

from database.connection import Settings
from main import app


@pytest.fixture(scope="session")
def event_loop() -> Generator[asyncio.AbstractEventLoop, Any, None]:
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


async def init_db():
    test_settings = Settings()
    test_settings.DATABASE_URL = "mongodb://localhost:27017/store"

    await test_settings.initialize_database()


@pytest.fixture(scope="session")
async def default_client():
    await init_db()
    async with httpx.AsyncClient(app=app, base_url="http://localhost:8082") as client:
        yield client


@pytest.fixture(scope="session")
def user_generator():
    return f"testuser{random.randint(1, 100000)}@packt.com"

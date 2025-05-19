import pytest
from httpx import AsyncClient, ASGITransport
import sys
from asyncio import new_event_loop

sys.path.append("src/")

from app import app


# @pytest.fixture(scope="session")
# def event_loop():
#     loop = new_event_loop()
#     yield loop
#     loop.close()


@pytest.fixture(scope="session")
async def async_client():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as client:
        yield client
    app.dependency_overrides.clear()

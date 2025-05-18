import pytest
from httpx import AsyncClient, ASGITransport
import sys

sys.path.append("src/")

from app import app


@pytest.fixture(scope="session")
async def async_client():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as client:
        yield client
    app.dependency_overrides.clear()

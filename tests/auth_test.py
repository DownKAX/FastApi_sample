import asyncio

import pytest
from httpx import AsyncClient, ASGITransport
import pytest_asyncio
from alembic import command
from alembic.config import Config
from main import app

@pytest_asyncio.fixture(name='client')
async def async_client():
    async with AsyncClient(transport=ASGITransport(app), base_url="http://test") as client:
        yield client

@pytest_asyncio.fixture(scope='изменить', autouse=True)
async def alembic_test_data_seeding():
    config = Config('alembic_test.ini')
    await asyncio.to_thread(command.upgrade, config, 'head')
    yield
    #await asyncio.to_thread(command.downgrade, config, 'первая версия')

class Test:
    @pytest.mark.asyncio
    async def test_success_signup(self, client):
        pass
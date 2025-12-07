from symbol import with_item
from urllib import request

import pytest
import asyncio
from httpx import AsyncClient, ASGITransport
from main import app

@pytest.mark.asyncio
async def test_read_root():
    async with AsyncClient(transport=ASGITransport(app=app),
                           base_url="http://test") as ac:
        response = await ac.get("/docs")
        assert response.status_code == 200

@pytest.mark.asyncio
async def test_get_name():
    async with AsyncClient(transport=ASGITransport(app=app),
                           base_url="http://test") as ac:
        response = await ac.get("/name")
        assert response.status_code == 200

@pytest.mark.asyncio
async def test_read_address():
    async with AsyncClient(transport=ASGITransport(app=app),
                           base_url="http://test") as ac:
        response = await ac.get("/address")
        assert response.status_code == 200

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_get_vouch_score(client: AsyncClient):
    # Verify baseline vouch score for brand new users
    response = await client.get("/api/v1/social/vouch-score")
    assert response.status_code == 200
    data = response.json()
    assert "vouch_score" in data
    assert data["vouch_score"] == 0.0


@pytest.mark.asyncio

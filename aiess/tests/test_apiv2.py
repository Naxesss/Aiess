import pytest
import asyncio
from datetime import datetime

from aiess.web import apiv2

def test_request_token():
    token = apiv2._request_token()

    assert token
    assert token.bearer
    assert token.expires_at > datetime.utcnow()
    assert token.access_token

@pytest.mark.asyncio
async def test_request_token_cached():
    apiv2.cached_token = None

    token_1 = apiv2.get_or_request_token()
    token_2 = apiv2.get_or_request_token()

    assert apiv2.cached_token == token_1
    assert token_2 == token_1

def test_request_discussions():
    response = apiv2.request_discussions()

    assert response
    assert response["discussions"]
    assert response["users"]

def test_request_discussion_posts():
    response = apiv2.request_discussions()

    assert response
    assert response["discussions"]
    assert response["users"]
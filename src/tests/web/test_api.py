from datetime import datetime

from web import api
from objects import Beatmapset, User

def test_cache():
    api.clear_response_cache()

    beatmapset_response = api.request_beatmapset(1)
    user_response = api.request_user(2)
    cached_beatmapset_response = api.request_beatmapset(1)
    cached_user_response = api.request_user(2)

    assert beatmapset_response
    assert user_response
    assert beatmapset_response == cached_beatmapset_response
    assert user_response == cached_user_response

    api.clear_response_cache()

    assert not api.requested_beatmapsets
    assert not api.requested_users

    assert api.request_beatmapset(1) == beatmapset_response
    assert api.request_user(2) == user_response

def test_cache_none():
    api.requested_beatmapsets[1] = None
    api.requested_users[2] = None

    assert api.request_beatmapset(1)
    assert api.request_user(2)

def test_timing():
    api.clear_response_cache()

    # Not cached, needs to be retrieved with API rate limit.
    time = datetime.utcnow()
    api.request_beatmapset(1)
    api.request_user(2)
    deltaTime = datetime.utcnow() - time

    assert deltaTime.total_seconds() > 1

    # Cached, can simply be read from a dictionary, should be pretty much instant.
    time = datetime.utcnow()
    api.request_beatmapset(1)
    api.request_user(2)
    deltaTime = datetime.utcnow() - time

    assert deltaTime.total_seconds() < 0.01

def test_request_beatmapset():
    beatmapset_response = api.request_beatmapset(1)

    assert beatmapset_response[0]["title"] == "DISCO PRINCE"
    assert beatmapset_response[0]["artist"] == "Kenji Ninuma"

def test_request_user():
    user_response = api.request_user(2)

    assert user_response["username"] == "peppy"
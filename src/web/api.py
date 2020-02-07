import json

from web.ratelimiter import request_with_rate_limit
from storage.settings import API_KEY, API_RATE_LIMIT

def request_api(request_type: str, query: str) -> object:
    """Requests a json object from the v1 osu!api, where the api key is supplied."""
    request = f"https://osu.ppy.sh/api/{request_type}?{query}&k={API_KEY}"
    response = request_with_rate_limit(request, API_RATE_LIMIT, "api")
    return json.loads(response.text)

def request_beatmapset(beatmapset_id: str) -> object:
    """Requests a json object of the given beatmapset id."""
    return request_api("get_beatmaps", f"s={beatmapset_id}")

def request_user(user_id: str) -> object:
    """Requests a json object of the given user id."""
    userObj = request_api("get_user", f"u={user_id}")
    if len(userObj) > 0:
        return userObj[0]
    else:
        # For when the user does not exist (e.g. restricted).
        return None
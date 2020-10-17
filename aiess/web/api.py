import json
from collections import defaultdict

from urllib.parse import quote

from aiess.web.ratelimiter import request_with_rate_limit
from aiess.settings import API_KEY, API_RATE_LIMIT

MODES = {
    "0": "osu",
    "1": "taiko",
    "2": "catch",
    "3": "mania"
}

cache = {}
def request_api(request_type: str, query: str) -> object:
    """Requests a json object from the v1 osu!api, where the api key is supplied."""
    request = f"https://osu.ppy.sh/api/{request_type}?{query}&k={API_KEY}"

    cache_line = f"/{request_type}?{query}"
    if cache_line in cache:
        return cache[cache_line]

    response = request_with_rate_limit(request, API_RATE_LIMIT, "api")
    try:
        json_response = json.loads(response.text)
        if "error" in json_response:
            # e.g. "Please provide a valid API key." if it's incorrect.
            error_str = json_response["error"]
            raise ValueError(f"The osu! api responded with an error \"{error_str}\"")

        cache[cache_line] = json_response
        return json_response
    except json.decoder.JSONDecodeError:
        # The response text is empty (e.g. "[]").
        return None

def request_beatmapset(beatmapset_id: str) -> object:
    """Requests a json object of the given beatmapset id.
    Caches any response gotten until cleared manually."""
    beatmapset_json = request_api("get_beatmaps", f"s={quote(str(beatmapset_id))}")
    return beatmapset_json

def request_user(user_id: str) -> object:
    """Requests a json object of the given user id.
    Caches any response gotten until cleared manually."""
    user_json = request_api("get_user", f"u={quote(str(user_id))}")
    if len(user_json) > 0:
        return user_json[0]
    # The user is restricted.
    return None
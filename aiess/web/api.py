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
GENRES = {
    "0": "Any",
    "1": "Unspecified",
    "2": "Video Game",
    "3": "Anime",
    "4": "Rock",
    "5": "Pop",
    "6": "Other",
    "7": "Novelty",
    # There is apparently no 8.
    "9": "Hip Hop",
    "10": "Electronic",
    "11": "Metal",  # API docs excluded 11, 12, and 14, so "Metal", "Classical", and "Jazz" are guesses.
    "12": "Classical",
    "13": "Folk",
    "14": "Jazz"
}
LANGUAGES = {
    "0": "Any",
    "1": "Other",
    "2": "English",
    "3": "Japanese",
    "4": "Chinese",
    "5": "Instrumental",
    "6": "Korean",
    "7": "French",
    "8": "German",
    "9": "Swedish",
    "10": "Spanish",
    "11": "Italian",
    "12": "Russian",
    "13": "Polish",
    "14": "Other"  # Seems 14 is also "Other".
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
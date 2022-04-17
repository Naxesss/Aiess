import json
from datetime import datetime, timedelta

from aiess.web.ratelimiter import request_with_rate_limit
from aiess.settings import API_RATE_LIMIT, APIV2_CLIENT_ID, APIV2_CLIENT_SECRET

cached_token = None

class Token():
    def __init__(self, bearer: str, expires_in: int, access_token: str):
        self.bearer       = bearer
        self.expires_at   = datetime.utcnow() + timedelta(seconds=expires_in)
        self.access_token = access_token
    
    def alive(self):
        return datetime.utcnow() < self.expires_at

def _request_token():
    response = request_with_rate_limit(
        request_url   = "https://osu.ppy.sh/oauth/token",
        rate_limit    = API_RATE_LIMIT,
        rate_limit_id = "api",
        timeout       = 10,
        method        = "POST",
        data          = {
            "client_id":     APIV2_CLIENT_ID,
            "client_secret": APIV2_CLIENT_SECRET,
            "grant_type":    "client_credentials",
            "scope":         "public"
        }
    )

    json_obj = json.loads(response.text)

    bearer       = json_obj["token_type"]
    expires_in   = json_obj["expires_in"]
    access_token = json_obj["access_token"]

    token = Token(bearer, expires_in, access_token)
    global cached_token
    cached_token = token

    return token

def get_or_request_token():
    if cached_token and cached_token.alive():
        return cached_token
    else:
        return _request_token()

def request_api(route: str, query: str=None) -> object:
    """Requests a json object from the v1 osu!api, where the api key is supplied."""
    route = route.strip("/")
    token = get_or_request_token()
    response = request_with_rate_limit(
        request_url   = f"https://osu.ppy.sh/api/v2/{route}" + (f"?{query}" if query else ""),
        rate_limit    = API_RATE_LIMIT,
        rate_limit_id = "api",
        timeout       = 10,
        headers       = { "Authorization": f"Bearer {token.access_token}" }
    )

    return json.loads(response.text)

def request_discussions(page: int=1, message_types: str=None, limit: int=None) -> object:
    """Requests a json object representing discussions on the given page, by default page 1."""
    # Response is of from:
    # {"beatmaps":[],"cursor":null,"discussions":[],"included_discussions":[],"reviews_config":{"max_blocks":100},"users":[]}
    return request_api(
        route = "/beatmapsets/discussions",
        query = f"page={page}" + (f"&message_types[]={message_types}" if message_types else "") + (f"&limit={limit}" if limit else "")
    )

def request_discussion_posts(page: int=1, limit: int=None) -> object:
    """Requests a json object representing discussion replies on the given page, by default page 1."""
    # Response is of form:
    # {"beatmaps":[],"discussions":[],"cursor":null,"posts":[],"users":[]}
    return request_api(
        route = "/beatmapsets/discussions/posts",
        query = f"page={page}" + (f"&limit={limit}" if limit else "")
    )

def request_news(cursor_id: int, cursor_published_at: str, limit: int=None) -> object:
    return request_api(
        route = "/news",
        query = f"cursor[id]={cursor_id}&cursor[published_at]={cursor_published_at}" + (f"&limit={limit}" if limit else "")
    )
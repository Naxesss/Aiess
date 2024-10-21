import sys
sys.path.append('..')

from datetime import datetime
from bs4 import BeautifulSoup
from requests import Response
from requests.exceptions import Timeout
from typing import Generator
import json

from aiess.web.ratelimiter import request_with_rate_limit
from aiess.objects import Event, Beatmapset, Discussion
from aiess.settings import PAGE_RATE_LIMIT
from aiess import event_types as types
from aiess.timestamp import to_string
from aiess.errors import DeletedContextError
from aiess.web import apiv2

from bnsite import api as bnsite_api

from scraper.parsers.beatmapset_event_parser import beatmapset_event_parser
from scraper.parsers.discussion_event_parser import discussion_event_parser
from scraper.parsers.discussion_parser import discussion_parser
from scraper.parsers import news_parser, group_parser

def request_page(url: str) -> Response:
    """Requests a response object using the page rate limit.
    If cloudflare IUAM (https://blog.cloudflare.com/tag/iuam/) is active we simply wait until it's over."""
    return request_with_rate_limit(url, PAGE_RATE_LIMIT, "page", timeout=60)  # `timeout` is in seconds.

def soupify(html: str) -> BeautifulSoup:
    """Returns the given html as a BeautifulSoup object."""
    return BeautifulSoup(html, features="html.parser")

def request_soup(url: str) -> BeautifulSoup:
    """Requests the page from the url as a BeautifulSoup object."""
    text = request_page(url).text
    return soupify(text)



def request_beatmapset_events(page: int=1, limit: int=50) -> BeautifulSoup:
    """Requests the beatmapset events page as a BeautifulSoup object. Only certain events are queried."""
    # This way if events are added we ignore them until we've properly supported them.
    event_types = [
        types.NOMINATE, types.QUALIFY, types.RANK, types.LOVE, types.UNLOVE, types.RESET, types.DISQUALIFY,  # Beatmap Status Events
        types.KUDOSU_GAIN, types.KUDOSU_LOSS, types.KUDOSU_ALLOW, types.KUDOSU_DENY,  # Kudosu Events
        types.RESOLVE, types.REOPEN,  # Discussion Status Events
        types.GENRE_EDIT, types.LANGUAGE_EDIT,  # Genre/Language Events
        types.DISCUSSION_DELETE, types.DISCUSSION_RESTORE, types.REPLY_DELETE, types.REPLY_RESTORE  # Delete/Restore Events
    ]

    type_query = ""
    for _type in map(lambda _type: _type.replace("-", "_"), event_types):
        type_query += f"&types[]={_type}"
    
    return request_soup(f"https://osu.ppy.sh/beatmapsets/events?page={page}&limit={limit}{type_query}")

def request_beatmapset_json(url: str) -> object:
    """Requests the page from the url as a json object."""
    beatmapset_soup = request_soup(url)
    beatmapset_json_tag = beatmapset_soup.find("script", {"id": "json-beatmapset"})
    beatmapset_json = beatmapset_json_tag.text
    return json.loads(beatmapset_json)

def request_discussion_events(page: int=1, limit: int=50) -> BeautifulSoup:
    """Requests the discussion events page as a BeautifulSoup object."""
    event_types = [types.SUGGESTION, types.PROBLEM, types.NOTE, types.PRAISE, types.HYPE]

    type_query = ""
    for _type in map(lambda _type: _type.replace("-", "_"), event_types):
        type_query += f"&message_types[]={_type}"
    
    json_response = apiv2.request_discussions(page=page, message_types=type_query, limit=limit)
    return (json_response["discussions"], json_response["users"])

def request_reply_events(page: int=1, limit: int=50) -> BeautifulSoup:
    """Requests the discussion reply events page as a BeautifulSoup object."""
    json_response = apiv2.request_discussion_posts(page=page, limit=limit)
    return (json_response["posts"], json_response["users"], json_response["discussions"])

def request_news(_from: datetime, limit: int=20) -> BeautifulSoup:
    """Requests the news home page as a BeautifulSoup object with the newest post being from the given datetime."""
    json_response = apiv2.request_news(cursor_id=0, cursor_published_at=to_string(_from), limit=limit)
    return json_response["news_posts"]

def request_group_page(group_id: int) -> BeautifulSoup:
    """Requests the group page of the given group id as a BeautifulSoup object."""
    return request_soup(f"https://osu.ppy.sh/groups/{group_id}")



def get_beatmapset_events(page: int=1, limit: int=50) -> Generator[Event, None, None]:
    """Returns a generator of Event objects from the beatmapset events page. Newer events are yielded first."""
    return beatmapset_event_parser.parse(request_beatmapset_events(page, limit))

def get_discussion_events(page: int=1, limit: int=50) -> Generator[Event, None, None]:
    """Returns a generator of Event objects from the discussion events page. Newer events are yielded first."""
    discussion_jsons, user_jsons = request_discussion_events(page=page, limit=limit)
    return discussion_event_parser.parse(discussion_jsons, user_jsons)

def get_reply_events(page: int=1, limit: int=50) -> Generator[Event, None, None]:
    """Returns a generator of Event objects from the discussion reply events page. Newer events are yielded first."""
    post_jsons, user_jsons, discussion_jsons = request_reply_events(page=page, limit=limit)
    return discussion_event_parser.parse(post_jsons, user_jsons, discussion_jsons_for_replies=discussion_jsons)

def get_news_events(_from: datetime, limit: int=20) -> Generator[Event, None, None]:
    """Returns a generator of Event objects from the news home page. Newer events are yielded first."""
    return news_parser.parse_json(request_news(_from, limit))

def get_group_events(_from: datetime) -> Generator[Event, None, None]:
    """Returns a generator of group addition and removal Event objects from all group pages."""
    for group_id in [4, 7, 11, 16, 22, 28, 31, 32, 48]:
        yield from group_parser.parse(group_id=group_id, group_page=request_group_page(group_id), last_checked_at=_from)



def request_discussions_json(beatmapset_id: int) -> object:
    """Requests the beatmapset discussion page as a json object, if it exists, otherwise None.
    Older beatmapsets have no discussions, for example, so they will return None."""
    try:
        return request_beatmapset_json(f"https://osu.ppy.sh/beatmapsets/{beatmapset_id}/discussion")
    except json.decoder.JSONDecodeError:
        return None

def get_map_page_discussions(beatmapset: Beatmapset, discussions_json: object=None) -> Generator[Discussion, None, None]:
    """Returns a generator of discussion objects from the beatmapset discussion page json. If not supplied it is scraped."""
    discussions_json = request_discussions_json(beatmapset.id) if discussions_json is None else discussions_json
    return discussion_parser.parse(discussions_json, beatmapset)

def get_map_page_event_jsons(beatmapset: Beatmapset, discussions_json: object=None) -> Generator[object, None, None]:
    """Returns a generator of event json objects from the beatmapset discussion page json. If not supplied it is scraped."""
    discussions_json = request_discussions_json(beatmapset.id) if discussions_json is None else discussions_json
    return discussions_json["events"]

def get_map_page_discussion_jsons(beatmapset: Beatmapset, discussions_json: object=None) -> Generator[object, None, None]:
    """Returns a generator of event json objects from the beatmapset discussion page json. If not supplied it is scraped."""
    discussions_json = request_discussions_json(beatmapset.id) if discussions_json is None else discussions_json
    return discussions_json["discussions"]
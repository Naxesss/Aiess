import sys
sys.path.append('..')

from datetime import datetime
from bs4 import BeautifulSoup
from requests import Response
from typing import Generator
import json

from aiess.web.ratelimiter import request_with_rate_limit
from aiess.objects import Event, Beatmapset, Discussion
from aiess.settings import PAGE_RATE_LIMIT
from aiess import event_types as types
from aiess.timestamp import to_string

from scraper.parsers.beatmapset_event_parser import beatmapset_event_parser
from scraper.parsers.discussion_event_parser import discussion_event_parser
from scraper.parsers.discussion_parser import discussion_parser
from scraper.parsers import news_parser, group_parser

def request_page(url: str) -> Response:
    """Requests a response object using the page rate limit.
    If cloudflare IUAM (https://blog.cloudflare.com/tag/iuam/) is active we simply wait until it's over."""
    return request_with_rate_limit(url, PAGE_RATE_LIMIT, "page")

def request_json(url: str) -> object:
    """Requests the page from the url as a json object."""
    return json.loads(request_page(url).text)

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
        types.NOMINATE, types.QUALIFY, types.RANK, types.LOVE, types.RESET, types.DISQUALIFY,  # Beatmap Status Events
        types.KUDOSU_GAIN, types.KUDOSU_LOSS, types.KUDOSU_ALLOW, types.KUDOSU_DENY,  # Kudosu Events
        types.RESOLVE, types.REOPEN,  # Discussion Status Events
        types.DISCUSSION_DELETE, types.DISCUSSION_RESTORE, types.REPLY_DELETE, types.REPLY_RESTORE  # Delete/Restore Events
    ]

    type_query = ""
    for _type in map(lambda _type: _type.replace("-", "_"), event_types):
        type_query += f"&types[]={_type}"
    
    return request_soup(f"https://osu.ppy.sh/beatmapsets/events?page={page}&limit={limit}{type_query}")

def request_discussion_events(page: int=1, limit: int=50) -> BeautifulSoup:
    """Requests the discussion events page as a BeautifulSoup object."""
    event_types = [types.SUGGESTION, types.PROBLEM, types.NOTE, types.PRAISE, types.HYPE]

    type_query = ""
    for _type in map(lambda _type: _type.replace("-", "_"), event_types):
        type_query += f"&message_types[]={_type}"
    
    return request_soup(f"https://osu.ppy.sh/beatmapsets/beatmap-discussions?page={page}&limit={limit}{type_query}")

def request_reply_events(page: int=1, limit: int=50) -> BeautifulSoup:
    """Requests the discussion reply events page as a BeautifulSoup object."""
    return request_soup(f"https://osu.ppy.sh/beatmapsets/beatmap-discussion-posts?page={page}&limit={limit}")

def request_news(_from: datetime, limit: int=20) -> BeautifulSoup:
    """Requests the news home page as a BeautifulSoup object with the newest post being from the given datetime."""
    # The `id` attribute doesn't seem to matter.
    return request_soup(f"https://osu.ppy.sh/home/news?cursor[id]=0&cursor[published_at]={to_string(_from)}&limit={limit}")

def request_group_page(group_id: int) -> BeautifulSoup:
    """Requests the group page of the given group id as a BeautifulSoup object."""
    return request_soup(f"https://osu.ppy.sh/groups/{group_id}")



def get_beatmapset_events(page: int=1, limit: int=50) -> Generator[Event, None, None]:
    """Returns a generator of Event objects from the beatmapset events page. Newer events are yielded first."""
    return beatmapset_event_parser.parse(request_beatmapset_events(page, limit))

def get_discussion_events(page: int=1, limit: int=50) -> Generator[Event, None, None]:
    """Returns a generator of Event objects from the discussion events page. Newer events are yielded first."""
    return discussion_event_parser.parse(request_discussion_events(page, limit))

def get_reply_events(page: int=1, limit: int=50) -> Generator[Event, None, None]:
    """Returns a generator of Event objects from the discussion reply events page. Newer events are yielded first."""
    return discussion_event_parser.parse(request_reply_events(page, limit))

def get_news_events(_from: datetime, limit: int=20) -> Generator[Event, None, None]:
    """Returns a generator of Event objects from the news home page. Newer events are yielded first."""
    return news_parser.parse(request_news(_from, limit))

def get_group_events(_from: datetime) -> Generator[Event, None, None]:
    """Returns a generator of group addition and removal Event objects from all group pages."""
    for group_id in [4, 7, 11, 16, 22, 28, 32]:
        yield from group_parser.parse(group_id=group_id, group_page=request_group_page(group_id), last_checked_at=_from)



def request_discussions_json(beatmapset: Beatmapset) -> object:
    """Requests the beatmapset discussion page as a json object, if it exists, otherwise None.
    Older beatmapsets have no discussions, for example, so they will return None."""
    try:
        return request_json(f"https://osu.ppy.sh/beatmapsets/{beatmapset.id}/discussion?format=json")
    except json.decoder.JSONDecodeError:
        return None

def get_map_page_discussions(beatmapset: Beatmapset, discussions_json: object=None) -> Generator[Discussion, None, None]:
    """Returns a generator of discussion objects from the beatmapset discussion page json. If not supplied it is scraped."""
    discussions_json = request_discussions_json(beatmapset) if discussions_json is None else discussions_json
    return discussion_parser.parse(discussions_json, beatmapset)

def get_map_page_event_jsons(beatmapset: Beatmapset, discussions_json: object=None) -> Generator[object, None, None]:
    """Returns a generator of event json objects from the beatmapset discussion page json. If not supplied it is scraped."""
    discussions_json = request_discussions_json(beatmapset) if discussions_json is None else discussions_json
    return discussions_json["beatmapset"]["events"]

def get_map_page_discussion_jsons(beatmapset: Beatmapset, discussions_json: object=None) -> Generator[object, None, None]:
    """Returns a generator of event json objects from the beatmapset discussion page json. If not supplied it is scraped."""
    discussions_json = request_discussions_json(beatmapset) if discussions_json is None else discussions_json
    return discussions_json["beatmapset"]["discussions"]
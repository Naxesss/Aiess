from bs4 import BeautifulSoup
from requests import Response
from typing import Generator
import json

from web.ratelimiter import request_with_rate_limit
from objects import Event, Beatmapset, Discussion
from parsers.beatmapset_event_parser import beatmapset_event_parser
from parsers.discussion_event_parser import discussion_event_parser
from parsers.discussion_parser import discussion_parser
from storage.settings import PAGE_RATE_LIMIT

def request_page(url: str) -> Response:
    """Requests a response object using the page rate limit."""
    return request_with_rate_limit(url, PAGE_RATE_LIMIT, "page")

def request_json(url: str) -> object:
    """Requests the page from the url as a json object."""
    return json.loads(request_page(url).text)

def soupify(html: str) -> BeautifulSoup:
    """Returns the given html as a BeautifulSoup object."""
    return BeautifulSoup(html, "html.parser")

def request_soup(url: str) -> BeautifulSoup:
    """Requests the page from the url as a BeautifulSoup object."""
    text = request_page(url).text
    return soupify(text)



def request_beatmapset_events(page: int=1) -> BeautifulSoup:
    """Requests the beatmapset events page as a BeautifulSoup object. Only certain events are queried."""
    # This way if events are added we ignore them until we've properly supported them.
    types = [
        "nominate", "qualify", "rank", "love", "nomination_reset", "disqualify", "approve",  # Beatmap Status Events
        "kudosu_gain", "kudosu_lost", "kudosu_allow", "kudosu_deny",  # Kudosu Events
        "issue_resolve", "issue_reopen",  # Discussion Status Events
        "discussion_delete", "discussion_restore", "discussion_post_delete", "discussion_post_restore"  # Delete/Restore Events
    ]

    type_query = ""
    for _type in types:
        type_query += f"&types[]={_type}"
    
    return request_soup(f"https://osu.ppy.sh/beatmapsets/events?page={page}&limit=50{type_query}")

def request_discussion_events(page: int=1) -> BeautifulSoup:
    """Requests the discussion events page as a BeautifulSoup object."""
    return request_soup(f"https://osu.ppy.sh/beatmapsets/beatmap-discussions?page={page}&limit=50")




def get_beatmapset_events(page: int=1) -> Generator[Event, None, None]:
    """Returns a generator of Event objects from the beatmapset events page. Newer events are yielded first."""
    return beatmapset_event_parser.parse(request_beatmapset_events(page))

def get_discussion_events(page: int=1) -> Generator[Event, None, None]:
    """Returns a generator of Event objects from the discussion events page. Newer events are yielded first."""
    return discussion_event_parser.parse(request_discussion_events(page))




def request_discussions_json(beatmapset: Beatmapset) -> object:
    """Requests the beatmapset discussion page as a json object, if it exists, otherwise None.
    Older beatmapsets have no discussions, for example, so they will return None."""
    try:
        return request_json(f"https://osu.ppy.sh/beatmapsets/{beatmapset.id}/discussion?format=json")
    except json.decoder.JSONDecodeError:
        return None

def get_map_page_discussions(beatmapset: Beatmapset, discussions_json: object=None) -> Generator[Discussion, None, None]:
    """Returns a generator of discussion objects from the beatmapset discussion page json. If not supplied it is scraped."""
    discussions_json = request_discussions_json(beatmapset) if discussions_json == None else discussions_json
    return discussion_parser.parse(discussions_json, beatmapset)

def get_map_page_event_jsons(beatmapset: Beatmapset, discussions_json: object=None) -> Generator[object, None, None]:
    """Returns a generator of event json objects from the beatmapset discussion page json. If not supplied it is scraped."""
    discussions_json = request_discussions_json(beatmapset) if discussions_json == None else discussions_json
    return discussions_json["beatmapset"]["events"]
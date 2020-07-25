import sys
sys.path.append('..')

from typing import Generator, Iterator
from bs4 import BeautifulSoup
from bs4.element import Tag
import json

from aiess.objects import Event, User, NewsPost
from aiess.timestamp import from_string

def parse(events: BeautifulSoup) -> Generator[Event, None, None]:
    """Returns a generator of news events from the given /news BeautifulSoup response, parsed top-down."""
    json_index = events.find("script", {"id": "json-index"})
    if not json_index:
        raise ValueError("No news json could be found.")

    post_jsons = json.loads(json_index.string)["news_posts"]
    return parse_post_jsons(post_jsons)

def parse_post_jsons(post_jsons: Iterator[object]) -> Generator[Event, None, None]:
    """Returns a generator of news events representing the given news post json objects."""
    for post_json in post_jsons:
        yield parse_post_json(post_json)

def parse_post_json(post_json: object) -> Event:
    """Returns an event representing the given news post json object
    (a single news post instance, for multiple see `parse_post_jsons`)."""
    author = User(name=post_json["author"].strip())
    return Event(
        _type      = "news",
        time       = from_string(post_json["published_at"]),
        newspost   = NewsPost(
            _id       = post_json["id"],
            title     = post_json["title"],
            preview   = post_json["preview"],
            author    = author,
            slug      = post_json["slug"],
            image_url = complete_image_url(post_json["first_image"])
        ),
        user       = author,  # Authors seem to have a space prefixed.
        content    = post_json["preview"]
    )

def complete_image_url(url: str) -> str:
    """Returns the given url, with https://osu.ppy.sh/ prepended, if it does not contain
    that part already. Some image urls in newsposts include the domain, while others do not
    (e.g "/help/wiki/shared/news/banners/community-mentorship-program.jpg")."""
    if url.startswith("https://"):
        return url
    return f"https://osu.ppy.sh{url}"
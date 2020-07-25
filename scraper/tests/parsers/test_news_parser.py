import sys
sys.path.append('..')

from aiess import Event, User, NewsPost
from aiess.timestamp import from_string

from scraper.tests.mocks.events import news as mock_news_events
from scraper.parsers import news_parser

def test_parse():
    events = []
    for event in news_parser.parse(mock_news_events.soup):
        events.append(event)

    assert len(events) == 6
    assert events[0] == Event(
        _type      = "news",
        time       = from_string("2020-07-22T21:00:00+00:00"),
        newspost   = NewsPost(
            _id       = 812,
            title     = "Aspire V - Finals Stage Voting",
            preview   = "You've chosen your favourite beatmaps from the Aspire V categories, now it's time to pick the best of the best!",
            author    = User(_id=2202163, name="-Mo-"),
            slug      = "2020-07-21-aspire-v-finals-stage-voting",
            image_url = "https://assets.ppy.sh/contests/94/header.jpg"
        ),
        user       = User(_id=2202163, name="-Mo-"),
        content    = "You've chosen your favourite beatmaps from the Aspire V categories, now it's time to pick the best of the best!"
    )
    assert events[1] == Event(
        _type      = "news",
        time       = from_string("2020-07-22T08:00:00+00:00"),
        newspost   = NewsPost(
            _id       = 811,
            title     = "New Featured Artist: Receptor",
            preview   = "We're excited to welcome Receptor aboard as our latest Featured Artist!",
            author    = User(_id=102335, name="Ephemeral"),
            slug      = "2020-07-22-new-featured-artist-receptor",
            image_url = "https://assets.ppy.sh/artists/91/header.jpg"
        ),
        user       = User(_id=102335, name="Ephemeral"),
        content    = "We're excited to welcome Receptor aboard as our latest Featured Artist!"
    )

def test_complete_image_url():
    assert news_parser.complete_image_url("/hello") == "https://osu.ppy.sh/hello"

def test_complete_image_url_complete():
    assert news_parser.complete_image_url("https://assets.ppy.sh/hello") == "https://assets.ppy.sh/hello"
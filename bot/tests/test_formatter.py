import sys
sys.path.append('..')

import pytest
import mock
from discord import Embed
from datetime import timedelta
from datetime import datetime

from aiess import Event, User, Beatmapset, Discussion, NewsPost
from aiess.timestamp import from_string
from aiess.database import SCRAPER_TEST_DB_NAME

from bot import database as db_module
from bot.database import Database
from bot.formatter import format_link
from bot.formatter import format_embed
from bot.formatter import format_field_name
from bot.formatter import format_field_value
from bot.formatter import format_footer_text
from bot.formatter import truncate
from bot.formatter import format_preview
from bot.formatter import format_footer_icon_url
from bot.formatter import format_thumbnail_url
from bot.formatter import format_image_url
from bot.formatter import format_context_field_name
from bot.formatter import format_context_field_value
from bot.formatter import format_history
from bot.formatter import TimeUnit
from bot.formatter import format_time
from bot.formatter import format_timeago

@pytest.fixture
def suggestion_event():
    beatmapset = Beatmapset(3, "artist", "title", User(2, "sometwo"), ["osu"])
    user = User(1, "someone")
    discussion = Discussion(5, beatmapset, user, content="hi")
    event = Event("suggestion", from_string("2020-04-11 20:00:00"), beatmapset, discussion, user, content="hi")

    return event

@pytest.fixture
def qualify_event():
    beatmapset = Beatmapset(3, "artist_with*strange~symbols`", "title", User(2, "_sometwo_"), ["osu"])
    event = Event("qualify", from_string("2020-04-11 20:00:00"), beatmapset)

    return event

@pytest.fixture
def kudosu_gain_event():
    mapper = User(2, "sometwo")
    beatmapset = Beatmapset(3, "artist", "title", mapper, ["osu"])
    user = User(1, "_someone_")
    discussion = Discussion(5, beatmapset, user, content="hi*")
    event = Event("kudosu_gain", from_string("2020-04-11 20:00:00"), beatmapset, discussion, mapper)

    return event

@pytest.fixture
def newspost_event():
    author = User(2, "sometwo")
    preview = "quite long preview" * 10
    newspost = NewsPost(_id=3, title="title", preview=preview, author=author, slug="slug", image_url="https://osu.ppy.sh/image.jpg")
    event = Event("news", from_string("2020-07-24 20:00:00"), newspost=newspost, user=author, content=preview)

    return event

@pytest.fixture
def test_database():
    database = Database(SCRAPER_TEST_DB_NAME)
    database.clear_table_data("events")
    db_module.clear_cache(SCRAPER_TEST_DB_NAME)
    return database

def test_format_link_discussion(suggestion_event):
    assert format_link(suggestion_event) == "https://osu.ppy.sh/beatmapsets/3/discussion#/5"

def test_format_link_no_discussion(qualify_event):
    assert format_link(qualify_event) == "https://osu.ppy.sh/beatmapsets/3"

def test_format_link_no_beatmapset():
    event = Event("test", from_string("2020-04-11 20:00:00"))

    with pytest.raises(ValueError) as err:
        format_link(event)
    
    assert "missing a beatmapset" in str(err)

def test_format_link_newspost(newspost_event):
    assert format_link(newspost_event) == "https://osu.ppy.sh/home/news/slug"



@pytest.mark.asyncio
async def test_format_embed(suggestion_event):
    embed: Embed = await format_embed(suggestion_event)
    
    assert embed.fields[0].name.startswith(":yellow_circle:\u2000Suggestion (**")
    assert embed.fields[0].name.endswith("** ago)")
    assert (
        embed.fields[0].value ==
        "[**artist - title**](https://osu.ppy.sh/beatmapsets/3)\nMapped by [sometwo](https://osu.ppy.sh/users/2) [**osu**]"
    )
    assert embed.footer.text == "someone \"hi\""
    assert embed.footer.icon_url == "https://a.ppy.sh/1"
    assert embed.colour.to_rgb() == (65, 65, 65)
    assert embed.thumbnail.url == "https://b.ppy.sh/thumb/3l.jpg"

@pytest.mark.asyncio
async def test_format_embed_newspost(newspost_event):
    embed: Embed = await format_embed(newspost_event)
    
    assert embed.fields[0].name.startswith("title (**")
    assert embed.fields[0].name.endswith("** ago)")
    assert embed.fields[0].value == "quite long preview" * 10
    assert embed.footer.text == "sometwo"
    assert embed.footer.icon_url == "https://a.ppy.sh/2"
    assert embed.colour.to_rgb() == (255, 160, 200)
    assert embed.image.url == "https://osu.ppy.sh/image.jpg"

@pytest.mark.asyncio
async def test_format_embed_context(kudosu_gain_event):
    embed: Embed = await format_embed(kudosu_gain_event)
    
    assert len(embed.fields) == 2
    assert embed.fields[1].name == format_context_field_name(kudosu_gain_event)
    assert embed.fields[1].value == format_context_field_value(kudosu_gain_event)

def test_format_field_name(suggestion_event):
    assert format_field_name(suggestion_event).startswith(":yellow_circle:\u2000Suggestion (**")
    assert format_field_name(suggestion_event).endswith("** ago)")

def test_format_field_name_qualify(qualify_event):
    assert format_field_name(qualify_event).startswith(":heart:\u2000Qualified (**")
    assert format_field_name(qualify_event).endswith("** ago)")

def test_format_field_name_newspost(newspost_event):
    assert format_field_name(newspost_event).startswith("title (**")
    assert format_field_name(newspost_event).endswith("** ago)")

@pytest.mark.asyncio
async def test_format_field_value(suggestion_event):
    assert (
        await format_field_value(suggestion_event) ==
        "[**artist - title**](https://osu.ppy.sh/beatmapsets/3)\nMapped by [sometwo](https://osu.ppy.sh/users/2) [**osu**]"
    )

@pytest.mark.asyncio
async def test_format_field_value_newspost(newspost_event):
    assert await format_field_value(newspost_event) == "quite long preview" * 10

@pytest.mark.asyncio
async def test_format_field_value_markdown(qualify_event):
    assert (
        await format_field_value(qualify_event) ==
        "[**artist\\_with\\*strange\\~symbols\\` - title**](https://osu.ppy.sh/beatmapsets/3)\nMapped by [\\_sometwo\\_](https://osu.ppy.sh/users/2) [**osu**]"
    )

def test_format_footer_text(suggestion_event):
    assert format_footer_text(suggestion_event) == "someone \"hi\""

def test_format_footer_text_newspost(newspost_event):
    # Newsposts already include their preview in the post itself, so we skip this.
    assert format_footer_text(newspost_event) == "sometwo"

def test_format_footer_text_no_user(qualify_event):
    assert format_footer_text(qualify_event) == Embed.Empty

def test_format_footer_text_preview(suggestion_event):
    suggestion_event.content = "04:25:218 (3,4) - the guitar is really strong here so mapping to the red beats only feels unfitting"
    assert format_footer_text(suggestion_event) == f"{suggestion_event.user} {format_preview(suggestion_event.content)}"

def test_format_footer_text_no_comment(suggestion_event):
    suggestion_event.content = ""
    assert format_footer_text(suggestion_event) == "someone"

def test_format_footer_text_kudosu_given(kudosu_gain_event):
    assert format_footer_text(kudosu_gain_event) == "sometwo"

def test_format_footer_text_kudosu_denied(kudosu_gain_event):
    kudosu_gain_event.type = "kudosu-deny"
    kudosu_gain_event.user = None
    assert format_footer_text(kudosu_gain_event) == Embed.Empty

def test_format_preview_empty_no_surrounding_quotes():
    assert format_preview("") == ""

def test_truncate():
    text = "04:25:218 (3,4) - the guitar is really strong here so mapping to the red beats only feels unfitting"
    assert truncate(text, length=75) == "04:25:218 (3,4) - the guitar is really strong here so mappin... [truncated]"
    assert truncate(text, length=200) == text

def test_format_preview_long():
    text = "04:25:218 (3,4) - the guitar is really strong here so mapping to the red beats only feels unfitting"
    assert format_preview(text) == "\"04:25:218 (3,4) - the guitar is really strong here so map...\""
    assert format_preview(text, length=75) == "\"04:25:218 (3,4) - the guitar is really strong here so mapping to the red...\""

def test_format_preview_newline():
    text = "04:25:218 (3,4) - the guitar is really strong here so\nmapping to the red beats only feels unfitting"
    assert format_preview(text) == "\"04:25:218 (3,4) - the guitar is really strong here so\""
    assert format_preview(text, split_newline=False) == "\"04:25:218 (3,4) - the guitar is really strong here so\nmap...\""

def test_format_footer_icon_url(suggestion_event):
    assert format_footer_icon_url(suggestion_event) == "https://a.ppy.sh/1"

def test_format_footer_icon_url_no_user(qualify_event):
    assert format_footer_icon_url(qualify_event) == Embed.Empty

def test_format_footer_icon_url_non_existing_user(suggestion_event):
    suggestion_event.user = User(_id=None, name="a")
    assert format_footer_icon_url(suggestion_event) == "https://osu.ppy.sh/images/layout/avatar-guest.png"

def test_format_footer_icon_url_news_freetext(newspost_event):
    newspost_event.user = None
    newspost_event.newspost.author = User(_id=None, name="-Mo- and Noffy")
    assert format_footer_icon_url(newspost_event) == "https://osu.ppy.sh/images/layout/avatar-guest.png"

def test_format_thumbnail_url(suggestion_event):
    assert format_thumbnail_url(suggestion_event) == "https://b.ppy.sh/thumb/3l.jpg"

def test_format_thumbnail_url_non_applicable(newspost_event):
    assert format_thumbnail_url(newspost_event) == Embed.Empty

def test_format_image_url(newspost_event):
    assert format_image_url(newspost_event) == "https://osu.ppy.sh/image.jpg"

def test_format_image_url_non_applicable(suggestion_event):
    assert format_image_url(suggestion_event) == Embed.Empty

def test_context_field_name(kudosu_gain_event):
    assert format_context_field_name(kudosu_gain_event) == "\\_someone\\_"

def test_context_field_value(kudosu_gain_event):
    assert format_context_field_value(kudosu_gain_event) == "\"hi\\*\""

def test_context_field_value_truncate(kudosu_gain_event):
    kudosu_gain_event.discussion.content = "a very long piece of text " * 10
    assert format_context_field_value(kudosu_gain_event) == "\"a very long piece of text a very long piece of text a ver...\""

@pytest.mark.asyncio
async def test_history(test_database):
    beatmapset = Beatmapset(3, "artist", "title", User(4, "mapper"), ["osu"])
    nom_event = Event("nominate", from_string("2020-01-01 00:00:00"), beatmapset, user=User(1, "someone"))
    qual_event = Event("qualify", from_string("2020-01-01 05:00:00"), beatmapset, user=User(2, "sometwo"))

    test_database.insert_event(nom_event)
    test_database.insert_event(qual_event)

    history = await format_history(beatmapset, database=test_database)
    assert history == "\n:thought_balloon: [someone](https://osu.ppy.sh/users/1)\u2000:heart: [sometwo](https://osu.ppy.sh/users/2)"

@pytest.mark.asyncio
async def test_history_filtering(test_database):
    beatmapset = Beatmapset(3, "artist", "title", User(4, "mapper"), ["osu"])
    nom_event = Event("nominate", from_string("2020-01-01 00:00:00"), beatmapset, user=User(1, "someone"))
    qual_event = Event("qualify", from_string("2020-01-01 05:00:00"), beatmapset, user=User(2, "sometwo"))
    suggestion_event = Event("suggestion", from_string("2020-01-01 01:00:00"), beatmapset, user=User(3, "somethree"))

    test_database.insert_event(nom_event)
    test_database.insert_event(qual_event)
    test_database.insert_event(suggestion_event)

    # The suggestion event should not appear in the history.
    history = await format_history(beatmapset, database=test_database)
    assert history == "\n:thought_balloon: [someone](https://osu.ppy.sh/users/1)\u2000:heart: [sometwo](https://osu.ppy.sh/users/2)"

@pytest.mark.asyncio
async def test_history_truncated(test_database):
    beatmapset = Beatmapset(3, "artist", "title", User(4, "mapper"), ["osu"])
    nom_event = Event("nominate", from_string("2020-01-01 00:00:00"), beatmapset, user=User(1, "someone"))
    qual_event = Event("qualify", from_string("2020-01-01 05:00:00"), beatmapset, user=User(2, "sometwo"))

    for _ in range(20):
        test_database.insert_event(nom_event)
        nom_event.time += timedelta(seconds=15)
    test_database.insert_event(qual_event)

    history = await format_history(beatmapset, length_limit=200, database=test_database)
    expected_history = "\n..."
    for _ in range(10):
        expected_history += ":thought_balloon: "
    assert history == expected_history + ":heart:"
    assert len(history) <= 200

def test_time_unit_comparison():
    assert TimeUnit.MILLISECONDS < TimeUnit.SECONDS

def test_time_unit_comparison_inferred():
    assert TimeUnit.HOURS >= TimeUnit.HOURS
    assert TimeUnit.HOURS >= TimeUnit.MINUTES

def test_time_unit_comparison_not_implemented():
    with pytest.raises(TypeError) as err:
        TimeUnit.HOURS >= 0
    
    assert "'>=' not supported between instances of 'TimeUnit' and 'int'" in str(err)

def test_format_time():
    assert format_time(timedelta(minutes=2, seconds=36)) == "2 min 36 s"

def test_format_time_max_units():
    assert format_time(timedelta(hours=3, minutes=2, seconds=36), max_units=1) == "3 h"
    assert format_time(timedelta(hours=3, minutes=2, seconds=36), max_units=2) == "3 h 2 min"
    assert format_time(timedelta(hours=3, minutes=2, seconds=36), max_units=3) == "3 h 2 min 36 s"
    assert format_time(timedelta(hours=3, minutes=2, seconds=36), max_units=None) == "3 h 2 min 36 s"

def test_format_time_min_unit():
    assert format_time(timedelta(hours=3, minutes=2, seconds=36), min_unit=TimeUnit.DAYS, max_units=None) == "< 1 d"
    assert format_time(timedelta(hours=3, minutes=2, seconds=36), min_unit=TimeUnit.HOURS, max_units=None) == "3 h"
    assert format_time(timedelta(hours=3, minutes=2, seconds=36), min_unit=TimeUnit.MINUTES, max_units=None) == "3 h 2 min"
    assert format_time(timedelta(hours=3, minutes=2, seconds=36), min_unit=TimeUnit.SECONDS, max_units=None) == "3 h 2 min 36 s"
    assert format_time(timedelta(hours=3, minutes=2, seconds=36), min_unit=None, max_units=None) == "3 h 2 min 36 s"

def test_format_time_numeric_deltatime():
    assert format_time(10956, min_unit=None, max_units=None) == "3 h 2 min 36 s"

def test_format_timeago():
    with mock.patch("bot.formatter.datetime") as mock_datetime:
        # Mock `datetime.utcnow`, but retain the original datetime class functionality through the `side_effect` attribute.
        mock_datetime.utcnow.return_value = from_string("2020-01-01 05:30:06")
        mock_datetime.side_effect = datetime

        assert format_timeago(from_string("2020-01-01 00:00:00")) == "**5 hours** ago"

def test_format_timeago_not_bold():
    with mock.patch("bot.formatter.datetime") as mock_datetime:
        mock_datetime.utcnow.return_value = from_string("2020-01-01 05:30:06")
        mock_datetime.side_effect = datetime

        assert format_timeago(from_string("2020-01-01 00:00:00"), bold=False) == "5 hours ago"
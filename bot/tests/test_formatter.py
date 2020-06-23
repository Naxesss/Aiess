import sys
sys.path.append('..')

import pytest
from discord import Embed
from datetime import timedelta

from aiess import Event, User, Beatmapset, Discussion
from aiess.timestamp import from_string
from aiess.database import SCRAPER_TEST_DB_NAME

from bot import database as db_module
from bot.database import Database
from bot.formatter import format_link
from bot.formatter import format_embed
from bot.formatter import format_field_name
from bot.formatter import format_field_value
from bot.formatter import format_footer_text
from bot.formatter import format_preview
from bot.formatter import format_footer_icon_url
from bot.formatter import format_thumbnail_url
from bot.formatter import format_context_field_name
from bot.formatter import format_context_field_value
from bot.formatter import format_history
from bot.formatter import format_recent_praise
from bot.formatter import TimeUnit
from bot.formatter import format_time

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
    event = Event("kudosu-gain", from_string("2020-04-11 20:00:00"), beatmapset, discussion, mapper)

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



def test_format_embed(suggestion_event):
    embed: Embed = format_embed(suggestion_event)
    
    assert embed.fields[0].name == ":yellow_circle: Suggestion"
    assert (
        embed.fields[0].value ==
        "[**artist - title**](https://osu.ppy.sh/beatmapsets/3)\nMapped by [sometwo](https://osu.ppy.sh/users/2) [**osu**]"
    )
    assert embed.footer.text == "someone \"hi\""
    assert embed.footer.icon_url == "https://a.ppy.sh/1"
    assert embed.colour.to_rgb() == (65, 65, 65)
    assert embed.thumbnail.url == "https://b.ppy.sh/thumb/3l.jpg"

def test_format_embed_context(kudosu_gain_event):
    embed: Embed = format_embed(kudosu_gain_event)
    
    assert len(embed.fields) == 2
    assert embed.fields[1].name == format_context_field_name(kudosu_gain_event)
    assert embed.fields[1].value == format_context_field_value(kudosu_gain_event)

def test_format_field_name(suggestion_event):
    assert format_field_name(suggestion_event) == ":yellow_circle: Suggestion"

def test_format_field_name_qualify(qualify_event):
    assert format_field_name(qualify_event) == ":heart: Qualified"

def test_format_field_value(suggestion_event):
    assert (
        format_field_value(suggestion_event) ==
        "[**artist - title**](https://osu.ppy.sh/beatmapsets/3)\nMapped by [sometwo](https://osu.ppy.sh/users/2) [**osu**]"
    )

def test_format_field_value_markdown(qualify_event):
    assert (
        format_field_value(qualify_event) ==
        "[**artist\\_with\\*strange\\~symbols\\` - title**](https://osu.ppy.sh/beatmapsets/3)\nMapped by [\\_sometwo\\_](https://osu.ppy.sh/users/2) [**osu**]"
    )

def test_format_footer_text(suggestion_event):
    assert format_footer_text(suggestion_event) == "someone \"hi\""

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

def test_format_footer_text_nominate_praise(test_database):
    beatmapset = Beatmapset(3, "artist", "title", User(4, "mapper"), ["osu"])
    nominator = User(2, "sometwo")
    discussion = Discussion(7, beatmapset, user=nominator, content="nice")

    praise_event = Event("praise", from_string("2020-01-01 04:56:00"), beatmapset, discussion, user=nominator, content=discussion.content)
    nom_event = Event("nominate", from_string("2020-01-01 05:00:00"), beatmapset, user=nominator)

    test_database.insert_event(praise_event)
    test_database.insert_event(nom_event)

    assert format_footer_text(nom_event, database=test_database) == "sometwo \"nice\""

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

def test_format_thumbnail_url(suggestion_event):
    assert format_thumbnail_url(suggestion_event) == "https://b.ppy.sh/thumb/3l.jpg"

def test_context_field_name(kudosu_gain_event):
    assert format_context_field_name(kudosu_gain_event) == "\\_someone\\_"

def test_context_field_value(kudosu_gain_event):
    assert format_context_field_value(kudosu_gain_event) == "\"hi\\*\""

def test_context_field_value_truncate(kudosu_gain_event):
    kudosu_gain_event.discussion.content = "a very long piece of text " * 10
    assert format_context_field_value(kudosu_gain_event) == "\"a very long piece of text a very long piece of text a ver...\""

def test_history(test_database):
    beatmapset = Beatmapset(3, "artist", "title", User(4, "mapper"), ["osu"])
    nom_event = Event("nominate", from_string("2020-01-01 00:00:00"), beatmapset, user=User(1, "someone"))
    qual_event = Event("qualify", from_string("2020-01-01 05:00:00"), beatmapset, user=User(2, "sometwo"))

    test_database.insert_event(nom_event)
    test_database.insert_event(qual_event)

    history = format_history(beatmapset, database=test_database)
    assert history == "\n:thought_balloon: [someone](https://osu.ppy.sh/users/1) :heart: [sometwo](https://osu.ppy.sh/users/2)"

def test_history_filtering(test_database):
    beatmapset = Beatmapset(3, "artist", "title", User(4, "mapper"), ["osu"])
    nom_event = Event("nominate", from_string("2020-01-01 00:00:00"), beatmapset, user=User(1, "someone"))
    qual_event = Event("qualify", from_string("2020-01-01 05:00:00"), beatmapset, user=User(2, "sometwo"))
    suggestion_event = Event("suggestion", from_string("2020-01-01 01:00:00"), beatmapset, user=User(3, "somethree"))

    test_database.insert_event(nom_event)
    test_database.insert_event(qual_event)
    test_database.insert_event(suggestion_event)

    # The suggestion event should not appear in the history.
    history = format_history(beatmapset, database=test_database)
    assert history == "\n:thought_balloon: [someone](https://osu.ppy.sh/users/1) :heart: [sometwo](https://osu.ppy.sh/users/2)"

def test_history_truncated(test_database):
    beatmapset = Beatmapset(3, "artist", "title", User(4, "mapper"), ["osu"])
    nom_event = Event("nominate", from_string("2020-01-01 00:00:00"), beatmapset, user=User(1, "someone"))
    qual_event = Event("qualify", from_string("2020-01-01 05:00:00"), beatmapset, user=User(2, "sometwo"))

    for _ in range(20):
        test_database.insert_event(nom_event)
        nom_event.time += timedelta(seconds=15)
    test_database.insert_event(qual_event)

    history = format_history(beatmapset, length_limit=200, database=test_database)
    expected_history = "\n..."
    for _ in range(10):
        expected_history += ":thought_balloon: "
    assert history == expected_history + ":heart:"
    assert len(history) <= 200

def test_recent_praise(test_database):
    beatmapset = Beatmapset(3, "artist", "title", User(4, "mapper"), ["osu"])
    nominator = User(2, "sometwo")
    discussion = Discussion(7, beatmapset, user=nominator, content="nice")

    praise_event = Event("praise", from_string("2020-01-01 04:56:00"), beatmapset, discussion, user=nominator, content=discussion.content)
    nom_event = Event("nominate", from_string("2020-01-01 05:00:00"), beatmapset, user=nominator)

    test_database.insert_event(praise_event)
    test_database.insert_event(nom_event)

    praise = format_recent_praise(nominator, beatmapset, database=test_database)
    assert praise == "nice"

def test_recent_praise_none(test_database):
    beatmapset = Beatmapset(3, "artist", "title", User(4, "mapper"), ["osu"])
    nominator = User(2, "sometwo")

    nom_event = Event("nominate", from_string("2020-01-01 05:00:00"), beatmapset, user=nominator)

    test_database.insert_event(nom_event)

    praise = format_recent_praise(nominator, beatmapset, database=test_database)
    assert praise is None

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
import pytest
from discord import Embed

from aiess import Event, User, Beatmapset, Discussion
from aiess.timestamp import from_string

from formatter import format_link
from formatter import format_embed
from formatter import format_field_name
from formatter import format_field_value
from formatter import format_footer_text
from formatter import format_footer_icon_url
from formatter import format_thumbnail_url

@pytest.fixture
def suggestion_event():
    beatmapset = Beatmapset(3, "artist", "title", User(2, "sometwo"), ["osu"])
    user = User(1, "someone")
    discussion = Discussion(5, beatmapset, user, content="hi")
    event = Event("suggestion", from_string("2020-04-11 20:00:00"), beatmapset, discussion, user, content="hi")

    return event



def test_format_link_discussion(suggestion_event):
    assert format_link(suggestion_event) == "https://osu.ppy.sh/beatmapsets/3/discussion#/5"

def test_format_link_no_discussion():
    beatmapset = Beatmapset(3, "artist", "title", User(2, "sometwo"), ["osu"])
    user = User(1, "someone")
    event = Event("nominate", from_string("2020-04-11 20:00:00"), beatmapset, user=user)

    assert format_link(event) == "https://osu.ppy.sh/beatmapsets/3"

def test_format_link_no_beatmapset():
    event = Event("test", from_string("2020-04-11 20:00:00"))

    with pytest.raises(ValueError) as err:
        format_link(event)
    
    assert "missing a beatmapset" in str(err)



def test_format_embed(suggestion_event):
    embed = format_embed(suggestion_event)
    
    assert embed.fields[0].name == ":yellow_circle: Suggestion"
    assert (embed.fields[0].value ==
        "[**artist - title**](https://osu.ppy.sh/beatmapsets/3)\nMapped by [sometwo](https://osu.ppy.sh/users/2) [**osu**]")
    assert embed.footer.text == "someone \"hi\""
    assert embed.footer.icon_url == "https://a.ppy.sh/1"
    assert embed.colour.to_rgb() == (200, 180, 220)
    assert embed.thumbnail.url == "https://b.ppy.sh/thumb/3l.jpg"

def test_format_field_name(suggestion_event):
    assert format_field_name(suggestion_event) == ":yellow_circle: Suggestion"

def test_format_field_value(suggestion_event):
    assert (format_field_value(suggestion_event) ==
        "[**artist - title**](https://osu.ppy.sh/beatmapsets/3)\nMapped by [sometwo](https://osu.ppy.sh/users/2) [**osu**]")

def test_format_footer_text(suggestion_event):
    assert format_footer_text(suggestion_event) == "someone \"hi\""

def test_format_footer_icon_url(suggestion_event):
    assert format_footer_icon_url(suggestion_event) == "https://a.ppy.sh/1"

def test_format_thumbnail_url(suggestion_event):
    assert format_thumbnail_url(suggestion_event) == "https://b.ppy.sh/thumb/3l.jpg"
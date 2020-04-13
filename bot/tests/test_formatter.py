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

@pytest.fixture
def qualify_event():
    beatmapset = Beatmapset(3, "artist_with*strange~symbols`", "title", User(2, "_sometwo_"), ["osu"])
    event = Event("qualify", from_string("2020-04-11 20:00:00"), beatmapset)

    return event


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
    assert (embed.fields[0].value ==
        "[**artist - title**](https://osu.ppy.sh/beatmapsets/3)\nMapped by [sometwo](https://osu.ppy.sh/users/2) [**osu**]")
    assert embed.footer.text == "someone \"hi\""
    assert embed.footer.icon_url == "https://a.ppy.sh/1"
    assert embed.colour.to_rgb() == (65, 65, 65)
    assert embed.thumbnail.url == "https://b.ppy.sh/thumb/3l.jpg"

def test_format_field_name(suggestion_event):
    assert format_field_name(suggestion_event) == ":yellow_circle: Suggestion"

def test_format_field_name_qualify(qualify_event):
    assert format_field_name(qualify_event) == ":heart: Qualified"

def test_format_field_value(suggestion_event):
    assert (format_field_value(suggestion_event) ==
        "[**artist - title**](https://osu.ppy.sh/beatmapsets/3)\nMapped by [sometwo](https://osu.ppy.sh/users/2) [**osu**]")

def test_format_field_value_markdown(qualify_event):
    assert (format_field_value(qualify_event) ==
        "[**artist\\_with\\*strange\\~symbols\\` - title**](https://osu.ppy.sh/beatmapsets/3)\nMapped by [\\_sometwo\\_](https://osu.ppy.sh/users/2) [**osu**]")

def test_format_footer_text(suggestion_event):
    assert format_footer_text(suggestion_event) == "someone \"hi\""

def test_format_footer_text_no_user(qualify_event):
    assert format_footer_text(qualify_event) == Embed.Empty

def test_format_footer_text_long(suggestion_event):
    suggestion_event.content = "04:25:218 (3,4) - the guitar is really strong here so mapping to the red beats only feels unfitting"
    assert format_footer_text(suggestion_event) == "someone \"04:25:218 (3,4) - the guitar is really strong here so map...\""

def test_format_footer_text_newline(suggestion_event):
    suggestion_event.content = "04:25:218 (3,4) - the guitar is really strong here so\nmapping to the red beats only feels unfitting"
    assert format_footer_text(suggestion_event) == "someone \"04:25:218 (3,4) - the guitar is really strong here so\""

def test_format_footer_text_no_comment(suggestion_event):
    suggestion_event.content = ""
    assert format_footer_text(suggestion_event) == "someone"

def test_format_footer_icon_url(suggestion_event):
    assert format_footer_icon_url(suggestion_event) == "https://a.ppy.sh/1"

def test_format_footer_icon_url_no_user(qualify_event):
    assert format_footer_icon_url(qualify_event) == Embed.Empty

def test_format_thumbnail_url(suggestion_event):
    assert format_thumbnail_url(suggestion_event) == "https://b.ppy.sh/thumb/3l.jpg"
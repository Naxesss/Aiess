import sys
sys.path.append('..')

import pytest
from unittest import mock

from discord import Embed

from aiess import Event, Beatmapset, User
from aiess.database import SCRAPER_TEST_DB_NAME
from aiess.timestamp import from_string

from bot.tests.commands.mock_command import MockCommand, MockMessage, MockChannel, MockGuild, MockDMChannel
from bot.cmd_modules import cmd_recent
from bot.receiver import receive_command
from bot.database import Database
from bot.commands import help_embed
from bot.cmdcommon import filters_embed, filter_embed

def setup_function():
    database = Database(SCRAPER_TEST_DB_NAME)
    # Reset database to state before any tests ran.
    database.clear_table_data("events")
    database.clear_table_data("discussions")
    database.clear_table_data("beatmapsets")
    database.clear_table_data("users")
    database.clear_table_data("beatmapset_modes")

def test_correct_setup():
    database = Database(SCRAPER_TEST_DB_NAME)
    assert not database.retrieve_table_data("events")
    assert not database.retrieve_table_data("discussions")
    assert not database.retrieve_table_data("beatmapsets")
    assert not database.retrieve_table_data("users")
    assert not database.retrieve_table_data("beatmapset_modes")

@pytest.mark.asyncio
@mock.patch("bot.cmd_modules.cmd_recent.SCRAPER_DB_NAME", SCRAPER_TEST_DB_NAME)
async def test_recent():
    beatmapset = Beatmapset(1, "artist", "title", creator=User(2, "sometwo"), modes=["osu"])
    event1 = Event("nominate", from_string("2020-01-01 00:00:00"), beatmapset, user=User(1, "someone"))
    event2 = Event("qualify", from_string("2020-01-01 01:00:00"), beatmapset, user=User(4, "somefour"), content="nicely done")

    database = Database(SCRAPER_TEST_DB_NAME)
    database.insert_event(event1)
    database.insert_event(event2)

    mock_message = MockMessage(channel=MockChannel(_id=6, guild=MockGuild(_id=2)))
    mock_command = MockCommand("recent", "type:(nominate or qualify)", context=mock_message)

    assert await receive_command(mock_command)

    assert mock_command.response.startswith("✓")
    assert "https://osu.ppy.sh/beatmapsets/1" in mock_command.response
    assert mock_command.response_embed
    assert mock_command.response_embed.fields
    assert mock_command.response_embed.fields[0].name.startswith(":heart:\u2000Qualified (**")
    assert mock_command.response_embed.fields[0].name.endswith("** ago)")
    assert "artist - title" in mock_command.response_embed.fields[0].value
    assert "sometwo" in mock_command.response_embed.fields[0].value
    assert mock_command.response_embed.footer.text == "somefour \"nicely done\""
    assert mock_command.response_embed.footer.icon_url == "https://a.ppy.sh/4"

@pytest.mark.asyncio
@mock.patch("bot.cmd_modules.cmd_recent.SCRAPER_DB_NAME", SCRAPER_TEST_DB_NAME)
async def test_recent_not_found():
    mock_message = MockMessage(channel=MockChannel(_id=6, guild=MockGuild(_id=2)))
    mock_command = MockCommand("recent", "type:(nominate or qualify)", context=mock_message)

    assert await receive_command(mock_command)

    assert mock_command.response == "✗ No event matching `type:(nominate or qualify)` could be found."
    assert mock_command.response_embed.fields[0].name == help_embed("recent").fields[0].name
    assert mock_command.response_embed.fields[0].value == help_embed("recent").fields[0].value

@pytest.mark.asyncio
@mock.patch("bot.cmd_modules.cmd_recent.SCRAPER_DB_NAME", SCRAPER_TEST_DB_NAME)
async def test_recent_dm_channel():
    mock_message = MockMessage(channel=MockDMChannel(_id=6))
    mock_command = MockCommand("recent", "type:(nominate or qualify)", context=mock_message)

    assert await receive_command(mock_command)

    assert mock_command.response.startswith("✗")
    assert "DM channel" in mock_command.response
    assert mock_command.response_embed.fields[0].name == mock_command.help_embed().fields[0].name
    assert mock_command.response_embed.fields[0].value == mock_command.help_embed().fields[0].value

@pytest.mark.asyncio
@mock.patch("bot.cmd_modules.cmd_recent.SCRAPER_DB_NAME", SCRAPER_TEST_DB_NAME)
async def test_recent_invalid_key():
    mock_message = MockMessage(channel=MockChannel(_id=6, guild=MockGuild(_id=2)))
    mock_command = MockCommand("recent", "undefined:test", context=mock_message)

    assert await receive_command(mock_command)

    assert mock_command.response.startswith("✗")
    assert "invalid key" in mock_command.response.lower()
    assert mock_command.response_embed.fields[0].name == filters_embed().fields[0].name
    assert mock_command.response_embed.fields[0].value == filters_embed().fields[0].value

@pytest.mark.asyncio
@mock.patch("bot.cmd_modules.cmd_recent.SCRAPER_DB_NAME", SCRAPER_TEST_DB_NAME)
async def test_recent_invalid_value():
    mock_message = MockMessage(channel=MockChannel(_id=6, guild=MockGuild(_id=2)))
    mock_command = MockCommand("recent", "type:undefined", context=mock_message)

    assert await receive_command(mock_command)

    assert mock_command.response.startswith("✗")
    assert "invalid value" in mock_command.response.lower()
    assert mock_command.response_embed.fields[0].name == filter_embed("type").fields[0].name
    assert mock_command.response_embed.fields[0].value == filter_embed("type").fields[0].value

@pytest.mark.asyncio
@mock.patch("bot.cmd_modules.cmd_recent.SCRAPER_DB_NAME", SCRAPER_TEST_DB_NAME)
async def test_recent_invalid_word():
    mock_message = MockMessage(channel=MockChannel(_id=6, guild=MockGuild(_id=2)))
    mock_command = MockCommand("recent", "type:nominate eand type:qualify", context=mock_message)

    assert await receive_command(mock_command)

    assert mock_command.response.startswith("✗")
    assert "invalid word" in mock_command.response.lower()
    assert mock_command.response_embed.fields[0].name == filters_embed().fields[0].name
    assert mock_command.response_embed.fields[0].value == filters_embed().fields[0].value
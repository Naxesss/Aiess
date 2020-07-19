import sys
sys.path.append('..')

import pytest

from bot import subscriber
from bot.tests.commands.mock_command import MockCommand, MockMessage, MockChannel, MockGuild, MockDMChannel
from bot.prefixes import DEFAULT_PREFIX
from bot.cmd_modules import cmd_sub
from bot.receiver import receive_command
from bot.database import Database, BOT_TEST_DB_NAME
from bot.objects import Subscription
from bot.cmdcommon import filters_embed, filter_embed

def setup_function():
    # Reset database to state before any tests ran.
    Database(BOT_TEST_DB_NAME).clear_table_data("subscriptions")
    # Use the test database by default, so we don't clutter the production one.
    subscriber.DEFAULT_DB_NAME = BOT_TEST_DB_NAME
    subscriber.cache = []

def test_correct_setup():
    assert not Database(BOT_TEST_DB_NAME).retrieve_table_data("subscriptions")

@pytest.mark.asyncio
async def test_sub():
    mock_message = MockMessage(channel=MockChannel(_id=6, guild=MockGuild(_id=2)))
    mock_command = MockCommand("sub", "type:(nominate or qualify)", context=mock_message)

    assert await receive_command(mock_command)

    assert mock_command.response.startswith("✓")
    assert mock_command.response_embed
    assert mock_command.response_embed.fields
    assert "🔔\u2000Subscribed" in mock_command.response_embed.fields[0].name
    assert f"type:(nominate or qualify)" in mock_command.response_embed.fields[0].value
    assert f"`type:nominate or type:qualify`" in mock_command.response_embed.fields[0].value

    assert subscriber.cache[0].channel_id == mock_message.channel.id
    assert subscriber.cache[0].filter == mock_command.args[0]

@pytest.mark.asyncio
async def test_sub_markdown_and_quotes():
    mock_message = MockMessage(channel=MockChannel(_id=6, guild=MockGuild(_id=2)))
    mock_command = MockCommand("sub", "user:\"__don't underline this__\"", context=mock_message)

    assert await receive_command(mock_command)

    assert mock_command.response.startswith("✓")
    assert mock_command.response_embed
    assert mock_command.response_embed.fields
    assert "🔔\u2000Subscribed" in mock_command.response_embed.fields[0].name
    assert f"user:\"\\_\\_don't underline this\\_\\_\"" in mock_command.response_embed.fields[0].value
    assert f"`user:\"__don't underline this__\"`" in mock_command.response_embed.fields[0].value

    assert subscriber.cache[0].channel_id == mock_message.channel.id
    assert subscriber.cache[0].filter == mock_command.args[0]

@pytest.mark.asyncio
async def test_sub_dm_channel():
    mock_message = MockMessage(channel=MockDMChannel(_id=6))
    mock_command = MockCommand("sub", "type:nominate", context=mock_message)

    assert await receive_command(mock_command)
    assert mock_command.response.startswith("✗")
    assert "DM channel" in mock_command.response
    assert mock_command.response_embed.fields[0].name == mock_command.help_embed().fields[0].name
    assert mock_command.response_embed.fields[0].value == mock_command.help_embed().fields[0].value
    assert not subscriber.cache

@pytest.mark.asyncio
async def test_sub_no_arg():
    subscriber.add_subscription(Subscription(guild_id=2, channel_id=6, _filter="type:(nominate or qualify)"))

    mock_message = MockMessage(channel=MockChannel(_id=6, guild=MockGuild(_id=2)))
    mock_command = MockCommand("sub", context=mock_message)

    assert await receive_command(mock_command)
    assert f"`{DEFAULT_COMMAND_PREFIX}sub <filter>`" in mock_command.response  # Should suggest these for if the user intended something else.
    assert f"`{DEFAULT_COMMAND_PREFIX}unsub`" in mock_command.response
    assert "🔔\u2000Current Subscription" in mock_command.response_embed.fields[0].name
    assert f"type:(nominate or qualify)" in mock_command.response_embed.fields[0].value
    assert f"`type:nominate or type:qualify`" in mock_command.response_embed.fields[0].value

@pytest.mark.asyncio
async def test_sub_no_arg_no_sub():
    mock_message = MockMessage(channel=MockChannel(_id=6, guild=MockGuild(_id=2)))
    mock_command = MockCommand("sub", context=mock_message)

    assert await receive_command(mock_command)
    assert f"`{DEFAULT_COMMAND_PREFIX}sub <filter>`" in mock_command.response  # Should suggest these for if the user intended something else.
    assert f"`{DEFAULT_COMMAND_PREFIX}unsub`" not in mock_command.response  # Don't need to suggest unsubscribing if we don't have a sub.
    assert "🔔\u2000Current Subscription" in mock_command.response_embed.fields[0].name
    assert f"None" in mock_command.response_embed.fields[0].value

@pytest.mark.asyncio
async def test_sub_parenthesis_inequality():
    mock_message = MockMessage(channel=MockChannel(_id=6, guild=MockGuild(_id=2)))
    mock_command = MockCommand("sub", "type:(nominate", context=mock_message)

    assert await receive_command(mock_command)
    assert mock_command.response.startswith("✗")
    assert "parenthes" in mock_command.response.lower()
    assert mock_command.response_embed.fields[0].name == mock_command.help_embed().fields[0].name
    assert mock_command.response_embed.fields[0].value == mock_command.help_embed().fields[0].value
    assert not subscriber.cache

@pytest.mark.asyncio
async def test_sub_undefined_type():
    mock_message = MockMessage(channel=MockChannel(_id=6, guild=MockGuild(_id=2)))
    mock_command = MockCommand("sub", "type:undefined", context=mock_message)

    assert await receive_command(mock_command)
    assert mock_command.response.startswith("✗")
    assert "`type:undefined`" in mock_command.response.lower()
    assert mock_command.response_embed.fields[0].name == filter_embed("type").fields[0].name
    assert mock_command.response_embed.fields[0].value == filter_embed("type").fields[0].value
    assert not subscriber.cache

@pytest.mark.asyncio
async def test_sub_undefined_type_duplicates():
    mock_message = MockMessage(channel=MockChannel(_id=6, guild=MockGuild(_id=2)))
    mock_command = MockCommand("sub", "type:undefined or type:undefined", context=mock_message)

    assert await receive_command(mock_command)
    assert mock_command.response.startswith("✗")
    assert mock_command.response.lower().count("`type:undefined`") == 1
    assert mock_command.response_embed.fields[0].name == filter_embed("type").fields[0].name
    assert mock_command.response_embed.fields[0].value == filter_embed("type").fields[0].value
    assert not subscriber.cache

@pytest.mark.asyncio
async def test_sub_undefined_key():
    mock_message = MockMessage(channel=MockChannel(_id=6, guild=MockGuild(_id=2)))
    mock_command = MockCommand("sub", "undefined:nominate or undefined:qualify", context=mock_message)

    assert await receive_command(mock_command)
    assert mock_command.response.startswith("✗")
    assert mock_command.response.lower().count("`undefined`") == 1
    assert mock_command.response_embed.fields[0].name == filters_embed().fields[0].name
    assert mock_command.response_embed.fields[0].value == filters_embed().fields[0].value
    assert not subscriber.cache

@pytest.mark.asyncio
async def test_sub_forgotten_colon():
    mock_message = MockMessage(channel=MockChannel(_id=6, guild=MockGuild(_id=2)))
    mock_command = MockCommand("sub", "typequalify and type:nominate", context=mock_message)

    assert await receive_command(mock_command)
    assert mock_command.response.startswith("✗")
    assert "`typequalify`" in mock_command.response
    assert mock_command.response_embed.fields[0].name == filters_embed().fields[0].name
    assert mock_command.response_embed.fields[0].value == filters_embed().fields[0].value
    assert not subscriber.cache

@pytest.mark.asyncio
async def test_sub_typoed_and():
    mock_message = MockMessage(channel=MockChannel(_id=6, guild=MockGuild(_id=2)))
    mock_command = MockCommand("sub", "type:qualify annd type:nominate", context=mock_message)

    assert await receive_command(mock_command)
    assert mock_command.response.startswith("✗")
    assert "`annd`" in mock_command.response
    assert mock_command.response_embed.fields[0].name == filters_embed().fields[0].name
    assert mock_command.response_embed.fields[0].value == filters_embed().fields[0].value
    assert not subscriber.cache

@pytest.mark.asyncio
async def test_sub_exclamation_in_value():
    mock_message = MockMessage(channel=MockChannel(_id=6, guild=MockGuild(_id=2)))
    mock_command = MockCommand("sub", "mode:osu or mode:osu!catch", context=mock_message)

    assert await receive_command(mock_command)
    assert mock_command.response.startswith("✗")
    assert "`!mode`" in mock_command.response
    assert mock_command.response_embed.fields[0].name == filters_embed().fields[0].name
    assert mock_command.response_embed.fields[0].value == filters_embed().fields[0].value
    assert not subscriber.cache
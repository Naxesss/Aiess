import sys
sys.path.append('..')

import pytest

from bot import subscriber
from bot.tests.commands.mock_command import MockCommand, MockMessage, MockChannel, MockGuild, MockDMChannel
from bot.cmd_modules import cmd_sub
from bot.receiver import receive_command
from bot.database import Database, BOT_TEST_DB_NAME

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
    assert "🔔 Subscribed" in mock_command.response_embed.fields[0].name
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
    assert "🔔 Subscribed" in mock_command.response_embed.fields[0].name
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
    mock_message = MockMessage(channel=MockChannel(_id=6, guild=MockGuild(_id=2)))
    mock_command = MockCommand("sub", context=mock_message)

    assert not await receive_command(mock_command)
    assert mock_command.response.startswith("✗")
    assert "argument" in mock_command.response.lower()
    assert mock_command.response_embed.fields[0].name == mock_command.help_embed().fields[0].name
    assert mock_command.response_embed.fields[0].value == mock_command.help_embed().fields[0].value
    assert not subscriber.cache

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
    assert mock_command.response_embed.fields[0].name == mock_command.help_embed().fields[0].name
    assert mock_command.response_embed.fields[0].value == mock_command.help_embed().fields[0].value
    assert not subscriber.cache

@pytest.mark.asyncio
async def test_sub_undefined_type_duplicates():
    mock_message = MockMessage(channel=MockChannel(_id=6, guild=MockGuild(_id=2)))
    mock_command = MockCommand("sub", "type:undefined or type:undefined", context=mock_message)

    assert await receive_command(mock_command)
    assert mock_command.response.startswith("✗")
    assert mock_command.response.lower().count("`type:undefined`") == 1
    assert mock_command.response_embed.fields[0].name == mock_command.help_embed().fields[0].name
    assert mock_command.response_embed.fields[0].value == mock_command.help_embed().fields[0].value
    assert not subscriber.cache

@pytest.mark.asyncio
async def test_sub_undefined_key():
    mock_message = MockMessage(channel=MockChannel(_id=6, guild=MockGuild(_id=2)))
    mock_command = MockCommand("sub", "undefined:nominate or undefined:qualify", context=mock_message)

    assert await receive_command(mock_command)
    assert mock_command.response.startswith("✗")
    assert mock_command.response.lower().count("`undefined`") == 1
    assert mock_command.response_embed.fields[0].name == mock_command.help_embed().fields[0].name
    assert mock_command.response_embed.fields[0].value == mock_command.help_embed().fields[0].value
    assert not subscriber.cache

@pytest.mark.asyncio
async def test_sub_forgotten_colon():
    mock_message = MockMessage(channel=MockChannel(_id=6, guild=MockGuild(_id=2)))
    mock_command = MockCommand("sub", "typequalify and type:nominate", context=mock_message)

    assert await receive_command(mock_command)
    assert mock_command.response.startswith("✗")
    assert "`typequalify`" in mock_command.response
    assert mock_command.response_embed.fields[0].name == mock_command.help_embed().fields[0].name
    assert mock_command.response_embed.fields[0].value == mock_command.help_embed().fields[0].value
    assert not subscriber.cache

@pytest.mark.asyncio
async def test_sub_typoed_and():
    mock_message = MockMessage(channel=MockChannel(_id=6, guild=MockGuild(_id=2)))
    mock_command = MockCommand("sub", "type:qualify annd type:nominate", context=mock_message)

    assert await receive_command(mock_command)
    assert mock_command.response.startswith("✗")
    assert "`annd`" in mock_command.response
    assert mock_command.response_embed.fields[0].name == mock_command.help_embed().fields[0].name
    assert mock_command.response_embed.fields[0].value == mock_command.help_embed().fields[0].value
    assert not subscriber.cache

@pytest.mark.asyncio
async def test_sub_exclamation_in_value():
    mock_message = MockMessage(channel=MockChannel(_id=6, guild=MockGuild(_id=2)))
    mock_command = MockCommand("sub", "mode:osu or mode:osu!catch", context=mock_message)

    assert await receive_command(mock_command)
    assert mock_command.response.startswith("✗")
    assert "`!mode`" in mock_command.response
    assert mock_command.response_embed.fields[0].name == mock_command.help_embed().fields[0].name
    assert mock_command.response_embed.fields[0].value == mock_command.help_embed().fields[0].value
    assert not subscriber.cache
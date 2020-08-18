import sys
sys.path.append('..')

import pytest

from bot.tests.commands.mock_command import MockCommand, MockMessage, MockChannel, MockDMChannel, MockGuild
from bot.cmd_modules import cmd_prefix
from bot.receiver import receive_command
from bot import prefixes
from bot.database import Database, BOT_TEST_DB_NAME

def setup_function():
    prefixes.DEFAULT_DB_NAME = BOT_TEST_DB_NAME
    Database(BOT_TEST_DB_NAME).clear_table_data("prefixes")
    prefixes.cache = {}

@pytest.mark.asyncio
async def test_prefix():
    mock_command = MockCommand("prefix", "&", context=MockMessage(channel=MockChannel(guild=MockGuild(_id=8))))
    
    assert await receive_command(mock_command)
    assert mock_command.response.startswith("✓")
    assert "`+`" in mock_command.response
    assert "`&`" in mock_command.response
    assert mock_command.prefix() == "&"

@pytest.mark.asyncio
async def test_prefix_dm_channel():
    mock_command = MockCommand("prefix", "&", context=MockMessage(channel=MockDMChannel()))
    
    assert await receive_command(mock_command)
    assert mock_command.response.startswith("✗")
    assert "DM channel" in mock_command.response

@pytest.mark.asyncio
async def test_prefix_whitespace_in_symbol():
    mock_command = MockCommand("prefix", "a b", context=MockMessage(channel=MockChannel(guild=MockGuild(_id=8))))
    
    assert await receive_command(mock_command)
    assert mock_command.response.startswith("✗")
    assert "whitespace" in mock_command.response.lower()

@pytest.mark.asyncio
async def test_prefix_very_long_symbol():
    mock_command = MockCommand("prefix", "a" * 2000, context=MockMessage(channel=MockChannel(guild=MockGuild(_id=8))))
    
    assert await receive_command(mock_command)
    assert mock_command.response.startswith("✗")
    assert "cannot exceed" in mock_command.response
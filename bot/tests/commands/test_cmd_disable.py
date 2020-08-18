import sys
sys.path.append('..')

import pytest

from bot.tests.commands.mock_command import MockCommand, MockMessage, MockChannel, MockDMChannel, MockGuild
from bot.cmd_modules import cmd_disable
from bot.receiver import receive_command
from bot.commands import help_embed, get_wrapper
from bot.database import Database, BOT_TEST_DB_NAME
from bot.cmdcommon import permissions_embed

from bot import permissions
from bot.permissions import get_permission_filter, set_permission_filter

def setup_function():
    permissions.DEFAULT_DB_NAME = BOT_TEST_DB_NAME
    Database(BOT_TEST_DB_NAME).clear_table_data("permissions")
    permissions.cache = {}

@pytest.mark.asyncio
async def test_disable():
    mock_command = MockCommand("disable", "disable", context=MockMessage(channel=MockChannel(guild=MockGuild(_id=3))))
    set_permission_filter(guild_id=3, command_wrapper=get_wrapper("disable"), permission_filter="user:<@0>")

    assert await receive_command(mock_command)
    assert "✓" in mock_command.response
    expected_embed = permissions_embed(guild_id=3, command_wrappers=[get_wrapper("disable")])
    assert mock_command.response_embed.fields[0].name == expected_embed.fields[0].name
    assert mock_command.response_embed.fields[0].value == expected_embed.fields[0].value
    assert not get_permission_filter(guild_id=3, command_wrapper=get_wrapper("disable"))

@pytest.mark.asyncio
async def test_disable_dm_channel():
    mock_command = MockCommand("disable", "disable", context=MockMessage(channel=MockDMChannel()))
    
    assert await receive_command(mock_command)
    assert "✗" in mock_command.response
    assert "dm channel" in mock_command.response.lower()
    assert mock_command.response_embed.fields[0].name == help_embed("disable").fields[0].name
    assert mock_command.response_embed.fields[0].value == help_embed("disable").fields[0].value
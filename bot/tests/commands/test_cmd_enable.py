import sys
sys.path.append('..')

import pytest

from bot.tests.commands.mock_command import MockCommand, MockMessage, MockChannel, MockDMChannel, MockGuild
from bot.cmd_modules import cmd_enable
from bot.receiver import receive_command
from bot.commands import help_embed, get_wrapper
from bot.database import Database, BOT_TEST_DB_NAME
from bot.cmdcommon import permissions_embed, filter_embed, filters_embed
from bot.filterers.perms_filterer import filter_context

from bot import permissions
from bot.permissions import get_permission_filter

def setup_function():
    permissions.DEFAULT_DB_NAME = BOT_TEST_DB_NAME
    Database(BOT_TEST_DB_NAME).clear_table_data("permissions")
    permissions.cache = {}

@pytest.mark.asyncio
async def test_enable():
    mock_command = MockCommand("enable", "enable", context=MockMessage(channel=MockChannel(guild=MockGuild(_id=3))))

    assert await receive_command(mock_command)
    assert "✓" in mock_command.response
    expected_embed = permissions_embed(guild_id=3, command_wrappers=[get_wrapper("enable")])
    assert mock_command.response_embed.fields[0].name == expected_embed.fields[0].name
    assert mock_command.response_embed.fields[0].value == expected_embed.fields[0].value
    assert get_permission_filter(guild_id=3, command_wrapper=get_wrapper("enable")) == "role:<@&0>"

@pytest.mark.asyncio
async def test_enable_with_filter():
    mock_command = MockCommand("enable", "enable", "user:<@0>", context=MockMessage(channel=MockChannel(guild=MockGuild(_id=3))))
    
    assert await receive_command(mock_command)
    assert "✓" in mock_command.response
    expected_embed = permissions_embed(guild_id=3, command_wrappers=[get_wrapper("enable")])
    assert mock_command.response_embed.fields[0].name == expected_embed.fields[0].name
    assert mock_command.response_embed.fields[0].value == expected_embed.fields[0].value
    assert get_permission_filter(guild_id=3, command_wrapper=get_wrapper("enable")) == "user:<@0>"

@pytest.mark.asyncio
async def test_enable_invalid_key():
    mock_command = MockCommand("enable", "enable", "undefined:value", context=MockMessage(channel=MockChannel(guild=MockGuild(_id=3))))

    assert await receive_command(mock_command)
    assert "✗" in mock_command.response
    assert "invalid key" in mock_command.response.lower()
    expected_embed = filters_embed(filter_context=filter_context)
    assert mock_command.response_embed.fields[0].name == expected_embed.fields[0].name
    assert mock_command.response_embed.fields[0].value == expected_embed.fields[0].value
    assert not get_permission_filter(guild_id=3, command_wrapper=get_wrapper("enable"))

@pytest.mark.asyncio
async def test_enable_invalid_value():
    mock_command = MockCommand("enable", "enable", "user:name", context=MockMessage(channel=MockChannel(guild=MockGuild(_id=3))))

    assert await receive_command(mock_command)
    assert "✗" in mock_command.response
    assert "invalid value" in mock_command.response.lower()
    expected_embed = filter_embed(key="user", filter_context=filter_context)
    assert mock_command.response_embed.fields[0].name == expected_embed.fields[0].name
    assert mock_command.response_embed.fields[0].value == expected_embed.fields[0].value
    assert not get_permission_filter(guild_id=3, command_wrapper=get_wrapper("enable"))

@pytest.mark.asyncio
async def test_enable_invalid_word():
    mock_command = MockCommand("enable", "enable", "user:<@0> gqjwnioqjwd", context=MockMessage(channel=MockChannel(guild=MockGuild(_id=3))))

    assert await receive_command(mock_command)
    assert "✗" in mock_command.response
    assert "invalid word" in mock_command.response.lower()
    expected_embed = filters_embed(filter_context=filter_context)
    assert mock_command.response_embed.fields[0].name == expected_embed.fields[0].name
    assert mock_command.response_embed.fields[0].value == expected_embed.fields[0].value
    assert not get_permission_filter(guild_id=3, command_wrapper=get_wrapper("enable"))

@pytest.mark.asyncio
async def test_enable_dm_channel():
    mock_command = MockCommand("enable", "enable", context=MockMessage(channel=MockDMChannel()))
    
    assert await receive_command(mock_command)
    assert "✗" in mock_command.response
    assert "dm channel" in mock_command.response.lower()
    assert mock_command.response_embed.fields[0].name == help_embed("enable").fields[0].name
    assert mock_command.response_embed.fields[0].value == help_embed("enable").fields[0].value
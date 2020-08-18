import sys
sys.path.append('..')

import pytest

from bot.tests.commands.mock_command import MockCommand, MockMessage, MockChannel, MockDMChannel, MockGuild
from bot.cmd_modules import cmd_perms
from bot.receiver import receive_command
from bot.prefixes import DEFAULT_PREFIX
from bot.prefixes import set_prefix
from bot.commands import help_embed

@pytest.mark.asyncio
async def test_perms():
    mock_command = MockCommand("perms", context=MockMessage(channel=MockChannel(guild=MockGuild(_id=3))))
    
    assert await receive_command(mock_command)
    assert f"`{DEFAULT_PREFIX}enable`" in mock_command.response
    assert f"`{DEFAULT_PREFIX}disable`" in mock_command.response
    assert "permissions" in mock_command.response_embed.fields[0].name.lower()
    assert mock_command.response_embed.fields[0].value.lower().startswith("***admin-only***")
    assert f"`{DEFAULT_PREFIX}perms/{DEFAULT_PREFIX}permissions [command(s)]`" in mock_command.response_embed.fields[0].value.lower()

@pytest.mark.asyncio
async def test_perms_custom_prefix():
    mock_command = MockCommand("perms", context=MockMessage(channel=MockChannel(guild=MockGuild(_id=8))))
    set_prefix(guild_id=8, prefix="&")
    
    assert await receive_command(mock_command)
    assert "`&enable`" in mock_command.response
    assert "`&disable`" in mock_command.response
    assert "permissions" in mock_command.response_embed.fields[0].name.lower()
    assert mock_command.response_embed.fields[0].value.lower().startswith("***admin-only***")
    assert "`&perms/&permissions [command(s)]`" in mock_command.response_embed.fields[0].value.lower()

@pytest.mark.asyncio
async def test_perms_dm_channel():
    mock_command = MockCommand("perms", context=MockMessage(channel=MockDMChannel()))
    
    assert await receive_command(mock_command)
    assert "✗" in mock_command.response
    assert "dm channel" in mock_command.response.lower()
    assert mock_command.response_embed.fields[0].name == help_embed("perms").fields[0].name
    assert mock_command.response_embed.fields[0].value == help_embed("perms").fields[0].value
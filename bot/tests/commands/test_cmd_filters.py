import sys
sys.path.append('..')

import pytest

from bot.tests.commands.mock_command import MockCommand, MockMessage, MockChannel, MockGuild
from bot.cmd_modules import cmd_filters
from bot.receiver import receive_command
from bot.prefixes import DEFAULT_PREFIX
from bot.prefixes import set_prefix
from bot.commands import help_embed

@pytest.mark.asyncio
async def test_filters():
    mock_command = MockCommand("filters", context=MockMessage(channel=MockChannel()))
    
    assert await receive_command(mock_command)
    assert f"`{DEFAULT_PREFIX}filters <key>`" in mock_command.response  # Should suggest using this for more details of a specific key.
    assert "filter" in mock_command.response_embed.title.lower()
    assert "case insensitive" in mock_command.response_embed.description
    assert "`key1:(value1 or value2) and key2:value3`" in mock_command.response_embed.description

    assert "keys" in mock_command.response_embed.fields[0].name.lower()
    assert "`/` denotes aliases" in mock_command.response_embed.fields[0].name.lower()
    assert "**`user`**" in mock_command.response_embed.fields[0].value.lower()
    assert "**`set-id/mapset-id/beatmapset-id`**" in mock_command.response_embed.fields[0].value.lower()

    assert "gates" in mock_command.response_embed.description.lower()
    assert "`and`" in mock_command.response_embed.description.lower()
    assert "`or`" in mock_command.response_embed.description.lower()
    assert "`not`" in mock_command.response_embed.description.lower()

@pytest.mark.asyncio
async def test_filters_with_arg():
    mock_command = MockCommand("filters", "user", context=MockMessage(channel=MockChannel()))
    
    assert await receive_command(mock_command)
    assert f"`{DEFAULT_PREFIX}filters`" in mock_command.response  # Should suggest using this for a list of keys and gates.
    assert "**`user`**" in mock_command.response_embed.fields[0].name.lower()
    assert "the username" in mock_command.response_embed.fields[0].value.lower()
    assert "value(s)" in mock_command.response_embed.fields[1].name.lower()
    assert "accepts any value" in mock_command.response_embed.fields[1].value.lower()
    assert "example(s)" in mock_command.response_embed.fields[2].name.lower()
    assert "∙\u00a0`user:lasse`" in mock_command.response_embed.fields[2].value.lower()

@pytest.mark.asyncio
async def test_filters_custom_prefix():
    mock_command = MockCommand("filters", context=MockMessage(channel=MockChannel(guild=MockGuild(_id=8))))
    set_prefix(guild_id=8, prefix="&")
    
    assert await receive_command(mock_command)
    assert f"`&filters <key>`" in mock_command.response

@pytest.mark.asyncio
async def test_filters_with_arg_custom_prefix():
    mock_command = MockCommand("filters", "user", context=MockMessage(channel=MockChannel(guild=MockGuild(_id=8))))
    set_prefix(guild_id=8, prefix="&")
    
    assert await receive_command(mock_command)
    assert f"`&filters`" in mock_command.response

@pytest.mark.asyncio
async def test_filters_unrecognized_command():
    mock_command = MockCommand("filters", "undefined", context=MockMessage(channel=MockChannel()))
    
    assert await receive_command(mock_command)
    assert mock_command.response.startswith("✗")
    assert "`undefined`" in mock_command.response
    assert mock_command.response_embed.fields[0].name == help_embed("filters").fields[0].name
    assert mock_command.response_embed.fields[0].value == help_embed("filters").fields[0].value
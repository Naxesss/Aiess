import sys
sys.path.append('..')

import pytest

from bot.tests.commands.mock_command import MockCommand, MockMessage, MockChannel
from bot.cmd_modules import cmd_help
from bot.receiver import receive_command
from bot.prefixes import DEFAULT_PREFIX
from bot.commands import register
from bot.commands import help_embed, general_help_embed

def setup_module():
    register(
        category      = "category",
        names         = ["name", "alias"],
        required_args = ["required"],
        optional_args = ["optional"],
        description   = "description",
        example_args  = ["example1", "example2"]
    )(None)

@pytest.mark.asyncio
async def test_help():
    mock_command = MockCommand("help", context=MockMessage(channel=MockChannel()))
    
    assert await receive_command(mock_command)
    assert f"`{DEFAULT_PREFIX}help <command>`" in mock_command.response  # Should suggest using this for more details of a specific command.
    assert mock_command.response_embed.fields[0].name == general_help_embed().fields[0].name
    assert mock_command.response_embed.fields[0].value == general_help_embed().fields[0].value

@pytest.mark.asyncio
async def test_help_with_arg():
    mock_command = MockCommand("help", "name", context=MockMessage(channel=MockChannel()))
    
    assert await receive_command(mock_command)
    assert f"`{DEFAULT_PREFIX}help`" in mock_command.response  # Should suggest using this for a list of commands.
    assert mock_command.response_embed.fields[0].name == help_embed("name").fields[0].name
    assert mock_command.response_embed.fields[0].value == help_embed("name").fields[0].value

@pytest.mark.asyncio
async def test_help_unrecognized_command():
    mock_command = MockCommand("help", "undefined", context=MockMessage(channel=MockChannel()))
    
    assert await receive_command(mock_command)
    assert mock_command.response.startswith("✗")
    assert "`undefined`" in mock_command.response
    assert mock_command.response_embed.fields[0].name == help_embed("help").fields[0].name
    assert mock_command.response_embed.fields[0].value == help_embed("help").fields[0].value
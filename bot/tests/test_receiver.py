import sys
sys.path.append('..')

import pytest

from bot.tests.commands.mock_command import MockMessage, MockChannel
from bot.commands import Command, FunctionWrapper
from bot.commands import registered_commands

from bot.receiver import parse_command
from bot.receiver import receive
from bot.receiver import receive_command
from bot.receiver import parse_args

def setup_module():
    wrapper = FunctionWrapper(
        name    = "test",
        execute = lambda command: command.respond("hi")
    )
    registered_commands["test"] = wrapper

def test_find_command():
    assert parse_command("+test") == Command("test")
    assert parse_command("+test 123") == Command("test", "123")
    assert parse_command("+test 1 2 3") == Command("test", "1", "2", "3")
    assert not parse_command("123")
    assert not parse_command("+ test")
    assert not parse_command("++test")
    assert not parse_command("123 +test")

@pytest.mark.asyncio
async def test_receive():
    mock_channel = MockChannel()
    mock_message = MockMessage("+test", channel=mock_channel)
    await receive(mock_message, client=None)
    assert mock_channel.messages[0].content == "hi"

@pytest.mark.asyncio
async def test_receive_command():
    mock_channel = MockChannel()
    mock_message = MockMessage("+test", channel=mock_channel)
    assert await receive_command(Command("test", context=mock_message))
    assert mock_channel.messages[0].content == "hi"

@pytest.mark.asyncio
async def test_receive_command_unrecognized():
    assert not await receive_command(Command("undefined"))

def test_parse_args():
    assert parse_args(["well", "hello", "there"], 2) == ["well", "hello there"]
import sys
sys.path.append('..')

import pytest

from bot.tests.commands.mock_command import MockMessage, MockChannel, MockGuild, MockClient, MockUser
from bot.commands import Command
from bot.commands import register
from bot.prefixes import set_prefix

from bot.receiver import parse_command
from bot.receiver import receive
from bot.receiver import receive_command
from bot.receiver import parse_args

async def greet(command: Command, name: str, comment: str=None) -> None:
    await command.respond(f"hi {name}" + (f", {comment}" if comment else ""))

def setup_module():
    register(
        category      = "category",
        names         = ["test", "alias"]
    )(lambda command: command.respond("hi"))
    register(
        category      = "category",
        names         = ["greet"],
        required_args = ["name"],
        optional_args = ["comment"]
    )(greet)

def test_parse_command():
    assert parse_command("+test") == Command("test")
    assert parse_command("+test 123") == Command("test", "123")
    assert parse_command("+test 1 2 3") == Command("test", "1", "2", "3")
    assert not parse_command("123")
    assert not parse_command("+ test")
    assert not parse_command("++test")
    assert not parse_command("123 +test")

def test_parse_command_quotes():
    assert parse_command("+test \"123\"") == Command("test", "123")
    assert parse_command("+test \"1 2\" \"3 4 5\"") == Command("test", "1 2", "3 4 5")

def test_parse_command_nested_quotes():
    assert parse_command("+test \"nested \"quotes\"\"") == Command("test", "nested \"quotes\"")

def test_parse_command_custom_prefix():
    context = MockMessage(channel=MockChannel(guild=MockGuild(_id=3)))
    set_prefix(guild_id=3, prefix="&")

    assert not parse_command("+test", context=context)
    assert parse_command("&test", context=context) == Command("test", context=context)
    assert parse_command("&test 123", context=context) == Command("test", "123", context=context)
    assert parse_command("&test 1 2 3", context=context) == Command("test", "1", "2", "3", context=context)
    assert not parse_command("123", context=context)
    assert not parse_command("& test", context=context)
    assert not parse_command("&&test", context=context)
    assert not parse_command("123 &test", context=context)

@pytest.mark.asyncio
async def test_receive():
    mock_channel = MockChannel()
    mock_message = MockMessage("+test", channel=mock_channel)
    await receive(mock_message, client=MockClient())
    assert mock_channel.messages[0].content == "hi"

@pytest.mark.asyncio
async def test_receive_command():
    mock_channel = MockChannel()
    mock_message = MockMessage("+test", channel=mock_channel)
    assert await receive_command(Command("test", context=mock_message))
    assert mock_channel.typing_triggered
    assert mock_channel.messages[0].content == "hi"

@pytest.mark.asyncio
async def test_receive_command_alias():
    mock_channel = MockChannel()
    mock_message = MockMessage("+alias", channel=mock_channel)
    assert await receive_command(Command("alias", context=mock_message))
    assert mock_channel.typing_triggered
    assert mock_channel.messages[0].content == "hi"

@pytest.mark.asyncio
async def test_receive_command_unrecognized():
    assert not await receive_command(Command("undefined"))

@pytest.mark.asyncio
async def test_receive_command_missing_arg():
    mock_channel = MockChannel()
    mock_message = MockMessage("+greet", channel=mock_channel)

    assert not await receive_command(Command("greet", context=mock_message))
    assert mock_channel.messages[0].content.startswith("✗")
    assert "missing required argument" in mock_channel.messages[0].content.lower()
    assert "`<name>`" in mock_channel.messages[0].content.lower()

@pytest.mark.asyncio
async def test_receive_command_without_optional_arg():
    mock_channel = MockChannel()
    mock_message = MockMessage("+greet someone", channel=mock_channel)

    assert await receive_command(Command("greet", "someone", context=mock_message))
    assert mock_channel.messages[0].content == "hi someone"

@pytest.mark.asyncio
async def test_receive_command_with_optional_arg():
    mock_channel = MockChannel()
    mock_message = MockMessage("+greet someone how are you doing?", channel=mock_channel)

    assert await receive_command(Command("greet", "someone", "how are you doing?", context=mock_message))
    assert mock_channel.messages[0].content == "hi someone, how are you doing?"

@pytest.mark.asyncio
async def test_receive_command_lacking_permission():
    mock_channel = MockChannel(guild=MockGuild(_id=3))
    mock_message = MockMessage("+test", channel=mock_channel, author=MockUser(is_admin=False))

    assert not await receive_command(Command("test", context=mock_message))
    assert mock_channel.typing_triggered
    assert "✗ lacking permission" in mock_channel.messages[0].content.lower()

def test_parse_args():
    assert parse_args(["well", "hello", "there"], 2) == ["well", "hello there"]
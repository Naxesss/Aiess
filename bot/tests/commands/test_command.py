import sys
sys.path.append('..')

import pytest

from discord import Embed
from discord import Forbidden, HTTPException

from bot.tests.commands.mock_command import MockChannel, MockMessage, MockErrorChannel, MockResponse

from bot.commands import COMMAND_PREFIX
from bot.commands import registered_commands
from bot.commands import Command, FunctionWrapper
from bot.commands import help_embed, general_help_embed

def test_init_command():
    command = Command("test", "1", "2", "3")
    assert command.name == "test"
    assert command.args == ["1", "2", "3"]

def test_init_command_no_args():
    command = Command("test")
    assert command.name == "test"
    assert not command.args

def test_eq_command_string():
    command = Command("test")
    assert not command == "some string"

def test_hash_command():
    command = Command("test")
    assert command.__hash__()

def test_str_command():
    command = Command("test", "1", "2", "3")
    assert str(command) == f"{COMMAND_PREFIX}test 1 2 3"

def test_str_wrapper():
    wrapper = FunctionWrapper(name="test", execute=None, required_args=["one", "two"], optional_args=["three"])
    assert str(wrapper) == f"`{COMMAND_PREFIX}test <one> <two> [three]`"



@pytest.mark.asyncio
async def test_command_respond():
    mock_channel = MockChannel()
    mock_message = MockMessage("+test 1 2 3", channel=mock_channel)
    command = Command("test", "1", "2", "3", context=mock_message)

    assert await command.respond("success")
    assert command.response == "success"
    assert command.response_embed is None
    assert mock_channel.messages[0].content == "success"
    assert mock_channel.messages[0].embed is None

@pytest.mark.asyncio
async def test_command_respond_embed():
    mock_channel = MockChannel()
    mock_message = MockMessage("+test 1 2 3", channel=mock_channel)
    command = Command("test", "1", "2", "3", context=mock_message)

    embed = Embed()
    embed.add_field(name="test", value="success")

    assert await command.respond("", embed=embed)
    assert command.response == ""
    assert command.response_embed == embed
    assert mock_channel.messages[0].content == ""
    assert mock_channel.messages[0].embed == embed

@pytest.mark.asyncio
async def test_command_respond_err():
    wrapper = FunctionWrapper(
        name="test", execute=None, required_args=["one", "two"], optional_args=["three"],
        description="A command that uses `<one>`, `<two>`, and `[three]` to do stuff.",
        example_args=["one two", "1 2 3", "\"o n e\" two three"])
    registered_commands["test"] = wrapper
    embed = help_embed("test")

    mock_channel = MockChannel()
    mock_message = MockMessage("+test 1 2 3", channel=mock_channel)
    command = Command("test", "1", "2", "3", context=mock_message)

    assert await command.respond_err("error")
    assert command.response == "✗ error"
    assert command.response_embed.fields[0].name == embed.fields[0].name
    assert command.response_embed.fields[0].value == embed.fields[0].value

@pytest.mark.asyncio
async def test_command_respond_forbidden():
    mock_error = Forbidden(MockResponse(status=403, reason="forbidden"), "lacking permissions")
    mock_channel = MockErrorChannel(raise_on_send=mock_error)
    mock_message = MockMessage("+test 1 2 3", channel=mock_channel)
    command = Command("test", "1", "2", "3", context=mock_message)

    assert not await command.respond("e.g. lacking send message permissions in the channel")
    assert command.response is None
    assert command.response_embed is None
    assert not mock_channel.messages

@pytest.mark.asyncio
async def test_command_respond_httpexception():
    mock_error = HTTPException(MockResponse(status=404, reason="not found"), "e.g. some channel doesn't exist")
    mock_channel = MockErrorChannel(raise_on_send=mock_error)
    mock_message = MockMessage("+test 1 2 3", channel=mock_channel)
    command = Command("test", "1", "2", "3", context=mock_message)

    assert not await command.respond("e.g. API did not respond with 200: OK")
    assert command.response is None
    assert command.response_embed is None
    assert not mock_channel.messages



def test_help_embed():
    wrapper = FunctionWrapper(
        name="test", execute=None, required_args=["one", "two"], optional_args=["three"],
        description="A command that uses `<one>`, `<two>`, and `[three]` to do stuff.",
        example_args=["one two", "1 2 3", "\"o n e\" two three"])
    registered_commands["test"] = wrapper
    embed = help_embed("test")

    assert embed
    assert embed.fields
    assert embed.fields[0].name == f"**`{COMMAND_PREFIX}test <one> <two> [three]`**"
    assert wrapper.description in embed.fields[0].value
    for example_args in wrapper.example_args:
        assert f"`{COMMAND_PREFIX}test {example_args}`" in embed.fields[1].value

def test_help_embed_unrecognized_arg():
    assert not help_embed("unrecognized")

def test_command_help_embed():
    wrapper = FunctionWrapper(
        name="test", execute=None, required_args=["one", "two"], optional_args=["three"],
        description="A command that uses `<one>`, `<two>`, and `[three]` to do stuff.",
        example_args=["one two", "1 2 3", "\"o n e\" two three"])
    registered_commands["test"] = wrapper

    embed1 = Command("test").help_embed()
    embed2 = help_embed("test")

    assert embed1.fields[0].name == embed2.fields[0].name
    assert embed1.fields[0].value == embed2.fields[0].value

def test_general_help_embed():
    wrapper = FunctionWrapper(
        name="test", execute=None, required_args=["one", "two"], optional_args=["three"],
        description="A command that uses `<one>`, `<two>`, and `[three]` to do stuff.",
        example_args=["one two", "1 2 3", "\"o n e\" two three"])
    registered_commands["test"] = wrapper
    registered_commands["test2"] = FunctionWrapper(name="test2", execute=None)
    embed = general_help_embed()

    assert embed
    assert embed.fields
    assert "Commands" in embed.fields[0].name
    assert "<>" in embed.fields[0].value  # Should show what these denote; required/optional args.
    assert "[]" in embed.fields[0].value
    assert f"**`{COMMAND_PREFIX}test <one> <two> [three]`**\u2000**`{COMMAND_PREFIX}test2`**" in embed.fields[0].value
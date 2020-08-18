import sys
sys.path.append('..')

import pytest

from discord import Embed
from discord import Forbidden, HTTPException

from bot.tests.commands.mock_command import MockChannel, MockDMChannel, MockGuild, MockMessage, MockErrorChannel, MockResponse

from bot.prefixes import DEFAULT_PREFIX
from bot.prefixes import set_prefix
from bot.commands import register, registered_commands, registered_categories
from bot.commands import Command, FunctionWrapper
from bot.commands import get_wrapper, help_embed, general_help_embed

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
    assert str(command) == f"{DEFAULT_PREFIX}test 1 2 3"

def test_str_wrapper():
    wrapper = FunctionWrapper(category=None, names=["test"], execute=None, required_args=["one", "two"], optional_args=["three"])
    assert str(wrapper) == "`{0}test <one> <two> [three]`"

def test_prefix_no_context():
    command = Command("test")
    assert command.prefix() == DEFAULT_PREFIX

def test_prefix_no_guild():
    command = Command("test", context=MockMessage(channel=MockDMChannel(_id=6)))
    assert command.prefix() == DEFAULT_PREFIX

def test_prefix_default():
    command = Command("test", context=MockMessage(channel=MockChannel(_id=6, guild=MockGuild(_id=7))))
    assert command.prefix() == DEFAULT_PREFIX

def test_prefix_custom():
    command = Command("test", context=MockMessage(channel=MockChannel(_id=6, guild=MockGuild(_id=7))))

    set_prefix(guild_id=7, prefix="&")
    assert command.prefix() == "&"

    set_prefix(guild_id=7, prefix=None)
    assert command.prefix() == DEFAULT_PREFIX

def test_guild_id():
    command = Command("test", context=MockMessage(channel=MockChannel(_id=6, guild=MockGuild(_id=7))))
    assert command.guild_id() == 7

def test_guild_id_dm_channel():
    command = Command("test", context=MockMessage(channel=MockDMChannel()))
    assert command.guild_id() is None



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
async def test_command_respond_mention_everyone():
    command = Command("test", context=MockMessage(channel=MockChannel()))

    assert await command.respond("@everyone")
    assert command.response == "@\u200beveryone"

@pytest.mark.asyncio
async def test_command_respond_mention_user():
    command = Command("test", context=MockMessage(channel=MockChannel()))

    assert await command.respond("<@51289736123>")
    assert command.response == "<@\u200b51289736123>"

@pytest.mark.asyncio
async def test_command_respond_mention_role():
    command = Command("test", context=MockMessage(channel=MockChannel()))

    assert await command.respond("<@&51289736123>")
    assert command.response == "<@\u200b&51289736123>"

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
    register(
        category="Some Category", names=["test"], required_args=["one", "two"], optional_args=["three"],
        description="A command that uses `<one>`, `<two>`, and `[three]` to do stuff.",
        example_args=["one two", "1 2 3", "\"o n e\" two three"]
    )(None)
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
    
    with pytest.raises(HTTPException):
        await command.respond("e.g. API did not respond with 200: OK")
    
    assert command.response is None
    assert command.response_embed is None
    assert not mock_channel.messages



def test_get_wrapper():
    register(
        category="Some Category", names=["test", "alias"], required_args=["one", "two"], optional_args=["three"],
        description="A command that uses `<one>`, `<two>`, and `[three]` to do stuff.",
        example_args=["one two", "1 2 3", "\"o n e\" two three"]
    )(None)

    assert get_wrapper("test") == registered_commands["test"]
    assert get_wrapper("alias") == registered_commands["test"]

def test_get_wrapper_unrecognized():
    assert not get_wrapper("unrecognized")

def test_help_embed():
    register(
        category="Some Category", names=["test"], required_args=["one", "two"], optional_args=["three"],
        description="A command that uses `<one>`, `<two>`, and `[three]` to do stuff.",
        example_args=["one two", "1 2 3", "\"o n e\" two three"]
    )(None)
    embed = help_embed("test")

    assert embed
    assert embed.fields
    assert embed.fields[0].name == f"**`{DEFAULT_PREFIX}test <one> <two> [three]`**"
    assert "A command that uses `<one>`, `<two>`, and `[three]` to do stuff." in embed.fields[0].value
    for example_args in ["one two", "1 2 3", "\"o n e\" two three"]:
        assert f"`{DEFAULT_PREFIX}test {example_args}`" in embed.fields[1].value

def test_help_embed_custom_prefix():
    register(
        category="Some Category", names=["test"], required_args=["one", "two"], optional_args=["three"],
        description="A command that uses `<one>`, `<two>`, and `[three]` to do stuff.",
        example_args=["one two", "1 2 3", "\"o n e\" two three"]
    )(None)
    embed = help_embed("test", prefix="&")

    assert embed.fields[0].name == "**`&test <one> <two> [three]`**"
    assert "A command that uses `<one>`, `<two>`, and `[three]` to do stuff." in embed.fields[0].value
    for example_args in ["one two", "1 2 3", "\"o n e\" two three"]:
        assert f"`&test {example_args}`" in embed.fields[1].value

def test_help_embed_unrecognized_arg():
    assert not help_embed("unrecognized")

def test_command_help_embed():
    register(
        category="Some Category", names=["test"], required_args=["one", "two"], optional_args=["three"],
        description="A command that uses `<one>`, `<two>`, and `[three]` to do stuff.",
        example_args=["one two", "1 2 3", "\"o n e\" two three"]
    )(None)

    embed1 = Command("test").help_embed()
    embed2 = help_embed("test")

    assert embed1.fields[0].name == embed2.fields[0].name
    assert embed1.fields[0].value == embed2.fields[0].value

def test_general_help_embed():
    registered_commands.clear()
    registered_categories.clear()

    register(
        category="A Test Category", names=["test", "alias"], required_args=["one", "two"], optional_args=["three"],
        description="A command that uses `<one>`, `<two>`, and `[three]` to do stuff.",
        example_args=["one two", "1 2 3", "\"o n e\" two three"]
    )(None)
    register(category="Other Test Category", names=["test2"])(None)
    
    embed = general_help_embed()

    assert embed
    assert "Commands" in embed.title
    assert "/" in embed.description  # Should explain that this denotes aliases.
    assert "<>" in embed.description  # Should explain that these two denote required/optional args.
    assert "[]" in embed.description
    assert embed.fields
    assert embed.fields[0].name == "A Test Category"
    assert embed.fields[1].name == "Other Test Category"
    assert f"**`{DEFAULT_PREFIX}test/{DEFAULT_PREFIX}alias <one> <two> [three]`**" in embed.fields[0].value
    assert f"**`{DEFAULT_PREFIX}test2`**" in embed.fields[1].value

def test_general_help_embed_custom_prefix():
    registered_commands.clear()
    registered_categories.clear()

    register(
        category="A Test Category", names=["test", "alias"], required_args=["one", "two"], optional_args=["three"],
        description="A command that uses `<one>`, `<two>`, and `[three]` to do stuff.",
        example_args=["one two", "1 2 3", "\"o n e\" two three"]
    )(None)
    register(category="Other Test Category", names=["test2"])(None)
    
    embed = general_help_embed(prefix="&")

    assert "**`&test/&alias <one> <two> [three]`**" in embed.fields[0].value
    assert "**`&test2`**" in embed.fields[1].value
import sys
sys.path.append('..')

import mock
from typing import List

from discord import Embed

from bot.commands import Command

class MockGuild():
    """Represents a guild (i.e. the parent of channels)."""
    def __init__(self, _id: int=None):
        self.id = int(_id) if _id is not None else None

class MockDMChannel():
    """Represents a DM channel (e.g. in which a message was sent).
    Unlike regular channels, DM channels do not contain a guild attribute."""
    def __init__(self, _id: int=None):
        self.id = int(_id) if _id is not None else None
        self.messages = []
        self.typing_triggered = False
    
    async def trigger_typing(self):
        self.typing_triggered = True
    
    async def send(self, content, embed: Embed=None):
        self.messages.append(
            MockMessage(
                content = content,
                channel = self,
                author  = MockUser(_id=0, name="Aiess"),
                embed   = embed
            )
        )

class MockChannel(MockDMChannel):
    """Represents a guild channel (e.g. in which a message was sent)."""
    def __init__(self, _id: int=None, guild: MockGuild=None):
        super().__init__(_id)
        self.guild = guild

class MockResponse():
    """Represents an http response object (e.g. the 403 response given when a Forbidden error occurs)."""
    def __init__(self, status: int, reason: str):
        self.status = status
        self.reason = reason

class MockErrorChannel(MockChannel):
    """Represents a guild channel (e.g. in which a message was sent)."""
    def __init__(self, raise_on_send: Exception, _id: int=None, guild: MockGuild=None):
        super().__init__(_id, guild)
        self.raise_on_send = raise_on_send

    async def send(self, content, embed: Embed=None):
        raise self.raise_on_send

class MockRole():
    """Represents a role (e.g. role of the user sending a message)."""
    def __init__(self, _id: int=None):
        self.id = int(_id) if _id is not None else None

class MockUser():
    """Represents a user (e.g. an author of a sent message)."""
    def __init__(self, _id: int=None, name: str=None, roles: List[MockRole]=[], is_admin: bool=True, is_dm: bool=False):
        self.id = int(_id) if _id is not None else None
        self.name = name
        self.roles = roles
        if not is_dm:
            self.guild_permissions = mock.MagicMock()
            self.guild_permissions.administrator = is_admin

class MockClient():
    """Represents a bot client instance."""
    def __init__(self, user: MockUser=None, latency: float=0):
        self.user = user if user else MockUser()
        self.latency = latency

class MockMessage():
    """Represents the message instance (e.g. from which a command was called). Contains
    the channel from where it was sent, as well as by whom."""
    def __init__(self, content: str=None, channel: MockChannel=None, author: MockUser=None, embed: Embed=None):
        self.content = str(content) if content is not None else None
        self.channel = channel if channel else MockChannel()
        self.guild = channel.guild if channel is not None and hasattr(channel, "guild") else None
        self.author = author if author else MockUser()
        self.embed = embed

class MockCommand(Command):
    """Represents the values with which a command is called (i.e. name, args, context),
    as well as the response from the command, if any."""
    def __init__(self, name: str, *args: str, context: MockMessage, client: MockClient=None):
        super().__init__(name, *args, context=context, client=client)
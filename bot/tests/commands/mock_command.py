import sys
sys.path.append('..')

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
    
    async def send(self, content, embed: Embed=None):
        self.messages.append(
            MockMessage(
                content=content,
                channel=self,
                user   =MockUser(_id=0, name="Aiess"),
                embed  =embed))

class MockChannel(MockDMChannel):
    """Represents a guild channel (e.g. in which a message was sent)."""
    def __init__(self, _id: int=None, guild: MockGuild=None):
        super().__init__(_id)
        self.guild = guild

class MockUser():
    """Represents a user (e.g. an author of a sent message)."""
    def __init__(self, _id: int=None, name: str=None):
        self.id = int(_id) if _id is not None else None
        self.name = name

class MockMessage():
    """Represents the message instance (e.g. from which a command was called). Contains
    the channel from where it was sent, as well as by whom."""
    def __init__(self, content: str=None, channel: MockChannel=None, user: MockUser=None, embed: Embed=None):
        self.content = str(content) if content is not None else None
        self.channel = channel
        self.user = user
        self.embed = embed

class MockCommand(Command):
    """Represents the values with which a command is called (i.e. name, args, context),
    as well as the response from the command, if any."""
    def __init__(self, name: str, *args: str, context: MockMessage):
        super().__init__(name, *args, context=context)
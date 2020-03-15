from commands import Command

class MockGuild():
    def __init__(self, _id: int):
        self.id = _id

class MockChannel():
    def __init__(self, _id: int, guild: MockGuild):
        self.id = _id
        self.guild = guild
        self.message = None

    def send(self, content: str):
        self.message.channel.command.response = content

class MockMessage():
    def __init__(self, channel: MockChannel):
        self.channel = channel
        self.command = None

class MockCommand(Command):
    """Represents the values with which a command is called (i.e. name, args, context),
    as well as output from the command (e.g. response)."""
    def __init__(self, name: str, *args: str, context: MockMessage=None):
        if context: context.command = self
        super().__init__(name, *args, context=context)

        self.response = None

    async def respond(self, response: str) -> bool:
        """A mocked version of response, always returns true.
        Sets the response attribute to the given response for checking."""
        self.response = response
        return True
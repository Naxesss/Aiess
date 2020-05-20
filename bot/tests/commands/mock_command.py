import sys
sys.path.append('..')

from bot.commands import Command

class MockCommand(Command):
    """Represents the values with which a command is called (i.e. name, args, context),
    as well as output from the command (e.g. response)."""
    def __init__(self, name: str, *args: str):
        super().__init__(name, *args)

        self.response = None

    async def respond(self, response: str) -> bool:
        """A mocked version of response, always returns true.
        Sets the response attribute to the given response for checking."""
        self.response = response
        return True
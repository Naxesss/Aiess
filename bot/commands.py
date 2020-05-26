import sys
sys.path.append('..')

from collections import defaultdict
from typing import Callable, TypeVar

from discord import Message
from discord import Forbidden, HTTPException

class Command():
    """Represents the values with which a command is called (i.e. name, args, context)."""
    def __init__(self, name: str, *args: str, context: Message=None):
        self.name = name
        self.args = [arg for arg in args]
        self.context = context
    
    def __str__(self) -> str:
        args = [f" {arg}" for arg in self.args]
        return f"+{self.name}{args}"
    
    def __key(self) -> tuple:
        return (
            self.name,
            self.args,
            self.context
        )
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Command):
            return False
        return self.__key() == other.__key()
    
    def __hash__(self) -> str:
        return hash(self.__key())
    
    async def respond(self, response: str) -> bool:
        """Returns whether a response was successfully sent."""
        if not self.context:
            return False  # I.e. called from test modules.
        
        try:
            await self.context.channel.send(response)
            return True
        except Forbidden:
            print(f"Lacking permissions to write \"{response}\" in {self.context.channel}.")
        except HTTPException:
            print(f"Unable to send \"{response}\" in {self.context.channel} due to connection issues.")
        
        return False

registered_commands = defaultdict()

T = TypeVar("T")
def register(name: str) -> Callable[[Callable[..., T]], T]:
    """A decorator which registers the respective function as a command
    able to be executed by the given name (e.g. "ping" in "+ping")."""

    def wrapper(func: Callable[..., T]) -> T:
        registered_commands[name] = func
        return func
    
    return wrapper
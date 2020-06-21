import sys
sys.path.append('..')

from collections import defaultdict
from typing import Callable, TypeVar, List

from discord import Message, Embed
from discord import Forbidden, HTTPException

class Command():
    """Represents the values with which a command is called (i.e. name, args, context),
    as well as the response from the command, if any."""
    def __init__(self, name: str, *args: str, context: Message=None):
        self.name = name
        self.args = [arg for arg in args]
        self.context = context
        
        self.response = None
        self.response_embed = None
    
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
    
    async def respond(self, response: str, embed: Embed=None) -> bool:
        """Returns whether a response was successfully sent."""
        try:
            await self.context.channel.send(response, embed=embed)
            self.response = response
            self.response_embed = embed
            return True
        except Forbidden:
            print(f"Lacking permissions to write \"{response}\" in {self.context.channel}.")
        except HTTPException:
            print(f"Unable to send \"{response}\" in {self.context.channel} due to connection issues.")
        
        return False

class FunctionWrapper():
    """Represents a command function, its required and/or optional arguments, if any,
    as well as information about the command (e.g. name, description, and example args)."""
    def __init__(
            self, name: str, execute: Callable,
            required_args: List[str]=[], optional_args: List[str]=[],
            description: str=None, example_args: List[str]=[]):
        self.name = name
        self.execute = execute
        self.required_args = required_args
        self.optional_args = optional_args
        self.description = description
        self.example_args = example_args

registered_commands = defaultdict(FunctionWrapper)

T = TypeVar("T")
def register(
        name: str, required_args: List[str]=[], optional_args: List[str]=[],
        description: str=None, example_args: List[str]=[]) -> Callable[[Callable[..., T]], T]:
    """A decorator which registers the respective function as a command
    able to be executed by the given name (e.g. "ping" in "+ping"), optionally
    with required and/or optional arguments as well."""

    def wrapper(execute: Callable[..., T]) -> T:
        registered_commands[name] = FunctionWrapper(name, execute, required_args, optional_args)
        return execute
    
    return wrapper
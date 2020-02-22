from collections import defaultdict
from typing import Callable, TypeVar

from discord import Message

class Command():
    """Represents the values with which a command is called (i.e. name, args, context)."""
    def __init__(self, name: str, *args: str, context: Message=None):
        self.name = name
        self.args = [arg for arg in args]
        self.context = context
    
    def __str__(self) -> str:
        args = [f" {arg}" for arg in self.args]
        return f"+{self.name}{args}"
    
    def __eq__(self, other) -> bool:
        if type(self) != type(other):
            return False
        return (
            self.name == other.name and
            self.args == other.args
        )
registered_commands = defaultdict()

T = TypeVar("T")
def register(name: str) -> Callable[[Callable[..., T]], T]:
    """A decorator which registers the respective function as a command
    able to be executed by the given name (e.g. "ping" in "+ping")."""

    def wrapper(func: Callable[..., T]) -> T:
        registered_commands[name] = func
        return func
    
    return wrapper

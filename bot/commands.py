import sys
sys.path.append('..')

from collections import defaultdict
from typing import Callable, TypeVar, List

from discord import Message, Embed, Client
from discord import Forbidden, HTTPException

COMMAND_PREFIX = "+"

class Command():
    """Represents the values with which a command is called (i.e. name, args, context),
    as well as the response from the command, if any."""
    def __init__(self, name: str, *args: str, context: Message=None, client: Client=None):
        self.name = name
        self.args = [arg for arg in args]
        self.context = context
        self.client = client
        
        self.response = None
        self.response_embed = None
    
    def __str__(self) -> str:
        args = "".join(f" {arg}" for arg in self.args)
        return f"{COMMAND_PREFIX}{self.name}{args}"
    
    def __key(self) -> tuple:
        return (
            self.name,
            tuple(self.args),
            self.context
        )
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Command):
            return False
        return self.__key() == other.__key()
    
    def __hash__(self) -> str:
        return hash(self.__key())
    
    def help_embed(self) -> Embed:
        """Returns an embed explaining how this command is used."""
        return help_embed(self.name)
    
    async def respond(self, response: str, embed: Embed=None) -> bool:
        """Sends a message in the channel where the command was called, with the given response text and embed, if any.
        Handles Forbidden and HTTPException errors by logging. Returns whether a response was successfully sent."""
        try:
            await self.context.channel.send(response, embed=embed)
            self.response = response
            self.response_embed = embed
            return True
        except Forbidden:
            print(f"Lacking permissions to write \"{response}\" in {self.context.channel}.")
        
        return False

    async def respond_err(self, response: str) -> bool:
        """Sends \"✗ `response`\", with a help embed attached, in the channel where the command was called. The
        help embed explains how the command is used. Handles Forbidden and HTTPException errors by logging.
        Returns whether a response was successfully sent."""
        return await self.respond(f"✗ {response}", embed=help_embed(self.name))

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
    
    def __str__(self):
        required_args_str = (" " + " ".join(map(lambda arg: f"<{arg}>", self.required_args))) if self.required_args else ""
        optional_args_str = (" " + " ".join(map(lambda arg: f"[{arg}]", self.optional_args))) if self.optional_args else ""
        return f"`{COMMAND_PREFIX}{self.name}{required_args_str}{optional_args_str}`"

registered_commands = defaultdict(FunctionWrapper)

T = TypeVar("T")
def register(
        name: str, required_args: List[str]=[], optional_args: List[str]=[],
        description: str=None, example_args: List[str]=[]) -> Callable[[Callable[..., T]], T]:
    """A decorator which registers the respective function as a command
    able to be executed by the given name (e.g. "ping" in "+ping"), optionally
    with required and/or optional arguments as well."""

    def wrapper(execute: Callable[..., T]) -> T:
        registered_commands[name] = FunctionWrapper(
            name, execute, required_args, optional_args, description, example_args
        )
        return execute
    
    return wrapper

def help_embed(name: str) -> Embed:
    """Returns an embed explaining how to use the command with the given name.
    Includes e.g. arguments, description, and examples."""
    name = name.lower()
    if name not in registered_commands:
        return None
    
    wrapper = registered_commands[name]

    embed = Embed()
    embed.add_field(
        name   = f"**{str(wrapper)}**",
        value  = wrapper.description,
        inline = True
    )
    if wrapper.example_args:
        embed.add_field(
            name   = "Example(s)",
            value  = "\r\n".join(f"∙ `{COMMAND_PREFIX}{name}" + (f" {args}" if args else "") + "`" for args in wrapper.example_args),
            inline = True
        )

    return embed

def general_help_embed() -> Embed:
    """Returns an embed showing a list of all registered commands."""
    embed = Embed()
    embed.add_field(
        name   = f"Commands",
        value  =
            "<> denotes required arguments. [] denotes optional arguments.\r\n\r\n" +
            "\u2000".join(f"**{str(registered_commands[name])}**" for name in registered_commands),
        inline = True
    )
    return embed
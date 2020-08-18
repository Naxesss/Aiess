import sys
sys.path.append('..')

from collections import defaultdict
from typing import Callable, TypeVar, List

from discord import Message, Embed, Client
from discord import Forbidden

from aiess.logger import log_err

from bot.formatter import format_dotted_list
from bot.prefixes import get_prefix
from bot.prefixes import DEFAULT_PREFIX

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
        return f"{self.prefix()}{self.name}{args}"
    
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
        return help_embed(self.name, self.prefix())
    
    def guild_id(self) -> bool:
        """Returns the id of the guild where the command was called, if any, otherwise None (e.g. DMChannel)."""
        return self.context.guild.id if self.context and hasattr(self.context, "guild") and hasattr(self.context.guild, "id") else None

    def prefix(self) -> str:
        """Returns the command prefix that should be used in this context."""
        return get_prefix(self.context)
    
    async def trigger_typing(self) -> None:
        """Triggers typing in the channel where the command was called.
        Disappears after 10 seconds or after a message is sent."""
        await self.context.channel.trigger_typing()

    async def respond(self, response: str, embed: Embed=None) -> bool:
        """Sends a message in the channel where the command was called, with the given response text and embed, if any.
        Handles Forbidden and HTTPException errors by logging. Returns whether a response was successfully sent."""
        # `\u200b` is a zero-width space. This prevents any kind of mention/highlight.
        response = response.replace("@", "@\u200b")
        try:
            await self.context.channel.send(response, embed=embed)
            self.response = response
            self.response_embed = embed
            return True
        except Forbidden:
            log_err(f"Lacking permissions to write \"{response}\" in {self.context.channel}.")
        
        return False

    async def respond_err(self, response: str, embed: Embed=None) -> bool:
        """Sends \"✗ `response`\", with a help embed attached, in the channel where the command was called. The
        help embed explains how the command is used. Can optionally override the help embed with another.
        Handles Forbidden and HTTPException errors by logging. Returns whether a response was successfully sent."""
        embed = self.help_embed() if not embed else embed
        return await self.respond(f"✗ {response}", embed=embed)

class FunctionWrapper():
    """Represents a command function, its required and/or optional arguments, if any,
    as well as information about the command (e.g. name, description, and example args)."""
    def __init__(
            self, category: str, names: str, execute: Callable,
            required_args: List[str]=[], optional_args: List[str]=[],
            description: str=None, example_args: List[str]=[]):
        self.category = category
        self.names = names
        self.execute = execute
        self.required_args = required_args
        self.optional_args = optional_args
        self.description = description
        self.example_args = example_args
    
    def __str__(self):
        names = "/".join(f"{{0}}{name}" for name in self.names)
        required_args_str = (" " + " ".join(map(lambda arg: f"<{arg}>", self.required_args))) if self.required_args else ""
        optional_args_str = (" " + " ".join(map(lambda arg: f"[{arg}]", self.optional_args))) if self.optional_args else ""
        return f"`{names}{required_args_str}{optional_args_str}`"

registered_aliases = defaultdict(str)
registered_commands = defaultdict(FunctionWrapper)
registered_categories = defaultdict(list)

GENERAL_CATEGORY = "General"
EVENTS_CATEGORY = "Events"

T = TypeVar("T")
def register(
        category: str, names: str, required_args: List[str]=[], optional_args: List[str]=[],
        description: str=None, example_args: List[str]=[]) -> Callable[[Callable[..., T]], T]:
    """A decorator which registers the respective function as a command
    able to be executed by the given names (e.g. "ping" in "+ping"), optionally
    with required and/or optional arguments as well."""

    def wrapper(execute: Callable[..., T]) -> T:
        for name in names:
            registered_aliases[name] = names[0]
        registered_categories[category].append(names[0])
        registered_commands[names[0]] = FunctionWrapper(
            category, names, execute, required_args, optional_args, description, example_args
        )
        return execute
    
    return wrapper

def get_wrapper(name: str) -> FunctionWrapper:
    """Returns the command wrapper of the given command name/alias, case insensitive, if any, otherwise None."""
    name = name.lower()
    if name not in registered_aliases:
        return None
    name = registered_aliases[name]
    return registered_commands[name]

def help_embed(name: str, prefix: str=DEFAULT_PREFIX) -> Embed:
    """Returns an embed explaining how to use the command with the given name.
    Includes e.g. arguments, description, and examples."""
    wrapper = get_wrapper(name)
    if not wrapper:
        return None

    embed = Embed()
    embed.add_field(
        name   = f"**{str(wrapper)}**".replace("{0}", prefix),
        value  = wrapper.description.replace("{0}", prefix) if wrapper.description else "Description missing.",
        inline = True
    )
    if wrapper.example_args:
        embed.add_field(
            name   = "Example(s)",
            value  = "\n".join(f"∙ `{prefix}{name}" + (f" {args}" if args else "") + "`" for args in wrapper.example_args),
            inline = True
        )

    return embed

def general_help_embed(prefix: str=DEFAULT_PREFIX) -> Embed:
    """Returns an embed showing a list of all registered commands."""
    embed = Embed()
    embed.title = "Commands"
    embed.description = "`<>` : required args, `[]` : optional args, `/` : aliases."

    for category in registered_categories:
        embed.add_field(
            name   = category,
            value  = format_dotted_list(
                f"**{registered_commands[name]}**".replace("{0}", prefix) for name in registered_categories[category]
            ),
            inline = False
        )
    
    return embed
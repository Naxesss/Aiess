import sys
sys.path.append('..')

import re as regex

from bot.prefixes import DEFAULT_PREFIX
from bot.filterer import FilterContext, Tag

filter_context = FilterContext(
    name     = "Permissions",
    examples = [
        f"**everyone** leave empty OR `role:@@everyone` (two @)",
        f"**admin-only** see `{DEFAULT_PREFIX}disable <command(s)>`",
        "**in #offtopic** `channel:#offtopic`",
        "**from @verified role** `role:@verified`",
        "**from @someone** `user:@someone`",
        "**from @verified role in #offtopic** `role:@verified and channel:#offtopic`",
        "**from @verified role in #offtopic or #bot** `role:@verified and channel:(#offtopic or #bot)`",
        "**from @verified role in #bot, or from @moderators anywhere** `role:@verified and channel:#bot or role:@moderators`"
    ],
    tags     = [
        Tag(
            names           = ["user"],
            description     = "Ensure caller is this user.",
            example_values  = ["@user", "<@user_id>"],
            value_hint      = "Any user mention.",
            value_predicate = lambda value: regex.match(r"<@!?(\d+)>", value) is not None,
            value_func      = lambda message: [f"<@{message.author.id}>", f"<@!{message.author.id}>"] if message.author else None
        ),
        Tag(
            names           = ["channel"],
            description     = "Ensure called in this channel.",
            example_values  = ["#channel", "<#channel_id>"],
            value_hint      = "Any channel mention.",
            value_predicate = lambda value: regex.match(r"<#(\d+)>", value) is not None,
            value_func      = lambda message: [f"<#{message.channel.id}>"] if message.channel else None
        ),
        Tag(
            names           = ["role"],
            description     = "Ensure caller has this role.",
            example_values  = ["@role", "<@&role_id>"],
            value_hint      = "Any role mention.",
            value_predicate = lambda value: regex.match(r"<@&(\d+)>", value) is not None,
            value_func      = lambda message: (
                    [f"<@&{role.id}>" for role in message.author.roles]
                        if message.author and hasattr(message.author, "roles")
                        else None
                )
        )
    ]
)
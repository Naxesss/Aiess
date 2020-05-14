import sys
sys.path.append('..')

from discord import Embed, Colour

from aiess import Event, User, Beatmapset
from aiess import event_types as types

from bot.database import Database

class TypeProps():
    """Represents the properties of how a type should be represented (e.g. emoji, name, colour)."""
    def __init__(self, emoji: str, title: str, colour: Colour, **kwargs):
        self.emoji = emoji
        self.title = title
        self.colour = colour

        self.show_history = False
        self.show_in_history = False
        self.show_context = False
        for key, value in kwargs.items():
            setattr(self, key, value)

colour_ranked     = Colour.from_rgb(255,200,90)
colour_qualified  = Colour.from_rgb(255,75,100)
colour_nominated  = Colour.from_rgb(50,150,255)
colour_discussion = Colour.from_rgb(65,65,65)
colour_resolve    = Colour.from_rgb(100,200,100)
colour_reopen     = Colour.from_rgb(255,160,70)

type_props = {
    types.RANK:               TypeProps(":sparkling_heart:",    "Ranked",           colour_ranked,      show_history=True),
    types.LOVE:               TypeProps(":gift_heart:",         "Loved",            colour_ranked,      show_history=True),

    types.QUALIFY:            TypeProps(":heart:",              "Qualified",        colour_qualified,   show_in_history=True),
    types.DISQUALIFY:         TypeProps(":broken_heart:",       "Disqualified",     colour_qualified,   show_in_history=True),

    types.NOMINATE:           TypeProps(":thought_balloon:",    "Nominated",        colour_nominated,   show_in_history=True),
    types.RESET:              TypeProps(":anger_right:",        "Nomination Reset", colour_nominated,   show_in_history=True),

    types.SUGGESTION:         TypeProps(":yellow_circle:",      "Suggestion",       colour_discussion),
    types.PROBLEM:            TypeProps(":red_circle:",         "Problem",          colour_discussion),
    types.NOTE:               TypeProps(":purple_circle:",      "Note",             colour_discussion),
    types.PRAISE:             TypeProps(":blue_heart:",         "Praise",           colour_discussion),
    types.HYPE:               TypeProps(":blue_circle:",        "Hype",             colour_discussion),
    types.REPLY:              TypeProps(":white_circle:",       "Reply",            colour_discussion,  show_context=True),

    types.RESOLVE:            TypeProps(":green_circle:",       "Resolved",         colour_resolve,     show_context=True),
    types.KUDOSU_GAIN:        TypeProps(":arrow_up:",           "Kudosu Given",     colour_resolve,     show_context=True),
    types.KUDOSU_ALLOW:       TypeProps(":arrow_double_up:",    "Kudosu Allowed",   colour_resolve,     show_context=True),

    types.REOPEN:             TypeProps(":orange_circle:",      "Reopened",         colour_reopen,      show_context=True),
    types.KUDOSU_LOSS:        TypeProps(":arrow_down:",         "Kudosu Removed",   colour_reopen,      show_context=True),
    types.KUDOSU_DENY:        TypeProps(":arrow_double_down:",  "Kudosu Denied",    colour_reopen,      show_context=True),

    types.DISCUSSION_DELETE:  TypeProps(":zap:",                "Deleted",          colour_discussion,  show_context=True),
    types.DISCUSSION_RESTORE: TypeProps(":wrench:",             "Restored",         colour_discussion,  show_context=True),
    types.REPLY_DELETE:       TypeProps(":zap:",                "Reply Deleted",    colour_discussion,  show_context=True),
    types.REPLY_RESTORE:      TypeProps(":wrench:",             "Reply Restored",   colour_discussion,  show_context=True)
}

def format_link(event: Event) -> str:
    """Returns a link which leads to the source of the given event
    (e.g. the discussion of a suggestion, or the beatmapset of a nomination)."""
    if event.discussion and event.discussion.beatmapset:
        return f"https://osu.ppy.sh/beatmapsets/{event.discussion.beatmapset.id}/discussion#/{event.discussion.id}"
    
    if event.beatmapset:
        return f"https://osu.ppy.sh/beatmapsets/{event.beatmapset.id}"
    
    raise ValueError("Cannot format a link of an event missing a beatmapset.")

def format_embed(event: Event) -> str:
    """Returns an embed which represents the given event."""
    embed = Embed()
    embed.add_field(name=format_field_name(event), value=format_field_value(event), inline=False)
    embed.set_footer(text=format_footer_text(event), icon_url=format_footer_icon_url(event))
    embed.colour = type_props[event.type].colour
    embed.set_thumbnail(url=format_thumbnail_url(event))

    if type_props[event.type].show_context and event.discussion:
        embed.add_field(name=format_context_field_name(event), value=format_context_field_value(event))

    return embed



def escape_markdown(obj: str) -> str:
    """Returns the given object cast to string, and where all markdown
    markers (e.g. '*', '_', and '~' characters) are escaped using backslash."""
    return (str(obj)
        .replace("*", "\\*")   # Italic / Bold
        .replace("_", "\\_")   # Italic / Underline
        .replace("~", "\\~")   # Strikethrough
        .replace("`", "\\`"))  # Code / Code Block

def format_field_name(event: Event) -> str:
    """Returns the embed title of the given event (e.g. :heart: Qualified)."""
    return f"{type_props[event.type].emoji} {type_props[event.type].title}"

def format_field_value(event: Event) -> str:
    """Returns the embed contents of the given event (i.e. the \"artist - title, mapped by creator [modes]\" part)."""
    artist_title_str = escape_markdown(f"{event.beatmapset.artist} - {event.beatmapset.title}")
    creator_str = escape_markdown(event.beatmapset.creator)

    beatmap_str = f"[**{artist_title_str}**](https://osu.ppy.sh/beatmapsets/{event.beatmapset.id})"
    mapped_by_str = f"Mapped by [{creator_str}](https://osu.ppy.sh/users/{event.beatmapset.creator.id})"
    mode_str = event.beatmapset.mode_str().replace("[", "[**").replace("]", "**]")

    result = f"{beatmap_str}\n{mapped_by_str} {mode_str}"

    if type_props[event.type].show_history:
        # Give how much room the function has to work with, allowing it to smartly shorten/truncate if needed.
        # This is to account for the embed field value character limit of 1024.
        result += format_history(event.beatmapset, length_limit=1024-len(result))

    return result

def format_footer_text(event: Event, database: Database=None) -> str:
    """Returns the footer text of the event (e.g. modder \"00:01:318 - fix blanket\"),
    if there's a user associated with the event, otherwise None."""
    if not event.user:
        return Embed.Empty
    
    if not event.content:
        if event.type in [types.NOMINATE, types.QUALIFY]:
            if not database:
                # Allows tests to use test databases instead of the production one.
                database = Database("aiess")
            
            praise_text = format_recent_praise(event.user, event.beatmapset, database)
            if praise_text:
                return f"{event.user} {format_preview(praise_text)}"
        
        return str(event.user)

    return f"{event.user} {format_preview(event.content)}"

def format_preview(content: str, length: int=60, split_newline: bool=True) -> str:
    """Returns a string of the user with the truncated content in quotes, if any,
    else just the user, again if any, otherwise None."""
    if not content:
        return ""
    
    preview = content
    if split_newline:
        preview = content.partition("\n")[0]
    preview = preview if len(preview) <= length else preview[:length-3] + "..."

    # Markdown does not function in footer text; trying to escape it here would lead to visible '\'.
    return f"\"{preview}\""

def format_footer_icon_url(event: Event) -> str:
    """Returns the footer icon url of the event (i.e. the image url of the user's avatar),
    if there's a user associated with the event, otherwise None."""
    if event.user:
        return f"https://a.ppy.sh/{event.user.id}"
    return Embed.Empty

def format_thumbnail_url(event: Event) -> str:
    """Returns the thumbnail url for the event (e.g. beatmapset thumbnail)."""
    return f"https://b.ppy.sh/thumb/{event.beatmapset.id}l.jpg"

def format_context_field_name(event: Event) -> str:
    """Returns the title for the discussion context; the name of the discussion author."""
    return escape_markdown(event.discussion.user)

def format_context_field_value(event: Event) -> str:
    """Returns the content for the discussion context, surrounded in quotes."""
    return f"\"{escape_markdown(event.discussion.content)}\""

def format_history(beatmapset: Beatmapset, length_limit: int=None, database: Database=None) -> str:
    """Returns the nomination history of this beatmapset (i.e. icons and names of actions and their authors).
    Optionally within a certain length, smartly shortening/truncating the contents if needed."""
    if not database: database = Database("aiess")  # Using wrapped database to access events.

    # Sorted by time ascending; newer events first.
    events = list(filter(
        lambda event: type_props[event.type].show_in_history,
        database.retrieve_beatmapset_events(beatmapset)))

    long_history = ""
    for event in events:
        # Some nomination events seem to be missing a user.
        if not event.user:
            if event.discussion and event.discussion.user:
                event.user = event.discussion.user
            else:
                raise ValueError("Nomination event has no user.")

        long_history = (
            f"{type_props[event.type].emoji} [{event.user}](https://osu.ppy.sh/users/{event.user.id})" +
            (" " if long_history else "") +
            long_history
        )

    if length_limit is None or len(long_history) <= length_limit:
        return f"\n{long_history}"
    
    short_history = ""
    for event in events:
        emoji = (
            f"{type_props[event.type].emoji}" +
            (" " if short_history else "")
        )

        # `- 3` to give space to ellipses if we need them.
        if len(short_history) + len(emoji) <= length_limit - 3:
            short_history = emoji + short_history
        else:
            # If there isn't enough space for anything, we skip the history completely.
            if len(short_history):
                short_history = "..." + short_history
            break
    
    return f"\n{short_history}"

def format_recent_praise(user: User, beatmapset: Beatmapset, database: Database=None):
    """Obtains the content of the most recent praise from the given user on the given beatmapset."""
    if not database: database = Database("aiess")

    praise_event = database.retrieve_last_type(user, beatmapset, where_type_str="type = \"praise\" OR type = \"hype\"")
    if praise_event:
        return praise_event.content
    return None
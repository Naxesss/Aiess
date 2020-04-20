from discord import Embed, Colour

from aiess import Event, User
from aiess import event_types as types

class TypeProps():
    """Represents the properties of how a type should be represented (e.g. emoji, name, colour)."""
    def __init__(self, emoji: str, title: str, colour: Colour, show_context: bool=False):
        self.emoji = emoji
        self.title = title
        self.colour = colour
        self.show_context = show_context

colour_ranked     = Colour.from_rgb(255,200,90)
colour_qualified  = Colour.from_rgb(255,75,100)
colour_nominated  = Colour.from_rgb(50,150,255)
colour_discussion = Colour.from_rgb(65,65,65)
colour_resolve    = Colour.from_rgb(100,200,100)
colour_reopen     = Colour.from_rgb(255,160,70)

type_props = {
    types.RANK:               TypeProps(":sparkling_heart:",    "Ranked",           colour_ranked),
    types.LOVE:               TypeProps(":gift_heart:",         "Loved",            colour_ranked),

    types.QUALIFY:            TypeProps(":heart:",              "Qualified",        colour_qualified),
    types.DISQUALIFY:         TypeProps(":broken_heart:",       "Disqualified",     colour_qualified),

    types.NOMINATE:           TypeProps(":thought_balloon:",    "Nominated",        colour_nominated),
    types.RESET:              TypeProps(":anger_right:",        "Nomination Reset", colour_nominated),

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

    return f"{beatmap_str}\n{mapped_by_str} {mode_str}"

def format_footer_text(event: Event) -> str:
    """Returns the footer text of the event (e.g. modder \"00:01:318 - fix blanket\"),
    if there's a user associated with the event, otherwise None."""
    if not event.user:
        return Embed.Empty
    
    if not event.content:
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
    return event.discussion.user

def format_context_field_value(event: Event) -> str:
    """Returns the content for the discussion context, surrounded in quotes."""
    return f"\"{event.discussion.content}\""
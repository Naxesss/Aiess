from discord import Embed, Colour

from aiess import Event

class TypeProps():
    """Represents the properties of how a type should be represented (i.e. emoji, name, colour)."""
    def __init__(self, emoji, title, colour):
        self.emoji = emoji
        self.title = title
        self.colour = colour

colour_ranked     = Colour.from_rgb(255,200,90)
colour_qualified  = Colour.from_rgb(255,75,100)
colour_nominated  = Colour.from_rgb(50,150,255)
colour_discussion = Colour.from_rgb(200,180,220)
colour_resolve    = Colour.from_rgb(70,255,100)
colour_reopen     = Colour.from_rgb(255,160,70)

type_props = {
    "rank":             TypeProps(":sparkling_heart:",    "Ranked",           colour_ranked),
    "love":             TypeProps(":gift_heart:",         "Loved",            colour_ranked),

    "qualify":          TypeProps(":heart:",              "Qualified",        colour_qualified),
    "disqualify":       TypeProps(":broken_heart:",       "Disqualified",     colour_qualified),

    "nominate":         TypeProps(":blue_heart:",         "Nominated",        colour_nominated),
    "nomination_reset": TypeProps(":small_blue_diamond:", "Nomination Reset", colour_nominated),

    "suggestion":       TypeProps(":yellow_circle:",      "Suggestion",       colour_discussion),
    "problem":          TypeProps(":red_circle:",         "Problem",          colour_discussion),
    "mapper_note":      TypeProps(":purple_circle:",      "Note",             colour_discussion),
    "hype":             TypeProps(":blue_circle:",        "Hype",             colour_discussion),
    "reply":            TypeProps(":white_circle:",       "Reply",            colour_discussion),

    "resolve":          TypeProps(":green_circle:",       "Resolve",          colour_resolve),
    "kudosu-gain":      TypeProps(":arrow_up:",           "Kudosu Gained",    colour_resolve),
    "kudosu-allow":     TypeProps(":arrow_double_up:",    "Kudosu Allowed",   colour_resolve),

    "reopen":           TypeProps(":orange_circle:",      "Reopen",           colour_reopen),
    "kudosu-lost":      TypeProps(":arrow_down:",         "Kudosu Lost",      colour_reopen),
    "kudosu-deny":      TypeProps(":arrow_double_down:",  "Kudosu Denied",    colour_reopen)
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
    return f"{type_props[event.type].emoji} {type_props[event.type].title}"

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
    if event.user:
        if event.content:
            # Markdown does not function in footer text; trying to escape it here would lead to visible '\'.
            return f"{event.user} \"{event.content}\""
        return event.user
    return None

def format_footer_icon_url(event: Event) -> str:
    """Returns the footer icon url of the event (i.e. the image url of the user's avatar),
    if there's a user associated with the event, otherwise None."""
    if event.user:
        return f"https://a.ppy.sh/{event.user.id}"
    return None

def format_thumbnail_url(event: Event) -> str:
    """Returns the thumbnail url for the event (e.g. beatmapset thumbnail)."""
    return f"https://b.ppy.sh/thumb/{event.beatmapset.id}l.jpg"
import sys
sys.path.append('..')

from enum import Enum
from datetime import datetime, timedelta, timezone
from functools import total_ordering
from typing import Union, Tuple

from discord import Embed, Colour

from aiess import Event, Beatmapset
from aiess import event_types as types

from aiess.database import SCRAPER_DB_NAME
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

colour_ranked     = Colour.from_rgb(255, 200, 90 )
colour_qualified  = Colour.from_rgb(255, 75,  100)
colour_nominated  = Colour.from_rgb(50,  150, 255)
colour_discussion = Colour.from_rgb(65,  65,  65 )
colour_resolve    = Colour.from_rgb(100, 200, 100)
colour_reopen     = Colour.from_rgb(255, 160, 70 )
colour_news       = Colour.from_rgb(255, 160, 200)
colour_added      = Colour.from_rgb(130, 235, 125)
colour_removed    = Colour.from_rgb(200, 160, 230)

type_props = {
    types.RANK:               TypeProps(":sparkling_heart:",         "Ranked",           colour_ranked,      show_history=True),
    types.LOVE:               TypeProps(":gift_heart:",              "Loved",            colour_ranked,      show_history=True),

    types.QUALIFY:            TypeProps(":heart:",                   "Qualified",        colour_qualified,   show_in_history=True),
    types.DISQUALIFY:         TypeProps(":broken_heart:",            "Disqualified",     colour_qualified,   show_in_history=True),
    types.UNLOVE:             TypeProps(":broken_heart:",            "Unloved",          colour_qualified,   show_in_history=True),

    types.NOMINATE:           TypeProps(":thought_balloon:",         "Nominated",        colour_nominated,   show_in_history=True),
    types.RESET:              TypeProps(":anger_right:",             "Nomination Reset", colour_nominated,   show_in_history=True),

    types.SUGGESTION:         TypeProps(":yellow_circle:",           "Suggestion",       colour_discussion),
    types.PROBLEM:            TypeProps(":red_circle:",              "Problem",          colour_discussion),
    types.NOTE:               TypeProps(":purple_circle:",           "Note",             colour_discussion),
    types.PRAISE:             TypeProps(":blue_heart:",              "Praise",           colour_discussion),
    types.HYPE:               TypeProps(":blue_circle:",             "Hype",             colour_discussion),
    types.REPLY:              TypeProps(":white_circle:",            "Reply",            colour_discussion,  show_context=True),

    types.RESOLVE:            TypeProps(":green_circle:",            "Resolved",         colour_resolve,     show_context=True),
    types.KUDOSU_GAIN:        TypeProps(":arrow_up:",                "Kudosu Given",     colour_resolve,     show_context=True),
    types.KUDOSU_ALLOW:       TypeProps(":arrow_double_up:",         "Kudosu Allowed",   colour_resolve,     show_context=True),

    types.REOPEN:             TypeProps(":orange_circle:",           "Reopened",         colour_reopen,      show_context=True),
    types.KUDOSU_LOSS:        TypeProps(":arrow_down:",              "Kudosu Removed",   colour_reopen,      show_context=True),
    types.KUDOSU_DENY:        TypeProps(":arrow_double_down:",       "Kudosu Denied",    colour_reopen,      show_context=True),

    types.DISCUSSION_DELETE:  TypeProps(":zap:",                     "Deleted",          colour_discussion,  show_context=True),
    types.DISCUSSION_RESTORE: TypeProps(":wrench:",                  "Restored",         colour_discussion,  show_context=True),
    types.REPLY_DELETE:       TypeProps(":zap:",                     "Reply Deleted",    colour_discussion,  show_context=True),
    types.REPLY_RESTORE:      TypeProps(":wrench:",                  "Reply Restored",   colour_discussion,  show_context=True),
    
    types.GENRE_EDIT:         TypeProps(":arrows_counterclockwise:", "Genre Edit",       colour_discussion),
    types.LANGUAGE_EDIT:      TypeProps(":arrows_counterclockwise:", "Language Edit",    colour_discussion),

    # Unlike other events, the embed title of news is simply the news title.
    types.NEWS:               TypeProps(None,                        None,               colour_news),

    types.ADD:                TypeProps(":performing_arts:",         "Added",            colour_added),
    types.REMOVE:             TypeProps(":performing_arts:",         "Removed",          colour_removed),
    
    types.SEV:                TypeProps(":scales:",                  "SEV Updated",      colour_ranked,      show_context=True)
}

def format_link(event: Event) -> str:
    """Returns a link which leads to the source of the given event
    (e.g. the discussion of a suggestion, or the beatmapset of a nomination)."""
    if event.discussion and event.discussion.beatmapset:
        # E.g. suggestions, problems, hypes, etc.
        return f"https://osu.ppy.sh/beatmapsets/{event.discussion.beatmapset.id}/discussion#/{event.discussion.id}"
    
    if event.beatmapset:
        # E.g. nominations, qualifications, ranks, etc.
        return f"https://osu.ppy.sh/beatmapsets/{event.beatmapset.id}"
    
    if event.newspost:
        return f"https://osu.ppy.sh/home/news/{event.newspost.slug}"
    
    if event.user:
        # E.g. group additions/removals.
        return f"https://osu.ppy.sh/users/{event.user.id}"

    raise ValueError("Cannot format a link of an event missing a beatmapset, newspost, and user.")

async def format_embed(event: Event, skip_timeago_if_recent: bool=False) -> str:
    """Returns an embed which represents the given event."""
    embed = Embed()
    embed.add_field(
        name   = format_field_name(event, skip_timeago_if_recent=skip_timeago_if_recent),
        value  = await format_field_value(event),
        inline = False
    )
    embed.set_footer(
        text     = format_footer_text(event),
        icon_url = format_footer_icon_url(event)
    )
    embed.colour = type_props[event.type].colour
    
    if format_thumbnail_url(event) is not None: embed.set_thumbnail(url=format_thumbnail_url(event))
    if format_image_url(event) is not None:     embed.set_image(url=format_image_url(event))

    if type_props[event.type].show_context and event.discussion:
        embed.add_field(
            name  = format_context_field_name(event),
            value = format_context_field_value(event)
        )

    return embed



def escape_markdown(obj: str) -> str:
    """Returns the given object cast to string, and where all markdown
    markers (e.g. '*', '_', and '~' characters) are escaped using backslash."""
    return (
        str(obj)
        .replace("*", "\\*")  # Italic / Bold
        .replace("_", "\\_")  # Italic / Underline
        .replace("~", "\\~")  # Strikethrough
        .replace("`", "\\`")  # Code / Code Block
    )

def format_field_name(event: Event, skip_timeago_if_recent: bool=False) -> str:
    """Returns the embed title of the given event (e.g. :heart: Qualified)."""
    if event.newspost:
        title = event.newspost.title
    else:
        title = f"{type_props[event.type].emoji}\u2000{type_props[event.type].title}"
    
    if event.group:
        return f"{title} (< {format_timeago(event.time)})"

    return f"{title} ({format_timeago(event.time)})"

async def format_field_value(event: Event) -> str:
    """Returns the embed contents of the given event (i.e. the \"artist - title, mapped by creator [modes]\" part)."""
    if event.beatmapset:
        artist_title_str = escape_markdown(f"{event.beatmapset.artist} - {event.beatmapset.title}")
        creator_str = escape_markdown(event.beatmapset.creator)

        beatmap_str = f"[**{artist_title_str}**](https://osu.ppy.sh/beatmapsets/{event.beatmapset.id})"
        mapped_by_str = f"Mapped by [{creator_str}](https://osu.ppy.sh/users/{event.beatmapset.creator.id})"
        mode_str = event.beatmapset.mode_str().replace("[", "[**").replace("]", "**]")

        result = f"{beatmap_str}\n{mapped_by_str} {mode_str}"

        if type_props[event.type].show_history:
            # Give how much room the function has to work with, allowing it to smartly shorten/truncate if needed.
            # This is to account for the embed field value character limit of 1024.
            result += await format_history(event.beatmapset, length_limit=1024-len(result))

        return result

    if event.newspost:
        return event.newspost.preview if event.newspost.preview else "(Missing preview)"
    
    if event.group:
        to_or_from = "to" if event.type == types.ADD else "from"
        return (
            f"[{escape_markdown(event.user)}](https://osu.ppy.sh/users/{event.user.id}) {to_or_from} the\n" +
            f"[**{event.group.name}**](https://osu.ppy.sh/groups/{event.group.id})" +
            (f"\nfor [**{event.group.mode}**]" if event.group.mode else "")
        )
    
    raise ValueError("Cannot format a field value of an event missing a beatmapset, newspost, and group.")

def format_footer_text(event: Event) -> str:
    """Returns the footer text of the event (e.g. modder \"00:01:318 - fix blanket\"),
    if there's a user associated with the event, otherwise None."""
    if event.newspost:
        return event.newspost.author.name

    if event.group:
        if not event.content:
            # Group events already include `event.user` elsewhere in the embed, so shouldn't be here.
            return None
        else:
            return f"NAT {format_preview(event.content)}"

    if event.type == types.SEV:
        return f"NAT {format_preview(event.content)}"

    if not event.user:
        return None

    if event.content:
        text = f"{event.user} {format_preview(event.content)}"

        formatted_diff = format_tab_diff(event)
        # Difficulty is already displayed in the context field for replies/resolves/etc.
        if formatted_diff and not type_props[event.type].show_context:
            text += f" {formatted_diff}"
        
        return text
    
    return str(event.user)

def truncate(content: str, length: int, indicator: str="... [truncated]") -> str:
    """Returns a string as per normal, unless it exceeds the length, at which point
    it is truncated with the indicator appended."""
    return content if len(content) <= length else content[:length-len(indicator)] + indicator

def format_preview(content: str, length: int=60, split_newline: bool=True) -> str:
    """Returns a string of the user with the truncated content in quotes, if any,
    else just the user, again if any, otherwise None."""
    if not content:
        return ""
    
    preview = content
    if split_newline:
        preview = content.partition("\n")[0]

    # Markdown does not function in footer text; trying to escape it here would lead to visible '\'.
    return "\"" + truncate(preview, length=length, indicator="...") + "\""

def format_tab_diff(event: Event):
    """Returns the difficulty in square brackets, if any and our tab is not "generalAll", otherwise None."""
    if (
        event.discussion and
        event.discussion.tab != "generalAll" and
        event.discussion.difficulty is not None
    ):
        return f"[{event.discussion.difficulty}]"
    return None

def format_footer_icon_url(event: Event) -> str:
    """Returns the footer icon url of the event (i.e. the image url of the user's avatar),
    if there's a user associated with the event, otherwise None."""
    if event.group:
        if not event.content:
            return None
        else:
            # `6616586` is the user id for the QAT bot, which I'm just going to use to represent the NAT/BNSite.
            return "https://a.ppy.sh/6616586"

    if event.type == types.SEV:
        return "https://a.ppy.sh/6616586"

    if event.user and not event.group:
        if event.user.id:
            return f"https://a.ppy.sh/{event.user.id}"
        else:
            # In case the user is restricted.
            return "https://osu.ppy.sh/images/layout/avatar-guest.png"
    
    if event.newspost:
        # In case the author field is free-text (e.g. "Noffy & -Mo-").
        return "https://osu.ppy.sh/images/layout/avatar-guest.png"
    
    return None

def format_thumbnail_url(event: Event) -> str:
    """Returns the thumbnail url for the event (e.g. beatmapset thumbnail), if applicable, else None."""
    if event.beatmapset:
        return f"https://b.ppy.sh/thumb/{event.beatmapset.id}l.jpg"
    
    if event.group:
        return f"https://a.ppy.sh/{event.user.id}"
    
    return None

def format_image_url(event: Event) -> str:
    """Returns the image url for the event (e.g. newspost banner), if applicable, else None."""
    if event.newspost:
        return event.newspost.image_url
    return None

def format_context_field_name(event: Event) -> str:
    """Returns the title for the discussion context; the name of the discussion author."""
    return escape_markdown(event.discussion.user)

def format_context_field_value(event: Event) -> str:
    """Returns the content for the discussion context, surrounded in quotes."""
    text = format_preview(escape_markdown(event.discussion.content))

    formatted_diff = format_tab_diff(event)
    if formatted_diff:
        text += escape_markdown(f" {formatted_diff}")
    
    return text

async def format_history(beatmapset: Beatmapset, length_limit: int=None, database: Database=None) -> str:
    """Returns the nomination history of this beatmapset (i.e. icons and names of actions and their authors).
    Optionally within a certain length, smartly shortening/truncating the contents if needed."""
    if not database: database = Database(SCRAPER_DB_NAME)  # Using wrapped database to access events.

    # Sorted by time ascending; newer events first.
    events = list(filter(
        lambda event: type_props[event.type].show_in_history,
        await database.retrieve_beatmapset_events(beatmapset)))

    long_history = ""
    for event in events:
        # Some nomination events seem to be missing a user.
        if not event.user:
            if event.discussion and event.discussion.user:
                event.user = event.discussion.user
            else:
                # Old versions of the scraper inserted system qualifications, we should ignore those.
                continue

        long_history = (
            f"{type_props[event.type].emoji} [{event.user}](https://osu.ppy.sh/users/{event.user.id})" +
            ("\u2000" if long_history else "") +
            long_history
        )

    if length_limit is None or len(long_history) < length_limit:
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
            if short_history:
                short_history = "..." + short_history
            break
    
    return f"\n{short_history}"



# This decorator infers `<=`, `>=`, and `>` from `<` (__lt__) and `==` (__eq__).
@total_ordering
class TimeUnit(Enum):
    MICROSECONDS = 0
    MILLISECONDS = 1
    SECONDS = 2
    MINUTES = 3
    HOURS = 4
    DAYS = 5
    WEEKS = 6
    MONTHS = 7
    YEARS = 8

    # Comparison is not inherently supported by Enum.
    # With the help of @total_ordering, we fully support comparison with this.
    def __lt__(self, other):
        if isinstance(other, TimeUnit):
            return self.value < other.value
        return NotImplemented

def unit_str(unit: TimeUnit, long: bool=False, size: int=None):
    """Returns the string representation of the time unit. By default as "d/h/min/etc", but
    becomes "days/hours/minutes/etc" if `long`. `size` only needs to be supplied if `long` is
    True, and enables plural adaptation (e.g. "1 day", not "1 days")."""
    s_if_plural = "s" if size and size != 1 else ""
    if unit == TimeUnit.YEARS:        return ("year"        + s_if_plural) if long else "y"
    if unit == TimeUnit.MONTHS:       return ("month"       + s_if_plural) if long else "M"
    if unit == TimeUnit.WEEKS:        return ("week"        + s_if_plural) if long else "w"
    if unit == TimeUnit.DAYS:         return ("day"         + s_if_plural) if long else "d"
    if unit == TimeUnit.HOURS:        return ("hour"        + s_if_plural) if long else "h"
    if unit == TimeUnit.MINUTES:      return ("minute"      + s_if_plural) if long else "min"
    if unit == TimeUnit.SECONDS:      return ("second"      + s_if_plural) if long else "s"
    if unit == TimeUnit.MILLISECONDS: return ("millisecond" + s_if_plural) if long else "ms"
    if unit == TimeUnit.MICROSECONDS: return ("microsecond" + s_if_plural) if long else "μs"

def format_time(
        delta_time: Union[timedelta, float], min_unit: TimeUnit=TimeUnit.SECONDS, max_units: int=2,
        long: bool=False) -> str:
    """Returns a string representing the difference in time, in the most appropriate units, (e.g. \"2 min 36 s\").
    
    `delta_time` : Union[timedelta, float]
        The time difference to format. Can be either a timedelta or a float second representation.
        The numeric argument can include decimals for subsecond accuracy.
    `min_unit` : TimeUnit
        The minimum unit to display (e.g. if seconds, miliseconds will be skipped).
        Set to None to remove this limit.
    `max_units` : int
        The maximum amount of units to display (e.g. if 2, and days and hours are displayed, the rest is skipped).
        Set to None to remove this limit.
    `long` : bool
        Whether to display units as "days/hours/minutes/etc" instead of "d/h/min/etc". False by default.
        Adapts to plurality (e.g. if 1 day, it'll display "1 day" and not "1 days")."""
    if isinstance(delta_time, timedelta):
        total_ms = delta_time.total_seconds() * 1000
    else:
        total_ms = delta_time * 1000

    years,        total_ms = divmod(total_ms, 365*24*60*60*1000)
    months,       total_ms = divmod(total_ms, 30*24*60*60*1000)   # Assuming all months are 30 days long.
    weeks,        total_ms = divmod(total_ms, 7*24*60*60*1000)
    days,         total_ms = divmod(total_ms, 24*60*60*1000)
    hours,        total_ms = divmod(total_ms, 60*60*1000)
    minutes,      total_ms = divmod(total_ms, 60*1000)
    seconds,      total_ms = divmod(total_ms, 1000)
    milliseconds, total_ms = divmod(total_ms, 1)
    microseconds, total_ms = divmod(total_ms, 0.001)

    formatted_units = []
    def try_add_formatted_unit(size: float, unit: TimeUnit):
        if size and (min_unit is None or min_unit <= unit) and (max_units is None or len(formatted_units) < max_units):
            formatted_units.append(f"{int(size)} {unit_str(unit, long=long, size=int(size))}")

    try_add_formatted_unit(years,        TimeUnit.YEARS)
    try_add_formatted_unit(months,       TimeUnit.MONTHS)
    try_add_formatted_unit(weeks,        TimeUnit.WEEKS)
    try_add_formatted_unit(days,         TimeUnit.DAYS)
    try_add_formatted_unit(hours,        TimeUnit.HOURS)
    try_add_formatted_unit(minutes,      TimeUnit.MINUTES)
    try_add_formatted_unit(seconds,      TimeUnit.SECONDS)
    try_add_formatted_unit(milliseconds, TimeUnit.MILLISECONDS)
    try_add_formatted_unit(microseconds, TimeUnit.MICROSECONDS)

    return " ".join(formatted_units) if formatted_units else f"< 1 {unit_str(min_unit, long=long, size=1)}"

def format_timeago(time: datetime):
    """Returns the dynamic markdown representation of the time since the given datetime in
    the format "{time} ago" e.g. "a minute ago" / "2 minutes ago" / "3 months ago"."""
    return f"<t:{int(time.replace(tzinfo=timezone.utc).timestamp())}:R>"

def format_dotted_list(elements: list) -> str:
    """Returns a dotted list representing the given elements."""
    # `\00a0` is a non-breaking space, ensuring that the dot and element are always aligned.
    return "\n".join(f"∙\u00a0{element}" for element in elements)
from aiess import Event

type_field_name = {
    "suggestion": ":yellow_circle: Suggestion",
    "problem": ":red_circle: Problem"
}

def format_link(event: Event) -> str:
    if event.discussion and event.discussion.beatmapset:
        return f"https://osu.ppy.sh/beatmapsets/{event.discussion.beatmapset.id}/discussion#/{event.discussion.id}"
    
    if event.beatmapset:
        return f"https://osu.ppy.sh/beatmapsets/{event.beatmapset.id}"
    
    raise ValueError("Cannot format a link of an event missing a beatmapset.")



def escape_markdown(string: str) -> str:
    # Cast to str in case the argument is of type e.g. User.
    return (str(string)
        .replace("*", "\\*")   # Italic / Bold
        .replace("_", "\\_")   # Italic / Underline
        .replace("~", "\\~")   # Strikethrough
        .replace("`", "\\`"))  # Code / Code Block

def format_field_name(event: Event) -> str:
    return type_field_name[event.type]

def format_field_value(event: Event) -> str:
    artist_title_str = escape_markdown(f"{event.beatmapset.artist} - {event.beatmapset.title}")
    creator_str = escape_markdown(event.beatmapset.creator)

    beatmap_str = f"[**{artist_title_str}**](https://osu.ppy.sh/beatmapsets/{event.beatmapset.id})"
    mapped_by_str = f"Mapped by [{creator_str}](https://osu.ppy.sh/users/{event.beatmapset.creator.id})"
    mode_str = event.beatmapset.mode_str().replace("[", "[**").replace("]", "**]")

    return f"{beatmap_str}\n{mapped_by_str} {mode_str}"

def format_footer_text(event: Event) -> str:
    if event.user:
        if event.content:
            # Markdown does not function in footer text; trying to escape it here would lead to visible '\'.
            return f"{event.user} \"{event.content}\""
        return event.user
    return None

def format_footer_icon_url(event: Event) -> str:
    if event.user:
        return f"https://a.ppy.sh/{event.user.id}"
    return None
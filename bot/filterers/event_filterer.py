import sys
sys.path.append('..')

from typing import Dict, List, Tuple
from collections import OrderedDict

from aiess import event_types as types

from bot.logic import expand, split_unescaped
from bot.logic import AND_GATES, OR_GATES, NOT_GATES
from bot.filterer import is_int, escape, is_valid, get_key_value_pairs
from bot.filterer import FilterContext, Tag

ANY_ALIASES = ["any", "all"]

# Any of these values can be substituted for the respective key;
# if the user expects it to work, it should work.
TYPE_ALIASES: Dict[str, List[str]] = {
    types.RANK:         ANY_ALIASES + ["ranked"],
    types.LOVE:         ANY_ALIASES + ["loved"],
    types.UNLOVE:       ANY_ALIASES + ["unloved",          "unlove"],
    types.QUALIFY:      ANY_ALIASES + ["qualified",        "qualification",    "qual"],
    types.DISQUALIFY:   ANY_ALIASES + ["disqualified",     "disqualification", "dq"],
    types.NOMINATE:     ANY_ALIASES + ["nominated",        "nomination",       "nom",   "bubble", "bubbled"],
    types.RESET:        ANY_ALIASES + ["reset",                                         "pop",    "popped"],

    types.SUGGESTION:   ANY_ALIASES + [],
    types.PROBLEM:      ANY_ALIASES + [],
    types.NOTE:         ANY_ALIASES + ["mapper note", "note"],
    types.PRAISE:       ANY_ALIASES + [],
    types.HYPE:         ANY_ALIASES + [],
    types.REPLY:        ANY_ALIASES + [],

    types.RESOLVE:      ANY_ALIASES + ["issue resolve", "issue resolved", "resolve", "resolved"],
    types.REOPEN:       ANY_ALIASES + ["issue reopen",  "issue reopened", "reopen",  "reopened"],

    types.KUDOSU_GAIN:  ANY_ALIASES + ["kudosu gain",  "kudosu gained", "kudosu given"],
    types.KUDOSU_LOSS:  ANY_ALIASES + ["kudosu loss",  "kudosu lost",   "kudosu taken"],
    types.KUDOSU_DENY:  ANY_ALIASES + ["kudosu deny",  "kudosu denied"],
    types.KUDOSU_ALLOW: ANY_ALIASES + ["kudosu allow", "kudosu allowed"],
    
    types.GENRE_EDIT:    ANY_ALIASES + ["genre edit", "genre"],
    types.LANGUAGE_EDIT: ANY_ALIASES + ["language edit", "language"],

    types.NEWS:         ANY_ALIASES + ["newspost", "newsposts", "news post", "news posts"],

    types.ADD:          ANY_ALIASES + ["added", "promote", "promoted"],
    types.REMOVE:       ANY_ALIASES + ["removed", "demote", "demoted"]
}

# Includes both full and probationary bns.
BN_ALIASES = ["bn", "bns", "bng", "nominators", "beatmap nominators"]
GROUP_ALIASES: Dict[str, List[str]] = {
    "4": ANY_ALIASES + ["gmt", "gmts", "global moderators", "global moderation team"],
    "7": ANY_ALIASES + ["nat", "nats", "nomination assessment", "nomination assessment team"],
    "11": ANY_ALIASES + ["dev", "devs", "developers"],
    "16": ANY_ALIASES + ["alu", "alumni", "alumnis"],
    "22": ANY_ALIASES + ["sup", "support", "support team"],
    "28": ANY_ALIASES + BN_ALIASES + ["full", "full bn", "full bns", "full beatmap nominators"],
    "32": (ANY_ALIASES + BN_ALIASES + ["probo", "probo bn", "probo bns", "probation", "probation bn",
        "probation bns", "probationary beatmap nominators"])
}

def get_all_type_aliases() -> List[str]:
    VALID_TYPES = [key for key in TYPE_ALIASES]
    VALID_TYPES.extend(alias for aliases in TYPE_ALIASES.values() for alias in aliases)
    # Accept "-" and "_" as substitutions of whitespace.
    VALID_TYPES.extend(alias.replace(" ", "-") for aliases in TYPE_ALIASES.values() for alias in aliases)
    VALID_TYPES.extend(alias.replace(" ", "_") for aliases in TYPE_ALIASES.values() for alias in aliases)
    return VALID_TYPES

def get_type_aliases(key: str) -> List[str]:
    VALID_TYPES = [key] + TYPE_ALIASES[key]
    VALID_TYPES.extend(alias for alias in TYPE_ALIASES[key])
    # Accept "-" and "_" as substitutions of whitespace.
    VALID_TYPES.extend(alias.replace(" ", "-") for alias in TYPE_ALIASES[key])
    VALID_TYPES.extend(alias.replace(" ", "_") for alias in TYPE_ALIASES[key])
    return VALID_TYPES

def get_all_group_aliases() -> List[str]:
    VALID_TYPES = [key for key in GROUP_ALIASES]
    VALID_TYPES.extend(alias for aliases in GROUP_ALIASES.values() for alias in aliases)
    # Accept "-" and "_" as substitutions of whitespace.
    VALID_TYPES.extend(alias.replace(" ", "-") for aliases in GROUP_ALIASES.values() for alias in aliases)
    VALID_TYPES.extend(alias.replace(" ", "_") for aliases in GROUP_ALIASES.values() for alias in aliases)
    return VALID_TYPES

def get_group_aliases(key: str) -> List[str]:
    VALID_TYPES = [key] + GROUP_ALIASES[key]
    VALID_TYPES.extend(alias for alias in GROUP_ALIASES[key])
    # Accept "-" and "_" as substitutions of whitespace.
    VALID_TYPES.extend(alias.replace(" ", "-") for alias in GROUP_ALIASES[key])
    VALID_TYPES.extend(alias.replace(" ", "_") for alias in GROUP_ALIASES[key])
    return VALID_TYPES

HINT_ANY = "Accepts any value."
HINT_INT = "Accepts any integer value."

filter_context = FilterContext(
    name     = "Events",
    examples = [
        "**#mapfeed** `type:(nom or qual or dq or reset or rank or love) and not user:banchobot`",
        "**#mapfeed-osu** `type:(nom or qual or dq or reset or rank or love) and not user:banchobot and mode:osu`",
        "**#groupfeed** `group:any`",
        "**#groupfeed-bns** `group:bns`",
        "**#newsfeed** `type:news`",
        "**#newsfeed-fa** `type:news and news-title:\"%featured artist%\"`",
        "**involves you** `(author or creator):{your name} and not user:{your name}`",
        "**involves you + works with renames** `(author-id or creator-id):{your id} and not user-id:{your id}`"
    ],
    tags     = [
        # User
        Tag(
            names           = ["user"],
            description     = "The username of the user performing the event (e.g. user nominating, replying, or giving kudosu).",
            example_values  = ["lasse", "\"seto kousuke\""],
            value_hint      = HINT_ANY,
            value_predicate = lambda value: True,
            value_func      = lambda event: [escape(event.user.name)] if event.user else None
        ),
        Tag(
            names           = ["user-id"],
            description     = "The id of the user performing the event (e.g. id of user nominating, replying, or giving kudosu).",
            example_values  = ["896613"],
            value_hint      = HINT_INT,
            value_predicate = is_int,
            value_func      = lambda event: [escape(event.user.id)] if event.user else None
        ),
        # Beatmapset
        Tag(
            names           = ["set-id", "mapset-id", "beatmapset-id"],
            description     = "The id of the beatmapset where the event occurred (e.g. id of mapset nominated or discussed).",
            example_values  = ["41823"],
            value_hint      = HINT_INT,
            value_predicate = is_int,
            value_func      = lambda event: [escape(event.beatmapset.id)] if event.beatmapset else None
        ),
        Tag(
            names           = ["artist"],
            description     = "The artist field of a beatmapset an event occurred on (e.g. \"LeaF\" in \"Leaf - Doppelganger\").",
            example_values  = ["nhato", "\"the quick brown fox\""],
            value_hint      = HINT_ANY,
            value_predicate = lambda value: True,
            value_func      = lambda event: [escape(event.beatmapset.artist)] if event.beatmapset else None
        ),
        Tag(
            names           = ["title"],
            description     = "The title field of a beatmapset an event occurred on (e.g. \"Doppelganger\" in \"Leaf - Doppelganger\").",
            example_values  = ["uta", "\"baka mitai\""],
            value_hint      = HINT_ANY,
            value_predicate = lambda value: True,
            value_func      = lambda event: [escape(event.beatmapset.title)] if event.beatmapset else None
        ),
        Tag(
            names           = ["creator"],
            description     = "The username of the creator of a beatmapset an event occurred on (e.g. \"Shurelia\" for any set hosted by them).",
            example_values  = ["lasse", "\"seto kousuke\""],
            value_hint      = HINT_ANY,
            value_predicate = lambda value: True,
            value_func      = lambda event: [escape(event.beatmapset.creator.name)] if event.beatmapset else None
        ),
        Tag(
            names           = ["creator-id"],
            description     = "The id of the creator of a beatmapset an event occurred on (e.g. \"3807986\" for any set hosted by Shurelia).",
            example_values  = ["896613"],
            value_hint      = HINT_INT,
            value_predicate = is_int,
            value_func      = lambda event: [escape(event.beatmapset.creator.id)] if event.beatmapset else None
        ),
        Tag(
            names           = ["mode"],
            description     = "The involved mode of a beatmapset an event occurred on (e.g. \"taiko\" for any set with a taiko map).",
            example_values  = ["osu", "taiko", "catch", "mania"],
            value_hint      = "\u2000".join(f"`{mode}`" for mode in ["osu", "taiko", "catch", "mania"]),
            value_predicate = lambda value: value in ["osu", "taiko", "catch", "mania"],
            value_func      = lambda event: [escape(mode) for mode in event.beatmapset.modes] if event.beatmapset else None
        ),
        Tag(
            names           = ["genre"],
            description     = "The genre of a beatmapset an event occurred on (e.g. \"rock\" for rock songs).",
            example_values  = ["rock", "pop", "jazz"],
            value_hint      = HINT_ANY,
            value_predicate = lambda value: True,
            value_func      = lambda event: [escape(event.beatmapset.genre)] if event.beatmapset else None
        ),
        Tag(
            names           = ["language"],
            description     = "The language of a beatmapset an event occurred on (e.g. \"english\" for songs in english).",
            example_values  = ["english", "instrumental", "spanish"],
            value_hint      = HINT_ANY,
            value_predicate = lambda value: True,
            value_func      = lambda event: [escape(event.beatmapset.language)] if event.beatmapset else None
        ),
        Tag(
            names           = ["tag", "tags"],
            description     = "The tags of a beatmapset an event occurred on (e.g. \"featured\" and \"artist\" if \"featured artist\" is in the tags).",
            example_values  = ["gder", "(mappers' and guild)", "(rock and instrumental)"],
            value_hint      = HINT_ANY,
            value_predicate = lambda value: True,
            value_func      = lambda event: [escape(tag) for tag in event.beatmapset.tags] if event.beatmapset else None,
            # E.g. tags:"mappers' guild" -> tags:(mappers' and guild).
            value_convert   = lambda value: ("(" + str.join(" and ", value.split(" ")) + ")") if " " in value else None
        ),
        # Discussion
        Tag(
            names           = ["discussion-id"],
            description     = "The id of the discussion an event occurred on (e.g. \"1589811\" for that specific discussion).",
            example_values  = ["1687831"],
            value_hint      = HINT_INT,
            value_predicate = is_int,
            value_func      = lambda event: [escape(event.discussion.id)] if event.discussion else None
        ),
        Tag(
            names           = ["author"],
            description     = "The username of the author of the discussion an event occurred on (e.g. \"Shurelia\" for any discussion started by them).",
            example_values  = ["lasse", "\"seto kousuke\""],
            value_hint      = HINT_ANY,
            value_predicate = lambda value: True,
            value_func      = lambda event: [escape(event.discussion.user.name)] if event.discussion else None
        ),
        Tag(
            names           = ["author-id"],
            description     = "The id of the author of the discussion an event occurred on (e.g. \"3807986\" for any discussion started by Shurelia).",
            example_values  = ["896613"],
            value_hint      = HINT_INT,
            value_predicate = is_int,
            value_func      = lambda event: [escape(event.discussion.user.id)] if event.discussion else None
        ),
        Tag(
            names           = ["discussion-content"],
            description     = "The text content of the discussion an event occurred on (e.g. \"blanket\" for any discussion started containing that).",
            example_values  = ["nice", "\"very cool\""],
            value_hint      = HINT_ANY,
            value_predicate = lambda value: True,
            value_func      = lambda event: [escape(event.discussion.content)] if event.discussion else None
        ),
        Tag(
            names           = ["discussion-tab"],
            description     = "The tab which the discussion of an event occurred on (e.g. \"timeline\" for any discussion associated with a timestamp).",
            example_values  = ["timeline", "general", "generalAll"],
            value_hint      = "\u2000".join(f"`{tab}`" for tab in ["timeline", "general", "generalAll"]),
            value_predicate = lambda value: value in ["timeline", "general", "generalAll"],
            value_func      = lambda event: [escape(event.discussion.tab)] if event.discussion else None
        ),
        Tag(
            names           = ["discussion-difficulty"],
            description     = "The difficulty which the discussion of an event occurred on (e.g. \"Expert\" for any discussion on that difficulty).",
            example_values  = ["insane", "\"gder's expert\""],
            value_hint      = HINT_ANY,
            value_predicate = lambda value: True,
            value_func      = lambda event: [escape(event.discussion.difficulty)] if event.discussion else None
        ),
        # Usergroup
        Tag(
            names           = ["group"],
            description     = "The name of the group a user was added to or removed from (e.g. \"bns\" for both full and probo BNs).",
            example_values  = ["bns", "nat", "gmt", "devs"],
            # Ignore group ids, only show distinct aliases (full bn and probo bn have some identical ones).
            value_hint      = "\u2000".join(list(OrderedDict.fromkeys(f"`{alias}`" for aliases in GROUP_ALIASES.values() for alias in aliases))),
            value_predicate = lambda value: value in get_all_group_aliases(),
            value_func      = lambda event: (
                    [escape(str(event.group.id))] +
                    ([escape(alias) for alias in get_group_aliases(str(event.group.id))] if str(event.group.id) in GROUP_ALIASES else [])
                ) if event.group else None
        ),
        Tag(
            names           = ["group-id"],
            description     = "The id of the group a user was added to or removed from (e.g. \"7\" for BAT/QAT/NAT).",
            example_values  = ["4", "7", "28", "32"],
            value_hint      = HINT_INT,
            value_predicate = is_int,
            value_func      = lambda event: [escape(event.group.id)] if event.group else None
        ),
        # Newspost
        Tag(
            names           = ["news-title"],
            description     = "The title of the newspost (e.g. \"%featured artist%\" for FA news).",
            example_values  = ["\"New Featured Artist: DragonForce\"", "\"%title contains this%\""],
            value_hint      = HINT_ANY,
            value_predicate = lambda value: True,
            value_func      = lambda event: [escape(event.newspost.title)] if event.newspost else None
        ),
        Tag(
            names           = ["news-content", "news-preview"],
            description     = "The preview of the newspost (e.g. \"We're excited to welcome Lasse as our newest featured artist!\").",
            example_values  = ["\"preview is exactly this\"", "\"%preview contains this%\""],
            value_hint      = HINT_ANY,
            value_predicate = lambda value: True,
            value_func      = lambda event: [escape(event.newspost.preview)] if event.newspost else None
        ),
        Tag(
            names           = ["news-author"],
            description     = "The username of the author of the newspost (e.g. \"Ephemeral\").",
            example_values  = ["Ephemeral", "\"The Spotlights Team\"", "\"%contains this%\""],
            value_hint      = HINT_ANY,
            value_predicate = lambda value: True,
            value_func      = lambda event: [escape(event.newspost.author.name)] if event.newspost else None
        ),
        Tag(
            names           = ["news-author-id"],
            description     = "The id of the author of the newspost (e.g. \"102335\" for Ephemeral).",
            example_values  = ["102335"],
            value_hint      = HINT_ANY,
            value_predicate = lambda value: True,
            value_func      = lambda event: [escape(event.newspost.author.id)] if event.newspost else None
        ),
        # Event
        Tag(
            names           = ["type"],
            description     = "The type of an event (e.g. nominate, kudosu_gain, or suggestion). Spaces, dashes, and underscores are interchangable.",
            example_values  = ["reset", "nomination-reset", "\"nomination reset\""],
            value_hint      = "\u2000".join(f"`{alias}`" for alias in TYPE_ALIASES) + "\u2000(+lots of aliases)",
            value_predicate = lambda value: value in get_all_type_aliases(),
            value_func      = lambda event: (
                    [escape(event.type)] +
                    ([escape(alias) for alias in get_type_aliases(event.type)] if event.type in TYPE_ALIASES else [])
                )
        ),
        Tag(
            names           = ["content"],
            description     = "The text content associated with an event (e.g. the text of a reply, disqualification, or discussion). `%` is a wildcard.",
            example_values  = ["nice", "\"very cool\"", "\"%contains this%\""],
            value_hint      = HINT_ANY,
            value_predicate = lambda value: True,
            value_func      = lambda event: [escape(event.content)] if event.content else None
        )
    ]
)

TAG_TO_SQL = {
    filter_context.get_tag("user")                  : "user.name LIKE %s",
    filter_context.get_tag("user-id")               : "user.id=%s",
    filter_context.get_tag("set-id")                : "beatmapset.id=%s",
    filter_context.get_tag("artist")                : "beatmapset.artist LIKE %s",
    filter_context.get_tag("title")                 : "beatmapset.title LIKE %s",
    filter_context.get_tag("creator")               : "creator.name LIKE %s",
    filter_context.get_tag("creator-id")            : "creator.id=%s",
    filter_context.get_tag("mode")                  : "mode=%s",
    filter_context.get_tag("discussion-id")         : "discussion.id=%s",
    filter_context.get_tag("author")                : "author.name LIKE %s",
    filter_context.get_tag("author-id")             : "author.id LIKE %s",
    filter_context.get_tag("discussion-content")    : "discussion.content LIKE %s",
    filter_context.get_tag("group")                 : "group_id=%s",
    filter_context.get_tag("group-id")              : "group_id=%s",
    filter_context.get_tag("news-title")            : "newspost.title LIKE %s",
    filter_context.get_tag("news-content")          : "newspost.preview LIKE %s",
    filter_context.get_tag("news-author")           : "newspost.author_name LIKE %s",
    filter_context.get_tag("news-author-id")        : "newspost.author_id=%s",
    filter_context.get_tag("type")                  : "type=%s",
    filter_context.get_tag("content")               : "events.content LIKE %s",
    filter_context.get_tag("discussion-tab")        : "discussion.tab LIKE %s",
    filter_context.get_tag("discussion-difficulty") : "discussion.difficulty LIKE %s",
    filter_context.get_tag("tags")                  : "beatmapset.tags LIKE %s"
}

def filter_to_sql(_filter: str) -> Tuple[str, tuple]:
    """Returns a tuple of the filter converted to an SQL WHERE clause and the inputs to the
    WHERE clause (e.g. ("type=%s", ("nominate",)) ), for use with the scraper database."""
    if not _filter:
        # Without a filter, we simply let everything through.
        return ("TRUE", ())

    if not is_valid(_filter, filter_context):
        raise ValueError("Received an invalid filter; cannot convert to sql.")

    converted_words = []
    converted_values = []
    for word, _ in split_unescaped(expand(_filter), (" ",)):
        # Convert gate symbols in the filter (e.g. "&", "!", "and", "|") to "AND", "OR", and "NOT".
        if any(map(lambda gate: word.lower() == gate.strip().lower(), AND_GATES)): word = "AND"
        if any(map(lambda gate: word.lower() == gate.strip().lower(), OR_GATES)):  word = "OR"
        if any(map(lambda gate: word.lower() == gate.strip().lower(), NOT_GATES)): word = "NOT"
        if word in ["AND", "OR", "NOT"]:
            converted_words.append(word)
            continue

        key, value = next(get_key_value_pairs(word))
        tag = filter_context.get_tag(key)
        if not tag:
            continue

        values = []
        use_and = False

        # Support type aliases (e.g. "resolve" should be converted to "issue-resolve").
        if key.lower() == "type":
            for _type in TYPE_ALIASES:
                if value.lower() in TYPE_ALIASES[_type]:
                    values.append(_type)
        
        # Support group aliases (e.g. "nat" should be converted to "7").
        if key.lower() == "group":
            for group in GROUP_ALIASES:
                if value.lower() in GROUP_ALIASES[group]:
                    values.append(group)

        # Ease tag search (e.g. "tags:"featured artist"" should be converted to "tags:%featured% and tags:%artist%").
        if key.lower() in ["tag", "tags"]:
            for split in value.split(" "):
                values.append("%" + split + "%")
            use_and = True

        if not values:
            # Our value is not an alias, so we can use it directly.
            values.append(value)

        if   len(values) > 1 and use_and: converted_words.append("(" + " AND ".join([TAG_TO_SQL[tag]] * len(values)) + ")")
        elif len(values) > 1:             converted_words.append("(" + " OR ".join([TAG_TO_SQL[tag]] * len(values)) + ")")
        else:                             converted_words.append(TAG_TO_SQL[tag])
        converted_values.extend(values)
    
    return (" ".join(converted_words), tuple(converted_values))
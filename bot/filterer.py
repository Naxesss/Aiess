import sys
sys.path.append('..')

from typing import Union, Dict, List, Generator, Callable, Tuple
from collections import OrderedDict
import re

from aiess import Event, User, Beatmapset, Discussion, NewsPost, Usergroup
from aiess import event_types as types

from bot.logic import expand, split_unescaped, extract_not
from bot.logic import AND_GATES, OR_GATES, NOT_GATES

KEY_VALUE_PATTERN = "(\"[^\"]+.|[^ ]+):(\"[^\"]+.|[^ ]+)"

ANY_ALIASES = ["any", "all"]

# Any of these values can be substituted for the respective key;
# if the user expects it to work, it should work.
TYPE_ALIASES: Dict[str, List[str]] = {
    types.RANK:         ANY_ALIASES + ["ranked"],
    types.LOVE:         ANY_ALIASES + ["loved"],
    types.QUALIFY:      ANY_ALIASES + ["qualified",        "qualification",    "qual"],
    types.DISQUALIFY:   ANY_ALIASES + ["disqualified",     "disqualification", "dq"],
    types.NOMINATE:     ANY_ALIASES + ["nominated",        "nomination",       "nom",   "bubble", "bubbled"],
    types.RESET:        ANY_ALIASES + ["nomination reset",                     "reset", "pop",    "popped"],

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

    types.NEWS:         ANY_ALIASES + ["newspost", "newsposts", "news post", "news posts"],

    types.ADD:          ANY_ALIASES + ["added", "promote", "promoted"],
    types.REMOVE:       ANY_ALIASES + ["removed", "demote", "demoted"]
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

# Includes both full and probationary bns.
BN_ALIASES = ["bn", "bns", "bng", "nominators", "beatmap nominators"]
GROUP_ALIASES: Dict[str, List[str]] = {
    "4": ANY_ALIASES + ["gmt", "gmts", "global moderators", "global moderation team"],
    "7": ANY_ALIASES + ["nat", "nats", "nomination assessment", "nomination assessment team"],
    "11": ANY_ALIASES + ["dev", "devs", "developers"],
    "16": ANY_ALIASES + ["alu", "alumni", "alumnis"],
    "22": ANY_ALIASES + ["sup", "support", "support team"],
    # Exclusively full/probo bns:
    "28": ANY_ALIASES + BN_ALIASES + ["full", "full bn", "full bns", "full beatmap nominators"],
    "32": (ANY_ALIASES + BN_ALIASES + ["probo", "probo bn", "probo bns", "probation", "probation bn",
        "probation bns", "probationary beatmap nominators"])
}

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

def escape(obj: str) -> str:
    """Returns the same object cast to string, but surrounded in quotes if it contains a space."""
    if " " in str(obj):
        return f"\"{obj}\""
    return str(obj)

class Validation():
    """Represents the validation used by a tag to figure out if a value `is_valid`.
    Also contains `hint`, which gives information about which values are considered valid
    (e.g. "Accepts integer values")."""
    def __init__(self, hint: str, is_valid: Callable[[str], bool]):
        self.hint = hint
        self.is_valid = is_valid

class Tag():
    """Represents a possible key-value pair and which conditions it appears in.
    Can both create a value from a given object (e.g. Event or Beatmapset) (None if N/A),
    as well as validate that a given value is valid (e.g. `type` will never have a value of `undefined`)."""
    def __init__(
            self, description: str, value_func: Callable[[object], str], validation: Validation,
            sql_format: str, example_values: List[str]=[]):
        self.description = description
        self.value_func = value_func
        self.validation = validation
        self.sql_format = sql_format
        self.example_values = example_values

def is_int(value: str) -> bool:
    """Returns whether the given string can be parsed as an integer."""
    try:
        int(value)
        return True
    except ValueError:
        return False

VALIDATION_ANY = Validation("Accepts any value.", lambda _: True)
VALIDATION_IDS = Validation("Accepts integer values.", is_int)

def specific_validation(values: List[str]) -> Validation:
    return Validation(
        "\u2000".join(f"`{value}`" for value in values),
        lambda value: value in values
    )

TAGS: Dict[List[str], Tag] = {
    # User tags:
    ("user",): Tag(
        "The username of the user performing the event (e.g. user nominating, replying, or giving kudosu).",
        lambda obj: [escape(obj.name)] if isinstance(obj, User) else None,
        VALIDATION_ANY, sql_format="user.name LIKE %s",
        example_values=["lasse", "\"seto kousuke\""]
    ),
    ("user-id",) : Tag(
        "The id of the user performing the event (e.g. id of user nominating, replying, or giving kudosu).",
        lambda obj: [escape(obj.id)] if isinstance(obj, User) else None,
        VALIDATION_IDS, sql_format="user.id=%s",
        example_values=["896613"]
    ),
    # Beatmapset tags:
    ("set-id", "mapset-id", "beatmapset-id") : Tag(
        "The id of the beatmapset where the event occurred (e.g. id of mapset nominated or discussed).",
        lambda obj: [escape(obj.id)] if isinstance(obj, Beatmapset) else None,
        VALIDATION_IDS, sql_format="beatmapset.id=%s",
        example_values=["41823"]
    ),
    ("artist",) : Tag(
        "The artist field of a beatmapset an event occurred on (e.g. \"LeaF\" in \"Leaf - Doppelganger\").",
        lambda obj: [escape(obj.artist)] if isinstance(obj, Beatmapset) else None,
        VALIDATION_ANY, sql_format="beatmapset.artist LIKE %s",
        example_values=["nhato", "\"the quick brown fox\""]
    ),
    ("title",) : Tag(
        "The title field of a beatmapset an event occurred on (e.g. \"Doppelganger\" in \"Leaf - Doppelganger\").",
        lambda obj: [escape(obj.title)] if isinstance(obj, Beatmapset) else None,
        VALIDATION_ANY, sql_format="beatmapset.title LIKE %s",
        example_values=["uta", "\"miss you\""]
    ),
    ("creator",) : Tag(
        "The username of the creator of a beatmapset an event occurred on (e.g. \"Shurelia\" for any set hosted by them).",
        lambda obj: [escape(obj.creator.name)] if isinstance(obj, Beatmapset) else None,
        VALIDATION_ANY, sql_format="creator.name LIKE %s",
        example_values=["lasse", "\"seto kousuke\""]
    ),
    ("creator-id",) : Tag(
        "The id of the creator of a beatmapset an event occurred on (e.g. \"3807986\" for any set hosted by Shurelia).",
        lambda obj: [escape(obj.creator.id)] if isinstance(obj, Beatmapset) else None,
        VALIDATION_IDS, sql_format="creator.id=%s",
        example_values=["896613"]
    ),
    ("mode",) : Tag(
        "The involved mode of a beatmapset an event occurred on (e.g. \"taiko\" for any set with a taiko map).",
        lambda obj: [escape(mode) for mode in obj.modes] if isinstance(obj, Beatmapset) else None,
        specific_validation(["osu", "taiko", "catch", "mania"]), sql_format="mode=%s",
        example_values=["osu"]
    ),
    # Discussion tags:
    ("discussion-id",) : Tag(
        "The id of the discussion an event occurred on (e.g. \"1589811\" for that specific discussion).",
        lambda obj: [escape(obj.id)] if isinstance(obj, Discussion) else None,
        VALIDATION_IDS, sql_format="discussion.id=%s",
        example_values=["1687831"]
    ),
    ("author",) : Tag(
        "The username of the author of the discussion an event occurred on (e.g. \"Shurelia\" for any discussion started by them).",
        lambda obj: [escape(obj.user.name)] if isinstance(obj, Discussion) else None,
        VALIDATION_ANY, sql_format="author.name LIKE %s",
        example_values=["lasse", "\"seto kousuke\""]
    ),
    ("author-id",) : Tag(
        "The id of the author of the discussion an event occurred on (e.g. \"3807986\" for any discussion started by Shurelia).",
        lambda obj: [escape(obj.user.id)] if isinstance(obj, Discussion) else None,
        VALIDATION_IDS, sql_format="author.id=%s",
        example_values=["896613"]
    ),
    ("discussion-content",) : Tag(
        "The text content of the discussion an event occurred on (e.g. \"blanket\" for any discussion started containing that).",
        lambda obj: [escape(obj.content)] if isinstance(obj, Discussion) else None,
        VALIDATION_ANY, sql_format="discussion.content LIKE %s",
        example_values=["nice", "\"very cool\""]
    ),
    # Group tags:
    ("group",) : Tag(
        # TODO: Have this be the case
        "The name of the group a user was added to or removed from (e.g. \"bns\" for both full and probo BNs).",
        lambda obj: (
            [escape(str(obj.group.id))] +
            ([escape(alias) for alias in get_group_aliases(str(obj.group.id))] if str(obj.group.id) in GROUP_ALIASES else [])
        ) if isinstance(obj, Event) and obj.group else None,
        Validation(
            # Ignore group ids, only show distinct aliases (full bn and probo bn have some identical ones).
            "\u2000".join(list(OrderedDict.fromkeys(f"`{alias}`" for aliases in GROUP_ALIASES.values() for alias in aliases))),
            lambda value: value in get_all_group_aliases()
        ), sql_format="group_id=%s",  # `GROUP_ALIASES` has the group id as key, so this should work.
        example_values=["bns", "nat", "gmt", "devs"]
    ),
    ("group-id",) : Tag(
        "The id of the group a user was added to or removed from (e.g. \"7\" for BAT/QAT/NAT).",
        lambda obj: [escape(obj.group.id)] if isinstance(obj, Event) and obj.group else None,
        VALIDATION_IDS, sql_format="group_id=%s",
        example_values=["4", "7", "28", "32"]
    ),
    # NewsPost tags:
    ("news-title",) : Tag(
        "The title of the newspost (e.g. \"%featured artist%\" for FA news).",
        lambda obj: [escape(obj.title)] if isinstance(obj, NewsPost) else None,
        VALIDATION_ANY, sql_format="newspost.title LIKE %s",
        example_values=["\"New Featured Artist: DragonForce\"", "\"%title contains this%\""]
    ),
    ("news-content", "news-preview") : Tag(
        "The preview of the newspost (e.g. \"We're excited to welcome Lasse as our newest featured artist!\").",
        lambda obj: [escape(obj.preview)] if isinstance(obj, NewsPost) else None,
        VALIDATION_ANY, sql_format="newspost.preview LIKE %s",
        example_values=["\"preview is exactly this\"", "\"%preview contains this%\""]
    ),
    ("news-author",) : Tag(
        "The username of the author of the newspost (e.g. \"Ephemeral\").",
        lambda obj: [escape(obj.author.name)] if isinstance(obj, NewsPost) else None,
        VALIDATION_ANY, sql_format="newspost.author_name LIKE %s",
        example_values=["Ephemeral", "\"The Spotlights Team\"", "\"%contains this%\""]
    ),
    ("news-author-id",) : Tag(
        "The id of the author of the newspost (e.g. \"102335\" for Ephemeral).",
        lambda obj: [escape(obj.author.id)] if isinstance(obj, NewsPost) else None,
        VALIDATION_IDS, sql_format="newspost.author_id=%s",
        example_values=["102335"]
    ),
    # Event tags:
    ("type",) : Tag(
        "The type of an event (e.g. nominate, kudosu_gain, or suggestion). Spaces, dashes, and underscores are interchangable.",
        lambda obj: (
            [escape(obj.type)] +
            ([escape(alias) for alias in get_type_aliases(obj.type)] if obj.type in TYPE_ALIASES else [])
        ) if isinstance(obj, Event) else None,
        Validation(
            "\u2000".join(f"`{alias}`" for alias in TYPE_ALIASES) + "\u2000(+lots of aliases)",  # Becomes too long otherwise.
            lambda value: value in get_all_type_aliases()
        ), sql_format="type=%s",
        example_values=["reset", "nomination-reset", "\"nomination reset\""]
    ),
    ("content",) : Tag(
        "The text content associated with an event (e.g. the text of a reply, disqualification, or discussion). `%` is a wildcard.",
        lambda obj: [escape(obj.content)] if isinstance(obj, Event) and obj.content else None,
        VALIDATION_ANY, sql_format="events.content LIKE %s",
        example_values=["nice", "\"very cool\"", "\"%contains this%\""]
    )
}



def dissect(obj: Union[Event, User, Beatmapset, Discussion]) -> List[str]:
    """Returns a list of lowercased key:value strings representing the given object."""
    dissections = list(dissect_shallow(obj))

    if isinstance(obj, Event):
        if obj.user:       dissections.extend(dissect(obj.user))
        if obj.discussion: dissections.extend(dissect(obj.discussion))
        if obj.beatmapset: dissections.extend(dissect(obj.beatmapset))
        if obj.newspost:   dissections.extend(dissect(obj.newspost))
        if obj.group:      dissections.extend(dissect(obj.group))

    # Lowercase everything for ease-of-access when filtering.
    return list(map(lambda dissection: dissection.lower(), dissections))

def dissect_shallow(obj: Union[Event, User, Beatmapset, Discussion]) -> Generator[str, None, None]:
    """Returns a generator of dissections on the given object without recursion
    (e.g. if on an event, the user properties are not part of the generator)."""
    for keys, tag in TAGS.items():
        for value in (tag.value_func(obj) or []):
            for key in keys:
                yield f"{key}:{value}"

def passes_filter(_filter: str, dissection_or_object: Union[List[str], Event, User, Beatmapset, Discussion]) -> bool:
    """Returns whether the given dissection (or dissection of the given Event/Beatmapset/Discussion/etc.)
    would pass the filter logically. This is case insensitive.

    That is, if all AND within any OR evaluate to True, in the expanded filter."""
    if (
        isinstance(dissection_or_object, Event) or
        isinstance(dissection_or_object, User) or
        isinstance(dissection_or_object, Beatmapset) or
        isinstance(dissection_or_object, Discussion) or
        isinstance(dissection_or_object, NewsPost)
    ):
        dissection = dissect(dissection_or_object)
    else:
        dissection = dissection_or_object

    _filter = _filter.lower()
    for or_split, _ in split_unescaped(expand(_filter), OR_GATES):
        
        passes_and = True
        for and_split, _ in split_unescaped(or_split, AND_GATES):
            without_not_gate, not_gate = extract_not(and_split)
            if not_gate:
                if without_not_gate in dissection:
                    passes_and = False
            else:
                if and_split not in dissection:
                    passes_and = False
        
        if passes_and:
            return True

    return False



def get_tag(tag_key: str) -> Tag:
    """Returns the tag associated with this key, case insensitive."""
    for tag_keys, tag in TAGS.items():
        if tag_key.lower() in map(lambda key: key.lower(), tag_keys):
            return tag
    return None

def get_tag_keys(tag_key: str) -> List[str]:
    """Returns all keys associated with this key, case insensitive."""
    for tag_keys, tag in TAGS.items():
        if tag_key.lower() in map(lambda key: key.lower(), tag_keys):
            return tag_keys
    return None

def get_key_value_pairs(_filter: str) -> Generator[Tuple[str, str], None, None]:
    """Returns a generator of key-value pair tuples from the given filter."""
    expansion = expand(_filter)
    for match in re.finditer(KEY_VALUE_PATTERN, expansion):
        yield (match.group(1), match.group(2).strip("\""))

def get_invalid_keys(_filter: str) -> Generator[str, None, None]:
    """Returns a generator of invalid keys from the given filter."""
    for key, _ in get_key_value_pairs(_filter):
        if not get_tag(key):
            yield key

def get_invalid_filters(_filter: str) -> Generator[str, None, None]:
    """Returns a generator of invalid key-value pair tuples from the given filter."""
    for key, value in get_key_value_pairs(_filter):
        if not get_tag(key).validation.is_valid(value.lower()):
            yield (key, value)

def get_invalid_words(_filter: str) -> Generator[str, None, None]:
    """Returns all space-separated instances of text, which are neither key-value
    pairs nor logical gates, in the given filter."""
    for split, _ in split_unescaped(expand(_filter), delimiters=[" "]):
        is_key_value_pair = re.match(KEY_VALUE_PATTERN, split)
        is_logical_gate = split.lower() in map(lambda gate: gate.replace(" ", ""), NOT_GATES + AND_GATES + OR_GATES)
        if not is_key_value_pair and not is_logical_gate:
            yield split

def is_valid(_filter: str) -> bool:
    if (
        list(get_invalid_keys(_filter)) or
        list(get_invalid_filters(_filter)) or
        list(get_invalid_words(_filter))
    ):
        return False
    return True



def filter_to_sql(_filter: str) -> (str, tuple):
    """Returns a tuple of the filter converted to an SQL WHERE clause and the inputs to the
    WHERE clause (e.g. ("type=%s", ("nominate",)) ), for use with the scraper database."""
    if not _filter:
        # Without a filter, we simply let everything through.
        return ("TRUE", ())

    if not is_valid(_filter):
        raise ValueError("Received an invalid filter; cannot convert to sql.")

    converted_words = []
    converted_values = []
    for word, _ in split_unescaped(expand(_filter), delimiters=[" "]):
        # Convert gate symbols in the filter (e.g. "&", "!", "and", "|") to "AND", "OR", and "NOT".
        if any(map(lambda gate: word.lower() == gate.strip().lower(), AND_GATES)): word = "AND"
        if any(map(lambda gate: word.lower() == gate.strip().lower(), OR_GATES)):  word = "OR"
        if any(map(lambda gate: word.lower() == gate.strip().lower(), NOT_GATES)): word = "NOT"
        if word in ["AND", "OR", "NOT"]:
            converted_words.append(word)
            continue

        key, value = next(get_key_value_pairs(word))
        tag = get_tag(key)
        if not tag:
            continue

        values = []

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

        if not values:
            # Our value is not an alias, so we can use it directly.
            values.append(value)

        if len(values) > 1: converted_words.append("(" + " OR ".join([tag.sql_format] * len(values)) + ")")
        else:               converted_words.append(tag.sql_format)
        converted_values.extend(values)
    
    return (" ".join(converted_words), tuple(converted_values))
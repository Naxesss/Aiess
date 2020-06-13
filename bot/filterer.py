import sys
sys.path.append('..')

from typing import Union, List, Generator, Tuple, Match, Dict, Callable
import re

from aiess import Event, User, Beatmapset, Discussion
from aiess import event_types as types

AND_GATES = [" and ", "&", "∧"]
OR_GATES  = [" or ",  "|", "∨"]
NOT_GATES = ["not ",  "!", "¬"]

# Regular expression for cases like "not A and (not B or not C)"
# Any group captured may be removed.
NOT_GATE_PATTERNS = ["(?:(?:^|[^A-Za-z0-9_ ])|( ))(not)(?:(?:[^A-Za-z0-9_ ])|( ))", "(!)", "(¬)"]

KEY_VALUE_PATTERN = "(\"[^\"]+.|[^ ]+):(\"[^\"]+.|[^ ]+)"

QUOTE_CHARS = ["\"", "“", "”"]

# Any of these values can be substituted for the respective key;
# if the user expects it to work, it should work.
TYPE_ALIASES: Dict[str, List[str]] = {
    types.RANK:         ["ranked"],
    types.LOVE:         ["loved"],
    types.QUALIFY:      ["qualified",        "qualification",    "qual"],
    types.DISQUALIFY:   ["disqualified",     "disqualification", "dq"],
    types.NOMINATE:     ["nominated",        "nomination",       "nom",   "bubble", "bubbled"],
    types.RESET:        ["nomination reset",                     "reset", "pop",    "popped"],

    types.SUGGESTION:   [],
    types.PROBLEM:      [],
    types.NOTE:         ["mapper note", "note"],
    types.PRAISE:       [],
    types.HYPE:         [],
    types.REPLY:        [],

    types.RESOLVE:      ["issue resolve", "issue resolved", "resolve", "resolved"],
    types.REOPEN:       ["issue reopen",  "issue reopened", "reopen",  "reopened"],

    types.KUDOSU_GAIN:  ["kudosu gain",  "kudosu gained", "kudosu given"],
    types.KUDOSU_LOSS:  ["kudosu loss",  "kudosu lost",   "kudosu taken"],
    types.KUDOSU_DENY:  ["kudosu deny",  "kudosu denied"],
    types.KUDOSU_ALLOW: ["kudosu allow", "kudosu allowed"]
}

def escape(obj: str) -> str:
    """Returns the same object cast to string, but surrounded in quotes if it contains a space."""
    if " " in str(obj):
        return f"\"{obj}\""
    return str(obj)

# The keys and values of `TYPE_ALIASES` together make up all recognized types.
VALID_TYPES = [escape(key) for key in TYPE_ALIASES]
VALID_TYPES.extend(escape(alias) for aliases in TYPE_ALIASES.values() for alias in aliases)

def is_int(value: str) -> bool:
    """Returns whether the given string can be parsed as an integer."""
    try:
        int(value)
        return True
    except:
        return False

# Used for checking whether a key-value pair is recognized and valid (e.g. "type:asdf" and
# "user-id:test" are both invalid; first is an unrecognized type, second is not an id).
VALID_FILTERS: Dict[str, Callable[[str], bool]] = {
    # `dissect_user`
    "user":                 lambda _: True,
    "user-id":              is_int,
    # `dissect_beatmapset`
    "mapset-id":            is_int,
    "artist":               lambda _: True,
    "title":                lambda _: True,
    "creator":              lambda _: True,
    "creator-id":           is_int,
    "mode":                 lambda value: value in ["osu", "taiko", "catch", "mania"],
    # `dissect_discussion`
    "discussion-id":        is_int,
    "author":               lambda _: True,
    "author-id":            is_int,
    "discussion-content":   lambda _: True,
    # `dissect_event`
    "type":                 lambda value: value in VALID_TYPES,
    "content":              lambda _: True
}



def expand(string: str) -> str:
    """Converts the given expression into disjunctive normal form.
    Supports literal, programatic and mathematical boolean operators (e.g. "and", "&", as well as "∧").
    
    As an example,
    \"A ∨ E ∧ ¬(B ∧ (C ∨ ¬D))\"
    would be converted to
    \"A ∨ E ∧ ¬B ∨ E ∧ ¬C ∧ E ∧ D\"."""

    # e.g. "!(A & B)" -> "(!A | !B)"
    string = de_morgans_law(string)

    # Performing expansion individually for each OR group ensures we don't
    # get stuck in an infinite loop for inputs such as:
    # "(A or B) and (C or D)" -> "A and (C or D) or B and (C or D)"
    temp_string = ""
    has_delimiter = False
    for split, delimiter in split_unescaped(string, OR_GATES):
        if delimiter:
            has_delimiter = True
        
        if has_delimiter:
            temp_string += expand(split) + (delimiter if delimiter else "")
        else:
            temp_string += split
    
    dist_string = distribute(temp_string)
    if string == dist_string:
        return string

    return expand(dist_string)



def distribute(string: str) -> str:
    """Returns an equivalent more distributed expression
    (e.g. "abc(type:(A and B))" -> "abc(type:A and type:B)")."""
    start, end = deepest_parentheses_range(string)
    if not start and not end:
        # No more parentheses, we're done after normalizing NOT gates.
        # e.g. "type:not nominate" -> "not type:nominate"
        return normalize_not(string)

    # first some (things or here (and then more) along with) even more
    #             ^^^^^^^^^^^^^^^               ^^^^^^^^^^^
    #             pre                           post
    #                      ^^^^^^               ^^^^^^^^^^^
    #                      pre_or               post_or

    content = string[start+1:end]
    pre = backwards_leveled(string[:start])
    post = forwards_leveled(string[end+1:])

    pre_or = None
    for pre_or, _ in split_unescaped(pre, OR_GATES):
        pass
    post_or, _ = next(split_unescaped(post, OR_GATES))

    # In this case there's no difference between AND or OR gates, as they maintain their relative orders.
    # e.g. "pre(x | y & z)post" would just become "prexpost | preypost & prezpost"
    expanded_content = pre[:-len(pre_or)]
    for split, gate in split_unescaped(content, AND_GATES + OR_GATES):
        split = surround_nonspace(split, pre_or, post_or)
        expanded_content += split + (gate if gate else "")
    expanded_content += post[len(post_or):]

    # first some (things or here (and then more) along with) even more
    # ^^^^^^^^^^^^               ^             ^           ^^^^^^^^^^^
    # pre_start                  start         end         post_end

    pre_start = string[:start - len(pre)]
    post_end = string[end + len(post) + 1:]

    return cleanup(pre_start + expanded_content + post_end)

def cleanup(string: str) -> str:
    """Returns the string without double spaces and without pairs of parentheses around."""
    while "  " in string:
        string = string.replace("  ", " ")
    
    while string.startswith("(") and string.endswith(")"):
        string = string[1:-1]
    
    return string

def parenthesis_equal(string: str) -> bool:
    """Returns whether this string has an equal amount of opening and closing parentheses."""
    parentheses = 0
    for char in string:
        if char == "(": parentheses += 1
        if char == ")": parentheses -= 1
    return parentheses == 0

def deepest_parentheses(string: str) -> str:
    """Returns the string within the deepest level of parentheses, without the parentheses. Raises ValueError on parenthesis inequality."""
    start, end = deepest_parentheses_range(string)
    return string[start:end].strip("()")

def deepest_parentheses_range(string: str) -> [Union[int, None], Union[int, None]]:
    """Returns a tuple of the indexes of the first deepest level of opening and closing parenthesis.
    Raises ValueError on parenthesis inequality."""
    if not parenthesis_equal(string):
        raise ValueError("There are not an equal amount of opening and closing parentheses.")

    depth = 0
    deepest = 0
    first_deepest = False
    deepest_start = None
    deepest_end = None

    for index, char in enumerate(string):
        if char == "(":
            depth += 1
            if depth > deepest:
                deepest = depth
                deepest_start = index
                first_deepest = True
        if char == ")":
            if depth == deepest and first_deepest:
                deepest_end = index
                first_deepest = False
            depth -= 1
    
    return (deepest_start, deepest_end)

def backwards_leveled(string: str) -> str:
    """Returns the content before a given position in the string, until our parenthesis level reduces
    (i.e. more opening parentheses are hit than closing ones)."""
    read = ""
    level = 0
    for char in reversed(string):
        if char == "(": level -= 1  # Reading backwards, so we're stepping behind this.
        if char == ")": level += 1
        if level < 0:
            break
        read = char + read  # Reading backwards, so prepend.
    return read

def forwards_leveled(string: str) -> str:
    """Returns the content after a given position in the string, until our parenthesis level reduces
    (i.e. more closing parentheses are hit than opening ones)."""
    read = ""
    level = 0
    for char in string:
        if char == "(": level += 1
        if char == ")": level -= 1
        if level < 0:
            break
        read += char
    return read

def split_unescaped(string: str, delimiters: List[str]) -> Generator[Tuple[str, str], None, None]:
    """Returns a generator of tuples consisting of splits and their respective following
    unescaped delimiters (or None if at the end) from the given string. Escaped delimiters are ones
    inside quotes or parentheses.
    
    So for example splitting \"\"A|B\"|C\" by \"|\" would result in (\"\"A|B\"\", \"|\") and (\"C\", None)."""
    read = ""
    quotes = 0
    parentheses = 0
    for char in string:
        
        if char in QUOTE_CHARS:
            # So, "this "would work"", but "not"this"".
            if not quotes or read.endswith(" "):
                quotes += 1
            else:
                quotes -= 1
        
        if char == "(": parentheses += 1
        if char == ")": parentheses -= 1
        
        read += char

        # Quotes and parentheses are considered escaped, so we ignore delimiters inside them.
        if not quotes and not parentheses:
            for delimiter in delimiters:
                if read.endswith(delimiter):
                    split = read[:-len(delimiter)]  # Don't include the delimiter itself in the split.
                    yield (split, delimiter)
                    read = ""
    
    yield (read, None)

def de_morgans_law(string: str) -> str:
    """Returns the equivalent boolean expression without NOT gates in front of parentheses,
    including double negation elimination."""
    string = double_negation_elimination(string)

    found_not_gate = None
    not_gate_start, not_gate_end = (None, None)
    needs_negating = None
    needs_negating_index = -1
    read = ""
    for index, char in enumerate(string):
        read += char

        if char == "(":
            for pattern_index, not_gate_pattern in enumerate(NOT_GATE_PATTERNS):
                match = None
                for temp_match in re.finditer(not_gate_pattern, read):
                    if not any(gate in read[temp_match.start(0):] for gate in (AND_GATES + OR_GATES)):
                        match = temp_match

                if match:
                    found_not_gate = NOT_GATES[pattern_index]
                    not_gate_start, not_gate_end = match.span()

                    needs_negating = forwards_leveled(string[index + 1:])
                    needs_negating_index = index + 1
                    break
        
        if found_not_gate:
            break
    
    if not needs_negating:
        return string
    
    # Excludes the found NOT gate.
    prefix = string[:not_gate_start] + string[not_gate_end:needs_negating_index - len("(")]
    postfix = string[needs_negating_index + len(needs_negating) + len(")"):]

    negated_part = negate(needs_negating, not_gate=found_not_gate)
    negated_part = double_negation_elimination(negated_part)

    # Recursively try to negate parentheses until no longer needed.
    return de_morgans_law(prefix + "(" + negated_part + ")" + postfix)

def negate(string: str, not_gate: str="!") -> str:
    """Returns an expression where everything in the string outside parentheses is negated, including OR and AND gates.
    Uses "!" as not gate, unless another is given."""

    reconstruction = ""
    for or_split, or_gate in split_unescaped(string, OR_GATES):

        # e.g. "A & B" -> "A | B"
        and_temp = ""
        for and_split, and_gate in split_unescaped(or_split, AND_GATES):
            and_split = surround_nonspace(and_split, not_gate, "")
            if and_gate: and_temp += and_split + flip_gate(and_gate)
            else:        and_temp += and_split
        
        # e.g. "A " -> "A ", but "A | B " -> "(A | B) "
        if any(or_gate in and_temp for or_gate in OR_GATES):
            and_temp = surround_nonspace(and_temp, "(", ")")

        if or_gate: reconstruction += and_temp + flip_gate(or_gate)
        else:       reconstruction += and_temp
    
    return reconstruction

def flip_gate(gate: str) -> str:
    """Returns any AND gate as the equivalent OR gate, and visa versa. So "&" would return "|", "∨" returns "∧", etc.
    If no such gate exists, we raise a ValueError."""
    for index, and_gate in enumerate(AND_GATES):
        if gate == and_gate:
            return OR_GATES[index]
    
    for index, or_gate in enumerate(OR_GATES):
        if gate == or_gate:
            return AND_GATES[index]
    
    raise ValueError(f"Cannot flip the gate \"{gate}\".")

def double_negation_elimination(string: str) -> str:
    """Returns the same string, but where all double NOT gates are removed, including mixed gate symbols
    (e.g. "not type:!A" -> "type:A")."""
    read = ""
    for char in string:
        read += char

        matches = []
        for pattern in NOT_GATE_PATTERNS:
            for match in re.finditer("(?=(?:" + pattern + "))", read):
                if not any(gate in read[match.start(0):] for gate in (AND_GATES + OR_GATES + ["(", ")"])):
                    matches.append(match)

        if len(matches) > 1:
            start1, end1 = combined_captured_span(matches[0])
            start2, end2 = combined_captured_span(matches[1])

            # Recursively remove double NOT gates.
            string = string[:start1] + string[end1:start2] + string[end2:]
            return double_negation_elimination(string)

    # No more double NOT gates.
    return string

def normalize_not(string: str) -> str:
    """Returns the string, but where NOT gates are moved as far back in the string as possible without
    changing the expression. Only works for expressions in disjunctive normal form."""
    reconstruction = ""
    for split, gate in split_unescaped(string, AND_GATES + OR_GATES):

        without_not_gate, not_gate = extract_not(split)

        normalized_split = surround_nonspace(without_not_gate, not_gate, "") if not_gate else split
        reconstruction += normalized_split + (gate if gate else "")
    
    return reconstruction

def extract_not(expr: str) -> (str, str):
    """Returns a tuple of the given expression without the first NOT gate found and
    the NOT gate that was found, if any, otherwise None."""
    for index, pattern in enumerate(NOT_GATE_PATTERNS):
        match = re.search(pattern, expr)
        if match:
            not_gate = NOT_GATES[index]
            start, end = combined_captured_span(match)
            without_not_gate = expr[:start] + expr[end:]

            return (without_not_gate, not_gate)
    
    return (expr, None)

def surround_nonspace(string: str, pre: str, post: str) -> str:
    """Returns the string surrounded by the given characters, maintaining spaces outside the surrounding."""
    pre_spaces = ""
    for char in string:
        if char == " ": pre_spaces += char
        else:           break
    
    post_spaces = ""
    for char in reversed(string):
        if char == " ": post_spaces += char
        else:           break

    string = string.strip(" ")
    return pre_spaces + pre + string + post + post_spaces

def combined_captured_span(match: Match) -> (int, int):
    """Returns the span of all capture groups in the match. That is, from the first start to the last end."""
    first_start = None
    last_end = None
    for start, end in match.regs[1:]:
        if (first_start is None or first_start > start) and start >= 0:
            first_start = start
        if (last_end is None or last_end < end) and end >= 0:
            last_end = end

    return first_start, last_end



def dissect(obj: Union[Event, User, Beatmapset, Discussion]) -> List[str]:
    """Returns a list of lowercased key:value strings representing the given object."""
    dissections = []

    if isinstance(obj, User):         dissections.extend(list(dissect_user(obj)))
    elif isinstance(obj, Beatmapset): dissections.extend(list(dissect_beatmapset(obj)))
    elif isinstance(obj, Discussion): dissections.extend(list(dissect_discussion(obj)))
    elif isinstance(obj, Event):      dissections.extend(list(dissect_event(obj)))

    # Lowercase everything for ease-of-access when filtering.
    return list(map(lambda dissection: dissection.lower(), dissections))

def dissect_user(user: User) -> Generator[str, None, None]:
    yield f"user:{escape(user.name)}"
    yield f"user-id:{escape(user.id)}"

def dissect_beatmapset(beatmapset: Beatmapset) -> Generator[str, None, None]:
    yield f"mapset-id:{escape(beatmapset.id)}"
    yield f"artist:{escape(beatmapset.artist)}"
    yield f"title:{escape(beatmapset.title)}"
    yield f"creator:{escape(beatmapset.creator.name)}"
    yield f"creator-id:{escape(beatmapset.creator.id)}"
    for mode in beatmapset.modes:
        yield f"mode:{escape(mode)}"
    
def dissect_discussion(discussion: Discussion) -> Generator[str, None, None]:
    yield from dissect_beatmapset(discussion.beatmapset)
    
    yield f"discussion-id:{escape(discussion.id)}"
    yield f"author:{escape(discussion.user.name)}"
    yield f"author-id:{escape(discussion.user.id)}"
    yield f"discussion-content:{escape(discussion.content)}"

def dissect_event(event: Event) -> Generator[str, None, None]:
    yield f"type:{escape(event.type)}"

    if event.type in TYPE_ALIASES:
        for alias in TYPE_ALIASES[event.type]:
            yield f"type:{escape(alias)}"

    # The dissection of the discussion includes the dissection of the beatmapset, if present.
    if event.discussion: yield from dissect(event.discussion)
    else:                yield from dissect(event.beatmapset)
    
    if event.user:    yield from dissect(event.user)
    if event.content: yield f"content:{escape(event.content)}"

def passes_filter(_filter: str, dissection: List[str]) -> bool:
    """Returns whether the dissection would pass the filter logically. This is case insensitive.

    That is, if all AND within any OR evaluate to True, in the expanded filter."""
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



def get_key_value_pairs(_filter: str) -> Generator[Tuple[str, str], None, None]:
    """Returns a generator of key-value pair tuples from the given filter."""
    expansion = expand(_filter)
    for match in re.finditer(KEY_VALUE_PATTERN, expansion):
        yield (match.group(1), match.group(2))

def get_invalid_keys(_filter: str) -> Generator[str, None, None]:
    """Returns a generator of invalid keys from the given filter."""
    for key, _ in get_key_value_pairs(_filter):
        if key.lower() not in VALID_FILTERS:
            yield key

def get_invalid_filters(_filter: str) -> Generator[str, None, None]:
    """Returns a generator of invalid key-value pair tuples from the given filter."""
    for key, value in get_key_value_pairs(_filter):
        if not VALID_FILTERS[key.lower()](value.lower()):
            yield (key, value)

def get_invalid_words(_filter: str) -> Generator[str, None, None]:
    """Returns all space-separated instances of text, which are neither key-value
    pairs nor logical gates, in the given filter."""
    for split in expand(_filter).split(" "):
        is_key_value_pair = re.match(KEY_VALUE_PATTERN, split)
        is_logical_gate = split.lower() in map(lambda gate: gate.replace(" ", ""), NOT_GATES + AND_GATES + OR_GATES)
        if not is_key_value_pair and not is_logical_gate:
            yield split
import sys
sys.path.append('..')

from typing import Union, List, Generator, Callable, Tuple
import re

from aiess import Event

from bot.logic import expand, split_unescaped, extract_not
from bot.logic import AND_GATES, OR_GATES, NOT_GATES, QUOTE_CHARS

KEY_VALUE_PATTERN = r"(\"[^\"]+.|[^ ]+):(\"[^\"]+.|[^ ]+)"

class Tag():
    """Used in filtering to find specific aspects of objects (e.g. the name of a user).
    
    - `names` :
        A list of strings determining which keys are associated to this tag in any key:value pair.
    - `description` :
        A string describing what aspect of an object this tag represents.
    - `example_values` :
        A list of strings showing examples of values that this tag accepts.
    - `value_hint` :
        A string showing what type of value this tag accepts in general.
    - `value_predicate` :
        A function given a string returning True if the string is a valid value for this tag.
    - `value_func` :
        A function given an object returning a list of key:value pairs representing that object.
    - `value_convert` :
        A function given a string value returning a either a new string value or None if no conversion is needed."""
    def __init__(
            self, names: List[str], description: str, example_values: List[str], value_hint: str,
            value_predicate: Callable[[str], bool], value_func: Callable[[Event], List[str]],
            value_convert: Callable[[str], str]=None
        ):
        self.names           = names
        self.description     = description
        self.example_values  = example_values
        self.value_hint      = value_hint
        self.value_predicate = value_predicate
        self.value_func      = value_func
        self.value_convert   = value_convert

class FilterContext():
    """Determines how any filter passed into this class should behave
    (e.g. which tags are valid and how objects are broken down into tags)."""
    def __init__(self, name: str, examples: List[str], tags: List[Tag]):
        self.name = name
        self.examples = examples
        self.tags = tags
    
    def get_tag(self, name: str) -> Tag:
        """Returns the tag associated with this key, case insensitive, if any, else None."""
        for tag in self.tags:
            if name.lower() in map(str.lower, tag.names):
                return tag
        return None
    
    def dissect(self, obj: object) -> List[str]:
        """Returns a list of lowercased key:value strings representing the given object in this context."""
        dissections = list(self.dissect_shallow(obj))
        # Lowercase everything for ease-of-access when filtering.
        return list(map(lambda dissection: dissection.lower(), dissections))
    
    def dissect_shallow(self, obj: object) -> Generator[str, None, None]:
        """Returns a generator of dissections on the given object,
        based on the tags of this filter context."""
        for tag in self.tags:
            for value in (tag.value_func(obj) or []):
                for name in tag.names:
                    yield f"{name}:{value}"

    def test(self, _filter: str, obj_or_dissection: Union[object, List[str]]) -> bool:
        """Tests the given filter against the dissection of an object.
        Returns whether the key:value pairs match logically. Case insensitive.
        
        That is, if all AND sections within any OR section evaluate to True, in the expanded filter."""
        if isinstance(obj_or_dissection, list):
            dissection = obj_or_dissection
        else:
            dissection = self.dissect(obj_or_dissection)

        _filter = _filter.lower()
        for or_split, _ in split_unescaped(expand(_filter), OR_GATES):
            
            passes_and = True
            for and_split, _ in split_unescaped(or_split, AND_GATES):
                without_not_gate, not_gate = extract_not(and_split)
                if not_gate:
                    if self.test_kvpair(without_not_gate, dissection):
                        passes_and = False
                        break
                else:
                    if not self.test_kvpair(and_split, dissection):
                        passes_and = False
                        break
            
            if passes_and:
                return True

        return False

    def test_kvpair(self, kvpair, dissections) -> bool:
        """Returns true if this key-value pair filter (e.g. "type:nominate") exists within given dissections (e.g.
        ["type:nominate", "creator:xyz", ...]). If the tag has a conversion function for the key-value pair, it
        is ran first and its result used instead (e.g. tags:"abc efg" -> tags:abc and tags:efg)."""
        for key, value in get_key_value_pairs(kvpair):
            tag = self.get_tag(key)
            if tag.value_convert is not None and tag.value_convert(value) is not None:
                return self.test(f"{key}:{tag.value_convert(value)}", dissections)
        
        return any(wildcard_sensitive_in(kvpair, dissection) for dissection in dissections)

def wildcard_sensitive_in(substring: str, full_string: str) -> bool:
    """Returns whether the given substring exists in the given full string,
    taking into account any wildcards in the substring. Acceptable wildcards are
    `%` and `_`."""
    if "%" not in substring and "_" not in substring:
        # No wildcards, so just check for equality.
        return substring == full_string

    pattern = (
        "^" +
        re.escape(substring)
            .replace("%", "(.*)")
            .replace("_", ".") +
        "$"
    )
    match = re.search(pattern, full_string)

    if match: return True
    else:     return False

def escape(obj: str) -> str:
    """Returns the same object cast to string, but surrounded in quotes if it contains a space."""
    if " " in str(obj):
        return f"\"{obj}\""
    return str(obj)

def unescape(string: str) -> str:
    """Returns the string without surrounding quotes recursively, accounts for different quote symbols."""
    if string.startswith(tuple(QUOTE_CHARS)) and string.endswith(tuple(QUOTE_CHARS)):
        return unescape(string[1:-1])
    return string

def is_int(value: str) -> bool:
    """Returns whether the given string can be parsed as an integer."""
    try:
        int(value)
        return True
    except ValueError:
        return False

def get_key_value_pairs(_filter: str) -> Generator[Tuple[str, str], None, None]:
    """Returns a generator of key-value pair tuples from the given filter."""
    expansion = expand(_filter)
    for match in re.finditer(KEY_VALUE_PATTERN, expansion):
        yield (match.group(1), match.group(2).strip("\""))

def get_invalid_gates(_filter: str) -> Generator[str, None, None]:
    """Returns a generator of invalid gates from the given filter (i.e. starting or ending the filter with one)."""
    expanded_filter = expand(_filter).strip()
    for gate in map(lambda g: g.strip(), (AND_GATES + OR_GATES)):
        if expanded_filter.startswith(gate) or expanded_filter.endswith(gate):
            yield gate

def get_invalid_keys(_filter: str, filter_context: FilterContext) -> Generator[str, None, None]:
    """Returns a generator of invalid keys from the given filter."""
    for key, _ in get_key_value_pairs(_filter):
        if not filter_context.get_tag(key):
            yield key

def get_invalid_filters(_filter: str, filter_context: FilterContext) -> Generator[str, None, None]:
    """Returns a generator of invalid key-value pair tuples from the given filter."""
    for key, value in get_key_value_pairs(_filter):
        if not filter_context.get_tag(key).value_predicate(value.lower()):
            yield (key, value)

def get_invalid_words(_filter: str) -> Generator[str, None, None]:
    """Returns all space-separated instances of text, which are neither key-value
    pairs nor logical gates, in the given filter."""
    for split, _ in split_unescaped(expand(_filter), (" ",)):
        is_key_value_pair = re.match(KEY_VALUE_PATTERN, split)
        is_logical_gate = split.lower() in map(lambda gate: gate.replace(" ", ""), NOT_GATES + AND_GATES + OR_GATES)
        if not is_key_value_pair and not is_logical_gate:
            yield split

def get_missing_gate(_filter: str) -> Generator[str, None, None]:
    """Returns a tuple of the first two space-separated instances of text,
    which have no gate between them, in the given filter."""
    was_gate = False
    prev_split = None
    for split, _ in split_unescaped(expand(_filter), (" ",)):
        is_key_value_pair = re.match(KEY_VALUE_PATTERN, split)
        is_logical_gate = split.lower() in map(lambda gate: gate.replace(" ", ""), NOT_GATES + AND_GATES + OR_GATES)

        if prev_split and is_key_value_pair and not was_gate:
            return (prev_split, split)
        
        was_gate = is_logical_gate
        prev_split = split

def is_valid(_filter: str, filter_context: FilterContext) -> bool:
    if (
        list(get_invalid_gates(_filter)) or
        list(get_invalid_keys(_filter, filter_context)) or
        list(get_invalid_filters(_filter, filter_context)) or
        list(get_invalid_words(_filter))
    ):
        return False
    return True
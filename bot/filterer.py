from typing import Union, List, Generator, Tuple

from aiess import Event, User, Beatmapset, Discussion

and_gates = [" and ", "&", "∧"]
or_gates  = [" or ",  "|", "∨"]
not_gates = [" not ", "!", "¬"]

quote_chars = ["\"", "“", "”"]

def expand(string: str) -> str:
    """Converts the given expression into disjunctive normal form.
    Supports literal, programatic and mathematical boolean operators (e.g. "and", "&", as well as "∧").
    
    As an example,
    \"A ∨ E ∧ ¬(B ∧ (C ∨ ¬D))\"
    would be converted to
    \"A ∨ ¬B ∧ E ∨ ¬C ∧ D ∧ E\"."""
    # TODO: Implement NOT gate functionality; De Morgan's laws and double negation elimination.

    # Performing expansion individually for each OR group ensures we don't
    # get stuck in an infinite loop for inputs such as:
    # "(one or two) and (three or four)" -> "one and (three or four) or two and (three or four)"
    temp_string = ""
    has_delimiter = False
    for split, delimiter in split_unescaped(string, or_gates):
        if delimiter:
            has_delimiter = True
        
        if has_delimiter:
            temp_string += expand(split) + (delimiter if delimiter else "")
        else:
            temp_string += split
    
    string = temp_string

    start, end = deepest_parentheses_range(string)
    if not start and not end:
        # No more parentheses, we're done.
        return string

    # first some (things here (and then more) along with) even more
    #             ^^^^^^^^^^^^               ^^^^^^^^^^^
    #             pre                        post

    content = string[start+1:end]
    pre = backwards_leveled(string[:start])
    post = forwards_leveled(string[end+1:])

    # In this case there's no difference between AND or OR gates, as they maintain their relative orders.
    # e.g. "pre(x | y & z)post" would just become "prexpost | preypost & prezpost"
    expanded_content = ""
    for split, delimiter in split_unescaped(content, and_gates + or_gates):
        expanded_content += pre + split + post + (delimiter if delimiter else "")

    # first some (things here (and then more) along with) even more
    # ^^^^^^^^^^^^            ^             ^           ^^^^^^^^^^^
    # pre_start               start         end         post_end

    pre_start = string[:start - len(pre)]
    post_end = string[end + len(post) + 1:]
    string = pre_start + expanded_content + post_end
  
    return expand(string)



def escape(string: str) -> str:
    """Returns the same string but surrounded in quotes if it contains a space."""
    if " " in string:
        return f"\"{string}\""
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
        
        if char in quote_chars:
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

def flip_gate(gate: str) -> str:
    """Returns any AND gate as the equivalent OR gate, and visa versa. So "&" would return "|", "∨" returns "∧", etc.
    If no such gate exists, we raise a ValueError."""
    for index, and_gate in enumerate(and_gates):
        if gate == and_gate:
            return or_gates[index]
    
    for index, or_gate in enumerate(or_gates):
        if gate == or_gate:
            return and_gates[index]
    
    raise ValueError(f"Cannot flip the gate \"{gate}\".")

def double_negation_elimination(string: str) -> str:
    """Returns the same string, but where all double NOT gates are removed."""
    return string.replace("!!", "")

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



def dissect(obj: Union[Event, User, Beatmapset, Discussion]) -> List[str]:
    """Returns a list of key:value strings representing the given object."""
    dissections = []

    if isinstance(obj, User):
        dissections.append(f"user:{escape(obj.name)}")
        dissections.append(f"user-id:{escape(obj.id)}")
    
    elif isinstance(obj, Beatmapset):
        dissections.append(f"mapset-id:{escape(obj.id)}")
        dissections.append(f"artist:{escape(obj.artist)}")
        dissections.append(f"title:{escape(obj.title)}")
        dissections.append(f"creator:{escape(obj.creator.name)}")
        dissections.append(f"creator-id:{escape(obj.creator.id)}")
        for mode in obj.modes:
            dissections.append(f"mode:{escape(mode)}")
    
    elif isinstance(obj, Discussion):
        dissections.extend(dissect(obj.beatmapset))
        
        dissections.append(f"discussion-id:{escape(obj.id)}")
        dissections.append(f"author:{escape(obj.user.name)}")
        dissections.append(f"author-id:{escape(obj.user.id)}")
        dissections.append(f"discussion-content:{escape(obj.content)}")
    
    elif isinstance(obj, Event):
        dissections.append(f"type:{escape(obj.type)}")

        # The dissection of the discussion includes the dissection of the beatmapset, if present.
        if obj.discussion:
            dissections.extend(dissect(obj.discussion))
        else:
            dissections.extend(dissect(obj.beatmapset))
        
        if obj.user:
            dissections.extend(dissect(obj.user))
        if obj.content:
            dissections.append(f"content:{escape(obj.content)}")

    return dissections
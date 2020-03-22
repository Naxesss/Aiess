from typing import Union, List

from aiess import Event, User, Beatmapset, Discussion

def escape(string: str) -> str:
    if " " in string:
        return f"\"{string}\""
    return string

def expand(string: str) -> str:
    pass

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
def dissect(obj: Union[Event, User, Beatmapset, Discussion]) -> List[str]:
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
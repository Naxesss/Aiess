from typing import Union

from aiess import Event, User, Beatmapset, Discussion

def escape(string: str):
    if " " in string:
        return f"\"{string}\""
    return string

def expand(string: str):
    pass

def dissect(obj: Union[Event, User, Beatmapset, Discussion]):
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
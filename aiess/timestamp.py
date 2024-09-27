from datetime import datetime
from contextlib import suppress
import os
import tempfile

from aiess.settings import ROOT_PATH

PATH_PREFIX = ROOT_PATH + "time/"

TIME_FORMAT     = "%Y-%m-%d %H:%M:%S"      # e.g. "2020-01-12 05:00:00"
TIME_FORMAT_TZ  = "%Y-%m-%dT%H:%M:%S%z"    # e.g. "2020-01-12T05:00:00+00:00"
TIME_FORMAT_TZ2 = "%Y-%m-%dT%H:%M:%S.%fZ"  # e.g. "2020-01-12T05:00:00.302Z"

FILE_NAME_PREFIX = "last_datetime-"
FILE_NAME_POSTFIX = ".txt"

def get_last(_id: str=None) -> datetime:
    """Returns the last datetime we're done with for this id. If the file doesn't exist, one will be created
    with the current time in UTC as datetime."""
    # Only in cases where the file does not already exist do we want to create and initialize one.
    # In any other case we should throw an exception if data is missing (e.g. corruption due to power loss),
    # to prevent silent failure.
    if not os.path.exists(get_dir_path(_id)):
        os.makedirs(get_dir_path(_id))
    
    path = get_path(_id)
    if not exists(_id):
        with open(path, "w") as _file:
            _file.write(to_string(datetime.utcnow()))

    with open(path, "r") as _file:
        last_datetime_text = _file.read()
        if not last_datetime_text:
            raise ValueError(f"{path} has no contents.")
        
        # Will only raise an exception if the file already exists, but has an invalid datetime format (e.g. empty).
        last_datetime = datetime.strptime(last_datetime_text, TIME_FORMAT)
        return last_datetime

def set_last(new_datetime: datetime, _id: str=None) -> None:
    """Sets the last datetime we're done with for this id. Creates the respective file if it does not exist."""
    if not os.path.exists(get_dir_path(_id)):
        os.makedirs(get_dir_path(_id))
    
    with tempfile.NamedTemporaryFile("w", dir=get_dir_path(_id), delete=False) as temp_file:
        temp_file.write(to_string(new_datetime))
        temp_file.flush()
        os.fsync(temp_file.fileno())

    os.replace(temp_file.name, get_path(_id))

def exists(_id: str=None) -> bool:
    """Returns whether a datetime file for this id exists."""
    return os.path.exists(get_path(_id))

def get_path(_id: str=None) -> str:
    """Returns the path to the event time file with the given identifier."""
    global PATH_PREFIX, FILE_NAME_PREFIX, FILE_NAME_POSTFIX
    return f"{PATH_PREFIX}{FILE_NAME_PREFIX}{_id}{FILE_NAME_POSTFIX}"

def get_dir_path(_id: str=None) -> str:
    """Returns the path to the event time file with the given identifier."""
    global PATH_PREFIX
    return f"{PATH_PREFIX}"

def to_string(_datetime: datetime) -> str:
    """Returns the ISO 8601 format (except timezone and microsecond values) of the given datetime."""
    return _datetime.strftime(TIME_FORMAT)

def from_string(string: str) -> datetime:
    """Returns the datetime of the given ISO 8601 formatted string (except timezone and microsecond
    values), otherwise raises ValueError (e.g. wrong format)."""
    time = None
    with suppress(ValueError): time = datetime.strptime(string, TIME_FORMAT)
    with suppress(ValueError): time = datetime.strptime(string, TIME_FORMAT_TZ)
    with suppress(ValueError): time = datetime.strptime(string, TIME_FORMAT_TZ2)

    if not time:
        raise ValueError(f"Could not parse \"{string}\" as an ISO-8061 formatted datetime.")

    if not time.tzinfo:
        return time

    return time.replace(tzinfo=None) + time.tzinfo.utcoffset(time)

    # Any other case (e.g. time being None or not matching the format).
    raise ValueError(f"The given string, {string}, did not match the format \"{TIME_FORMAT}\".")
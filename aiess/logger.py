from datetime import datetime

from aiess import timestamp
from aiess.settings import ROOT_PATH

PATH_PREFIX = ROOT_PATH + "logs/"

time_str = None

# These are ANSI escape sequences, see http://ascii-table.com/ansi-escape-sequences.php
class colors:
    CLEAR = "\033[0m"

    LOADING_FILLED = "\033[47m"
    LOADING_EMPTY  = "\033[44m"

    EVENT   = "\033[33m"
    AUTHOR  = "\033[32m"
    CONTEXT = "\033[34m"

def fmt(string: str, esc_seq: str):
    return f"{esc_seq}{string}{colors.CLEAR}"

def init(_time_str: str=None):
    """Sets the time string for the log file (i.e. "log-{time_str}.txt")."""
    global time_str
    if _time_str: time_str = _time_str
    else:         time_str = datetime.utcnow().strftime("%Y%m%d-%H%M%S")

def log(_obj="", newline: bool=True, postfix: str="") -> None:
    """Takes the given object as a string with the current timestamp,
    prints it, and appends it to the current log file."""
    message = timestamped_str(_obj) if newline else str(_obj)
    try:
        print(message, end="")
    except OSError as error:
        # Occurs when the message includes character codes which the python terminal doesn't recognize.
        print(f"OSError: {error}\n")
    
    write(_obj, newline, postfix)

def write(_obj, newline: bool=True, postfix: str="") -> None:
    """Takes the given object as a string and appends it to the current log file,
    with a given postfix, if specified."""
    global time_str
    if not time_str:
        return  # Tests do not initalize the time string.

    message = timestamped_str(_obj) if newline else str(_obj)
    with open(f"{PATH_PREFIX}log{postfix}-{time_str}.txt", "a", encoding="utf-8") as _file:
        _file.write(message)

def timestamped_str(_obj) -> str:
    """Returns the given object as a string, prefixes it by a timestamp (unless the object evaluates to False),
    and postfixes it by a newline character."""
    if not _obj:
        return "\n"
    
    stamp = timestamp.to_string(datetime.utcnow())
    return f"{stamp} | {str(_obj)}\n"

def log_err(err: Exception) -> None:
    """Takes the given exception as a string with the current timestamp,
    and appends it to both the current log and log-err files."""
    log(err)
    write(err, postfix="-err")
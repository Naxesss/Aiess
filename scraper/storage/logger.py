

PATH_PREFIX = "../logs/"

time_str = None

def init(_time_str: str):
    """Sets the time string for the log file (i.e. "log-{time_str}.txt")."""
    global time_str
    time_str = _time_str

def log(_obj="", end: str="\n", postfix: str="") -> None:
    """Takes the given object as a string, prints it, and appends it to the current log file."""
    message = str(_obj)
    try:
        print(message, end=end)
    except OSError as error:
        # Occurs when the message includes character codes which the python terminal doesn't recognize.
        print(f"OSError: {error}")
    
    write(_obj, end, postfix)

def write(_obj, end: str="\n", postfix: str="") -> None:
    """Takes the given object as a string and appends it to the current log file,
    with a given postfix, if specified."""
    global time_str
    if not time_str:
        return  # Tests do not initalize the time string.

    message = str(_obj)
    with open(f"{PATH_PREFIX}log{postfix}-{time_str}.txt", "a", encoding="utf-8") as _file:
        _file.write(message + end)

def log_err(err: Exception) -> None:
    """Takes the given exception as a string and appends it to both the current log and log-err files."""
    log(err)
    write(err, postfix="-err")
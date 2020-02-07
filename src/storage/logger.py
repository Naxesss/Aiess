

PATH_PREFIX = "../logs/"

time_str = None

def init(_time_str):
    """Sets the time string for the log file (i.e. "log-{time_str}.txt")."""
    global time_str
    time_str = _time_str

def log(_obj="", end="\n") -> None:
    """Takes the given object as a string, prints it, and appends it to the current log file."""
    global time_str
    if not time_str:
        return  # Tests do not initalize the time string.

    message = str(_obj)
    try:
        print(message, end=end)
    except OSError as error:
        # Occurs when the message includes character codes which the python terminal doesn't recognize.
        print(f"OSError: {error}")
    
    with open(f"{PATH_PREFIX}log-{time_str}.txt", "a", encoding="utf-8") as _file:
        _file.write(message + end)
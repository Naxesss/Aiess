from datetime import datetime

# Seems all timeago tags follow this format. If it changes we should raise before it becomes an issue.
# dateutil is a potential catch-all for this, but it inevitably makes assumptions that may be unexpected.
ISO_8061_FORMAT = "%Y-%m-%dT%H:%M:%S+00:00"

def from_ISO_8601_to_datetime(time: str) -> datetime:
    """Returns the given ISO 8601 formatted string into its datetime equivalent, otherwise raises ValueError (e.g. wrong format)."""
    try:
        return datetime.strptime(time, ISO_8061_FORMAT)
    except:
        # Any other case (e.g. time being None or not matching the format).
        raise ValueError(f"The given time, {time}, did not match the format \"{ISO_8061_FORMAT}\".")
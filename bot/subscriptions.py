import sys
sys.path.append('..')

class Subscription():
    """Represents a channel subscription, containing channel identifying information as well as a filter.
    This allows for figuring out where to send data, as well as which data to send."""

    def __init__(self, guild_id: str, channel_id: str, _filter: str):
        self.guild_id = guild_id
        self.channel_id = channel_id
        self.filter = _filter
    
    def __str__(self) -> str:
        return f"Guild {self.guild_id}, Channel {self.channel_id}, Filter \"{self.filter}\""

    def __eq__(self, other) -> bool:
        if not isinstance(other, Subscription):
            return False
        return (
            self.guild_id == other.guild_id and
            self.channel_id == other.channel_id and
            self.filter == other.filter
        )
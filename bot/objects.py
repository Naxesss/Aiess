import sys
sys.path.append('..')

class Subscription():
    """Represents a channel subscription, containing channel identifying information as well as a filter.
    This allows for figuring out where to send data, as well as which data to send."""

    def __init__(self, guild_id: int, channel_id: int, _filter: str):
        self.guild_id = int(guild_id) if guild_id is not None else None
        self.channel_id = int(channel_id)
        self.filter = _filter
    
    def __str__(self) -> str:
        return f"Guild {self.guild_id}, Channel {self.channel_id}, Filter \"{self.filter}\""
    
    def __key(self) -> tuple:
        return (
            self.guild_id,
            self.channel_id,
            self.filter
        )
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Subscription):
            return False
        return self.__key() == other.__key()
    
    def __hash__(self) -> str:
        return hash(self.__key())

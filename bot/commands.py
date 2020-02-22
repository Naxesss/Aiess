from discord import Message

class Command():
    def __init__(self, name: str, *args: str, context: Message=None):
        self.name = name
        self.args = [arg for arg in args]
        self.context = context
    
    def __str__(self) -> str:
        args = [f" {arg}" for arg in self.args]
        return f"+{self.name}{args}"
    
    def __eq__(self, other) -> bool:
        if type(self) != type(other):
            return False
        return (
            self.name == other.name and
            self.args == other.args
        )
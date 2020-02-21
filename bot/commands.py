
class Command():
    def __init__(self, name: str, *args: str):
        self.name = name
        self.args = [arg for arg in args]

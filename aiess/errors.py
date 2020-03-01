class ParsingError(Exception):
    """For use in cases where parsing some portion of an event failed and should stop the program."""
    pass

class DeletedContextError(Exception):
    """For use in cases where some portion of an event is missing due to its context being deleted.
    This should not stop the program, but instead simply delete the event the error was raised from."""
    pass
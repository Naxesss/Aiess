import sys
sys.path.append('..')

from bot.commands import Command
from bot.receiver import parse_command, receive_command

def test_find_command():
    assert parse_command("+test") == Command("test")
    assert parse_command("+test 123") == Command("test", "123")
    assert parse_command("+test 1 2 3") == Command("test", "1", "2", "3")
    assert not parse_command("123")
    assert not parse_command("+ test")
    assert not parse_command("++test")
    assert not parse_command("123 +test")

def test_receive_command():
    assert receive_command(Command("ping"))
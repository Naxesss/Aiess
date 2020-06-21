import sys
sys.path.append('..')

from bot.commands import Command
from bot.commands import COMMAND_PREFIX

def test_init_command():
    command = Command("test", "1", "2", "3")
    assert command.name == "test"
    assert command.args == ["1", "2", "3"]

def test_init_command_no_args():
    command = Command("test")
    assert command.name == "test"
    assert not command.args

def test_eq_command_string():
    command = Command("test")
    assert not command == "some string"

def test_hash_command():
    command = Command("test")
    assert command.__hash__()

def test_str_command():
    command = Command("test", "1", "2", "3")
    assert str(command) == f"{COMMAND_PREFIX}test 1 2 3"

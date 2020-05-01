import sys
sys.path.append('..')

from bot.commands import Command

def test_init():
    command = Command("test", "1", "2", "3")
    
    assert command.name == "test"
    assert command.args == ["1", "2", "3"]

def test_init_no_args():
    command = Command("test")

    assert command.name == "test"
    assert not command.args
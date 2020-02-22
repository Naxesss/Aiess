import pytest

from tests.mock_command import MockCommand
from receiver import receive_command

@pytest.mark.asyncio
async def test_ping():
    mock_command = MockCommand("ping")
    await receive_command(mock_command)
    assert mock_command.response == "pong"
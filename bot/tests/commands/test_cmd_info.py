import sys
sys.path.append('..')

import pytest
import mock
from datetime import datetime

from aiess.timestamp import from_string
from aiess.database import Database, SCRAPER_TEST_DB_NAME

from bot.tests.commands.mock_command import MockCommand, MockMessage, MockChannel
from bot.cmd_modules import cmd_info
from bot.receiver import receive_command

async def mock_application_info():
    mock_app_info = mock.MagicMock()
    mock_app_info.description = "description"
    mock_app_info.owner = "owner"
    mock_app_info.id = 2
    return mock_app_info

@pytest.mark.asyncio
async def test_info():
    mock_client = mock.MagicMock()
    mock_client.guilds = [object()] * 5
    mock_client.user = mock.MagicMock()
    mock_client.user.created_at = from_string("2020-01-01 00:00:00")
    mock_client.user.name = "name"
    mock_client.user.avatar_url = "avatar url"
    mock_client.application_info = mock_application_info

    mock_command = MockCommand("info", context=MockMessage(channel=MockChannel()), client=mock_client)
    
    with mock.patch("bot.cmd_modules.cmd_info.retrieve_event_count", return_value=8000):
        with mock.patch("bot.cmd_modules.cmd_info.retrieve_event_count_today", return_value=40):
            with mock.patch("bot.cmd_modules.cmd_info.retrieve_subscription_count", return_value=6):
                with mock.patch("bot.cmd_modules.cmd_info.retrieve_first_event_at", return_value=from_string("2020-01-01 00:00:00")):
                    assert await receive_command(mock_command)

    assert f"https://discord.com/api/oauth2/authorize?client_id=2&permissions=0&scope=bot" in mock_command.response
    assert mock_command.response_embed.author.name == "name"
    assert mock_command.response_embed.author.icon_url == "avatar url"
    assert mock_command.response_embed.description == "description"

    assert mock_command.response_embed.fields[0].name == "Created"
    assert mock_command.response_embed.fields[0].value.startswith("**2020-01-01**\n(<t:")
    assert mock_command.response_embed.fields[0].value.endswith(":R>)")

    assert mock_command.response_embed.fields[1].name == "Author"
    assert mock_command.response_embed.fields[1].value == "owner"

    assert mock_command.response_embed.fields[2].name == "Source"
    assert mock_command.response_embed.fields[2].value == "https://github.com/Naxesss/Aiess"

    assert mock_command.response_embed.fields[3].name == "Events"
    assert mock_command.response_embed.fields[3].value == "**8000** in total, **40** in past 24h"

    assert mock_command.response_embed.fields[4].name == "Subscriptions"
    assert mock_command.response_embed.fields[4].value == "**6** in total across **5** servers"
    
    assert mock_command.response_embed.fields[5].name == "First event"
    assert mock_command.response_embed.fields[5].value.startswith("**2020-01-01**\n(<t:")
    assert mock_command.response_embed.fields[5].value.endswith(":R>)")

def mock_retrieve_table_data(self, table, where, selection):
    raise TimeoutError

@mock.patch("bot.cmd_modules.cmd_info.SCRAPER_DB_NAME", SCRAPER_TEST_DB_NAME)
@mock.patch.object(Database, 'retrieve_table_data', mock_retrieve_table_data)
def test_retrieve_event_count_timeout():
    assert cmd_info.retrieve_event_count() == "(timed out)"
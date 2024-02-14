import os
from dotenv import load_dotenv
import requests
import pytest

load_dotenv()
VALID_TOKEN = os.getenv("DISCORD_TOKEN")
VALID_CHANNEL_ID = "1201390755604877362"
Content = {"content": "test"}

@pytest.fixture
def valid_headers():
    return {"Authorization": VALID_TOKEN}

def test_send_discord_message_valid(valid_headers):
    url = f"https://discord.com/api/v9/channels/{VALID_CHANNEL_ID}/messages"
    payload = Content
    res = requests.post(url, json=payload, headers=valid_headers)

    assert res.status_code == 200

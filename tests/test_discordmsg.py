import os
from dotenv import load_dotenv
import requests
import pytest

load_dotenv()
discord_token = os.getenv("DISCORD_TOKEN")

VALID_CHANNEL_ID = "1201390755604877362"
VALID_TOKEN = discord_token

@pytest.fixture
def valid_headers():
    return {"Authorization": VALID_TOKEN}

def test_send_discord_message_valid(valid_headers):
    url = f"https://discord.com/api/v9/channels/{VALID_CHANNEL_ID}/messages"
    payload = {"content": "test"}
    res = requests.post(url, json=payload, headers=valid_headers)

    assert res.status_code == 200

def test_send_discord_message_invalid_token():
    url = f"https://discord.com/api/v9/channels/{VALID_CHANNEL_ID}/messages"
    payload = {"content": "test"}
    invalid_headers = {"Authorization": "invalid_token"}
    res = requests.post(url, json=payload, headers=invalid_headers)

    assert res.status_code == 401
    
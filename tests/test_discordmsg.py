import os
from dotenv import load_dotenv
import requests
import pytest
load_dotenv()
VALID_TOKEN = os.getenv("DISCORD_TOKEN")
Content = {"content": "tests"}
@pytest.fixture
def valid_headers():
    return {"Authorization": VALID_TOKEN}
def test_send_discord_message_valid(valid_headers):
    url = "http://127.0.0.1:5000/api/v1/channels/<channel_id>/messages"
    payload = Content
    res = requests.post(url, json=payload, headers=valid_headers)
    assert res.status_code == 200

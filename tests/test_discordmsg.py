import os
from dotenv import load_dotenv
from faker import Faker
import requests
import pytest

fake = Faker()

load_dotenv()
VALID_TOKEN = os.getenv("DISCORD_TOKEN")
VALID_CHANNEL_ID = "1201390755604877362"

def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", type=int, default=1, help="Number of random messages to send")


@pytest.fixture
def valid_headers():
    return {"Authorization": VALID_TOKEN}

@pytest.mark.parametrize("num_records", [2])
def test_send_discord_message_valid(valid_headers, num_records):
    url = f"https://discord.com/api/v9/channels/{VALID_CHANNEL_ID}/messages"
    for _ in range(num_records):
        payload = {"content": fake.word()}
        res = requests.post(url, json=payload, headers=valid_headers)

        assert res.status_code == 200

'''
def test_send_discord_message_variable(valid_headers, request):
    num_records = request.config.getoption("--num_records")
    url = f"https://discord.com/api/v9/channels/{VALID_CHANNEL_ID}/messages"
    for _ in range(num_records):
        payload = {"content": fake.word()}
        res = requests.post(url, json=payload, headers=valid_headers)

        assert res.status_code == 200
'''
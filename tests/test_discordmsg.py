import os
from dotenv import load_dotenv
import requests
from faker import Faker
import pytest
load_dotenv()
fake = Faker()
VALID_TOKEN = os.getenv("DISCORD_TOKEN")
def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", type=int, default=1, help="Number of random messages to send")
@pytest.fixture
def valid_headers():
    return {"Authorization": VALID_TOKEN}
@pytest.mark.parametrize("num_records", [2])
def test_send_discord_message_valid(valid_headers, num_records):
    url = "http://127.0.0.1:5000/api/v1/channels/<channel_id>/messages"
    for _ in range(num_records):
        Content = {"content": fake.word()}
        payload = Content
        res = requests.post(url, json=payload, headers=valid_headers)
        assert res.status_code == 200
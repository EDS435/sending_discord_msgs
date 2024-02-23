import os
from dotenv import load_dotenv
import requests
load_dotenv()
discord_token = os.getenv("DISCORD_TOKEN")
if discord_token is None:
    raise ValueError("Discord token not found in the .env file")
url = "http://127.0.0.1:5000/api/v1/channels/<channel_id>/messages"
payload = {
    "content" : "testing"
}
headers = {
    "Authorization" : discord_token
}
res = requests.post(url, json=payload, headers=headers)


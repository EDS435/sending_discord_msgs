import os
from dotenv import load_dotenv
import requests

load_dotenv()
discord_token = os.getenv("DISCORD_TOKEN")

if discord_token is None:
    raise ValueError("Discord token not found in the .env file")

url = "https://discord.com/api/v9/channels/1201390755604877362/messages"

payload = {
    "content" : "test"
}

headers = {
    "Authorization" : discord_token
}

res = requests.post(url, payload, headers=headers)

import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.nightbot.tv/1"
CHANNEL_ID = os.getenv("CHANNEL_ID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")

def send_winner_message(winner_name):
    """Send the winner announcement to the YouTube chat."""
    headers = {
        "Authorization": f"Session {AUTH_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "channel": CHANNEL_ID,
        "message": f"Congratulations, {winner_name}! You won the giveaway!"
    }
    response = requests.post(f"{BASE_URL}/channel/send", headers=headers, json=payload)
    if response.status_code == 200:
        print("Message Sent Successfully:", response.json())
    else:
        print("Failed to Send Message:", response.status_code, response.text)

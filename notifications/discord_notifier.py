import os
from dotenv import load_dotenv
import requests


class DiscordNotifier:

    def __init__(self, webhook_url):
        self.webhook_url = webhook_url

    def send(self, message):

        payload = {
            "content": message
        }

        response = requests.post(
            self.webhook_url,
            json=payload
        )

        response.raise_for_status()
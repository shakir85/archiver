"""
Sends notification to a discord channel using webhooks
Discord API docs: https://pypi.org/project/discord-webhook/
"""
import os
import logging
import requests
from http.client import HTTPException
from discord_webhook import DiscordWebhook, DiscordEmbed

"""
colors:
    teal -> 0x1abc9c
    green -> 0x2ecc71
    red -> 0xe74c3c
"""

LOG_DIR = f"{os.getenv('HOME')}/syncdir"
WEBHOOK = os.getenv('WEBHOOK')


def set_logging() -> None:
    if not os.path.exists(LOG_DIR):
        os.mkdir(path=LOG_DIR, mode=0o0777)

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
                        filename=f"{LOG_DIR}/syncdir.log", filemode="a")


def notify(job_name: str, status: str) -> None:
    embed = ""
    color = ""

    if status == "success":
        color = "0xe74c3c"
    if status == "failure":
        color = "0xe74c3c"

    try:
        webhook = DiscordWebhook(url=WEBHOOK)
        embed = DiscordEmbed(title=status, description=f'{job_name} - archive', color=color)

        embed.set_timestamp()
        webhook.add_embed(embed)

        response = webhook.execute()
        logging.info("Notification sent to Discord")

        status_code = response.status_code

        if status_code != 200:
            logging.error(f"Message sending failed - status code: {status_code}")
            raise requests.exceptions.RequestException

    except HTTPException as e:
        logging.error(f"HTTP Exception - check Discord webhook URL\n{e}\n")


notify(job_name="foo", status="success")

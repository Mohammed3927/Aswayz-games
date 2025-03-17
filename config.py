import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
PREFIX = os.getenv("PREFIX", "!")
GAME_CHANNELS = list(map(int, os.getenv("GAME_CHANNELS", "").split(",")))

REQUIRED_PERMISSIONS = ["administrator", "manage_events"]

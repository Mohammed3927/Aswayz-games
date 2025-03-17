import os
from dotenv import load_dotenv

# تحميل المتغيرات من .env
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
PREFIX = os.getenv("PREFIX", "!")
GAME_CHANNELS = list(map(int, os.getenv("GAME_CHANNELS", "").split(",")))

# الصلاحيات المطلوبة لتشغيل الألعاب
REQUIRED_PERMISSIONS = ["administrator", "manage_events"]

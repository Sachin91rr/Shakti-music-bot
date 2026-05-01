import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv(""))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID"))
BOT_USERNAME = os.getenv("BOT_USERNAME")
MONGO_DB_URI = os.getenv("MONGO_DB_URI")

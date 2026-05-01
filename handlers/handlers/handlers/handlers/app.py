from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from handlers import load_handlers

app = Client(
    "ShaktiMusicBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

load_handlers(app)

app.run()

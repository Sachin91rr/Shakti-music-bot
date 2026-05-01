from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from handlers import load_handlers
from core.vc import start_vc
import asyncio

app = Client(
    "ShaktiMusicBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

load_handlers(app)

async def main():
    await app.start()
    await start_vc()
    print("✅ Shakti Cineplex Music 🌈 Started")
    await idle()

from pyrogram.idle import idle
asyncio.get_event_loop().run_until_complete(main())

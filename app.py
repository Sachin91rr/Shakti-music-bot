from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

app = Client(
    "ShaktiMusicBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message()
async def start_handler(client, message):
    if message.text == "/start":
        await message.reply_text(
            "🎵 Welcome to Shakti Cineplex Music 🌈\n\nUse /play <song name>"
        )

app.run()

from pyrogram import filters
from core.player import add_to_queue

def register(app):
    @app.on_message(filters.command("play"))
    async def play_cmd(client, message):
        if len(message.command) < 2:
            return await message.reply_text("❌ Usage: /play song name")

        query = " ".join(message.command[1:])
        msg = await message.reply_text("🔎 Searching...")

        song = await add_to_queue(query)

        if not song:
            return await msg.edit_text("❌ Song not found")

        await msg.edit_text(
            f"✅ Added to queue\n\n🎵 **{song['title']}**"
        )

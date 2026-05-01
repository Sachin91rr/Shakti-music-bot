from pyrogram import filters
from core.player import show_queue

def register(app):
    @app.on_message(filters.command("queue"))
    async def queue_cmd(client, message):
        queue = show_queue()

        if not queue:
            return await message.reply_text("📭 Queue empty")

        text = "📃 **Playlist Queue**\n\n"
        for i, song in enumerate(queue, start=1):
            text += f"{i}. {song['title']}\n"

        await message.reply_text(text)

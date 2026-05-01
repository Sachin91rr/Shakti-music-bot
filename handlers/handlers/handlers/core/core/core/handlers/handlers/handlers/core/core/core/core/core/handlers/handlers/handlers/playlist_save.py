from pyrogram import filters
from core.player import show_queue
from core.playlist_db import save_playlist, load_playlist

def register(app):
    @app.on_message(filters.command("saveplaylist"))
    async def save_cmd(client, message):
        queue = show_queue()
        await save_playlist(message.from_user.id, queue)
        await message.reply_text("✅ Playlist saved")

    @app.on_message(filters.command("loadplaylist"))
    async def load_cmd(client, message):
        songs = await load_playlist(message.from_user.id)
        if not songs:
            return await message.reply_text("📭 No saved playlist")
        await message.reply_text(f"✅ Loaded {len(songs)} songs")

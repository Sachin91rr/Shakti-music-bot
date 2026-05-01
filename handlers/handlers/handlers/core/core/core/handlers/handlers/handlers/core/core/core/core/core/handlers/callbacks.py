from pyrogram import filters
from pyrogram.types import CallbackQuery

def register(app):
    @app.on_callback_query()
    async def callback_handler(client, query: CallbackQuery):
        data = query.data

        if data == "help_play":
            await query.message.edit_text(
                "🎵 **Play Help**\n\nUse `/play song name`"
            )

        elif data == "help_playlist":
            await query.message.edit_text(
                "📃 **Playlist Help**\n\nUse `/queue` to view queue"
            )

        elif data == "help_admin":
            await query.message.edit_text(
                "👮 **Admin Commands**\n\n"
                "/skip\n/stop\n/pause\n/resume"
            )

        elif data == "close":
            await query.message.delete()

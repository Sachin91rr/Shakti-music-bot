from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def register(app):
    @app.on_message(filters.command("start"))
    async def start_cmd(client, message):
        buttons = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🎵 Play", callback_data="help_play"),
                    InlineKeyboardButton("📃 Playlist", callback_data="help_playlist"),
                ],
                [
                    InlineKeyboardButton("👮 Admin", callback_data="help_admin"),
                    InlineKeyboardButton("❌ Close", callback_data="close"),
                ],
            ]
        )

        await message.reply_text(
            "✨ **Welcome to Shakti Cineplex Music 🌈**\n\n"
            "Premium VC Music Bot\n"
            "Use `/play song name` to start music 🎧",
            reply_markup=buttons
                    )

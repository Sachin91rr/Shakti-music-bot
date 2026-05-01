from pyrogram import filters

def register(app):
    @app.on_message(filters.command("play"))
    async def play_cmd(client, message):
        if len(message.command) < 2:
            return await message.reply_text("❌ Usage: /play song name")

        query = " ".join(message.command[1:])
        await message.reply_text(f"🔎 Searching: **{query}** ...")

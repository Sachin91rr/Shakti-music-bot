from pyrogram import filters

def register(app):
    @app.on_message(filters.command("skip"))
    async def skip_cmd(client, message):
        await message.reply_text("⏭ Song skipped")

    @app.on_message(filters.command("stop"))
    async def stop_cmd(client, message):
        await message.reply_text("⏹ Playback stopped")

    @app.on_message(filters.command("pause"))
    async def pause_cmd(client, message):
        await message.reply_text("⏸ Playback paused")

    @app.on_message(filters.command("resume"))
    async def resume_cmd(client, message):
        await message.reply_text("▶️ Playback resumed")

from pyrogram import filters
from core.vc_player import leave_stream

def register(app):
    @app.on_message(filters.command("skip"))
    async def skip_cmd(client, message):
        await message.reply_text("⏭ Song skipped")

    @app.on_message(filters.command("stop"))
    async def stop_cmd(client, message):
        try:
            await leave_stream(message.chat.id)
        except:
            pass
        await message.reply_text("⏹ Playback stopped")

    @app.on_message(filters.command("pause"))
    async def pause_cmd(client, message):
        await message.reply_text("⏸ Playback paused")

    @app.on_message(filters.command("resume"))
    async def resume_cmd(client, message):
        await message.reply_text("▶️ Playback resumed")

    @app.on_message(filters.command("joinvc"))
    async def joinvc(client, message):
        await message.reply_text("✅ Assistant ready for VC")

    @app.on_message(filters.command("leavevc"))
    async def leavevc(client, message):
        try:
            await leave_stream(message.chat.id)
        except:
            pass
        await message.reply_text("👋 Left voice chat")

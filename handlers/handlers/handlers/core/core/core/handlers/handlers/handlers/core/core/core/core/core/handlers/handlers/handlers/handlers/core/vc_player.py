from pytgcalls.types.input_stream import AudioPiped
from core.vc import vc

async def play_stream(chat_id: int, stream_url: str):
    await vc.join_group_call(
        chat_id,
        AudioPiped(stream_url)
    )

async def leave_stream(chat_id: int):
    await vc.leave_group_call(chat_id)

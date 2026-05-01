from pytgcalls import PyTgCalls
from core.assistant import assistant

vc = PyTgCalls(assistant)

async def start_vc():
    await assistant.start()
    await vc.start()

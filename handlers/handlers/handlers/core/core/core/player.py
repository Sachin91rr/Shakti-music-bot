from core.queue import add_song, list_queue
from core.youtube import search_song

async def add_to_queue(query: str):
    song = await search_song(query)
    if not song:
        return None

    add_song(song)
    return song

def show_queue():
    return list_queue()

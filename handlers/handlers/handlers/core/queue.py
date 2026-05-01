from collections import deque

music_queue = deque()

def add_song(song: dict):
    music_queue.append(song)

def get_next_song():
    if music_queue:
        return music_queue.popleft()
    return None

def clear_queue():
    music_queue.clear()

def list_queue():
    return list(music_queue)

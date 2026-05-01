from database import playlists

async def save_playlist(user_id: int, songs: list):
    await playlists.update_one(
        {"user_id": user_id},
        {"$set": {"songs": songs}},
        upsert=True
    )

async def load_playlist(user_id: int):
    data = await playlists.find_one({"user_id": user_id})
    if data:
        return data.get("songs", [])
    return []

import yt_dlp
import asyncio

YDL_OPTS = {
    "format": "bestaudio",
    "quiet": True,
    "noplaylist": True,
}

async def search_song(query: str):
    loop = asyncio.get_event_loop()

    def _extract():
        with yt_dlp.YoutubeDL(YDL_OPTS) as ydl:
            info = ydl.extract_info(f"ytsearch:{query}", download=False)
            if "entries" in info and info["entries"]:
                data = info["entries"][0]
                return {
                    "title": data["title"],
                    "url": data["url"],
                    "webpage_url": data["webpage_url"],
                }
        return None

    return await loop.run_in_executor(None, _extract)

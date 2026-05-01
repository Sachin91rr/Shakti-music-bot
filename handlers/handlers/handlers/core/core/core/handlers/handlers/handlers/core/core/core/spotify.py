import re

def parse_spotify(query: str):
    if "spotify.com" in query:
        return {
            "type": "spotify",
            "query": query
        }
    return None

def parse_jiosaavn(query: str):
    if "jiosaavn.com" in query or "saavn" in query:
        return {
            "type": "jiosaavn",
            "query": query
        }
    return None

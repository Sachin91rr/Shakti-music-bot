from pyrogram import Client
import os

assistant = Client(
    "assistant_account",
    api_id=int(os.getenv("API_ID")),
    api_hash=os.getenv("API_HASH"),
    session_string=os.getenv("STRING_SESSION"),
)

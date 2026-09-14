from pyrogram import Client
from pyrogram.storage import MemoryStorage

API_ID = int(input("API_ID: "))
API_HASH = input("API_HASH: ")

with Client(
    "my_account",
    api_id=API_ID,
    api_hash=API_HASH
) as app:
    print("\nSESSION STRING:\n")
    print(app.export_session_string())
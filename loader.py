from pyrogram import Client
import os
from config import api_id, api_hash
app = Client(
    "my_bot",
    api_id=api_id,
    api_hash=api_hash
)

os.system('cls')
print('Ok im working')
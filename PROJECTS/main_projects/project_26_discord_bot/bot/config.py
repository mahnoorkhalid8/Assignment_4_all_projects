import os
from dotenv import load_dotenv

load_dotenv()  # Loads from .env file

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

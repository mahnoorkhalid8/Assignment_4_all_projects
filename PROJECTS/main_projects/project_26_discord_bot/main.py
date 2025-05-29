from dotenv import load_dotenv
import os

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

import streamlit as st
import asyncio
import threading
from bot.bot_logic import setup_bot
from bot.config import DISCORD_TOKEN 


bot = setup_bot()

def run_bot():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(bot.start(DISCORD_TOKEN))
    except Exception as e:
        print(f"Error running bot: {e}")

# Streamlit UI
st.title("🤖 Discord Bot Control Panel")
st.markdown("Control your custom Discord bot from this panel!")

if st.button("Start Bot"):
    st.write("Starting bot... Please wait.")
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.start()
    st.success("✅ Bot is now running in the background!")

# Optional command tester
command = st.text_input("Type 'hello' to test command (not sent to Discord)")
if command == "hello":
    st.info("This would trigger the !hello command on Discord.")
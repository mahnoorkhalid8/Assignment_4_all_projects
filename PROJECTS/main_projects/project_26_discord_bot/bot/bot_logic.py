import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True
intents.presences = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    # Reply to every message
    await message.channel.send(f"👋 You said: {message.content}")

    await bot.process_commands(message)
    
@bot.command()
async def hello(ctx):
    await ctx.send("👋 Hello! I am your friendly bot!")
    
@bot.command()
async def bot_status(ctx):
    await ctx.send(f"🤖 Bot is online and running as {bot.user}!")
    
def setup_bot():
    return bot

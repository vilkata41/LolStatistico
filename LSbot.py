import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
client = discord.Client()

@client.event
async def on_message(msg):
    if msg.content == "hey":
        await msg.channel.send("sup")

client.run(TOKEN)

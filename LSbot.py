import os
import discord
from dotenv import load_dotenv
import apiTesting

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
client = discord.Client()


@client.event
async def on_message(msg):
    cmd = parse(msg.content)
    if cmd != "":
        if cmd == "help":
            await msg.channel.send("I am currently a work in progress. "
                                   "I will soon give you a whole load of information...")
        elif cmd == "test":
            await msg.channel.send(apiTesting.test())
        else:
            await msg.channel.send("Sorry, my parents didn't teach me how to answer to this. "
                                   "Try again.")


def parse(inpt):
    if not inpt.startswith("ls "):
        return ""

    result = inpt.replace("ls ", "", 1)
    return result


client.run(TOKEN)

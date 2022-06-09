import os
import discord
from dotenv import load_dotenv
import apiTesting

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
client = discord.Client()
curr_region = "EUNE"


@client.event
async def on_message(msg):
    cmd = parse(msg.content)
    if cmd is not [] and len(cmd) > 0:
        if cmd[0] == "help":
            if len(cmd) > 1:
                message = "Only one argument expected. Please just write 'ls help' to get help."
            else:
                message = "I am currently a work in progress." \
                          "I will soon give you a whole load of information... " \
                          "Right now you can check the following commands: \n\n" \
                          "-ls tips_with (championName) - where (championName) should be replaced" \
                          "with the champion name you want to check tips for gameplay of.\n\n" \
                          #"-ls tips_against (championName) - where (championName) should be replaced" \
                          #"with the champion you are playing against."
            await msg.channel.send(message)
        elif cmd[0] == "tips_with":
            if len(cmd) != 2:
                message = "Wrong number of arguments. Check 'ls help' to see the commands."
            else:
                message = apiTesting.tips_with_champ(cmd[1], curr_region)
            await msg.channel.send(message)
        else:
            await msg.channel.send("Sorry, my parents didn't teach me how to answer to this. "
                                   "Try again.")


def parse(inpt):
    if not inpt.startswith("ls "):
        return []

    result_string = inpt.replace("ls ", "", 1)
    result_list = result_string.split(" ")
    return result_list


client.run(TOKEN)

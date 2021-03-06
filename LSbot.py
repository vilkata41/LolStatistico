import os
import cassiopeia as cass
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
                          f"\n\nCurrent region: {curr_region}. \n" \
                          "If you want to select another region, type the command " \
                          "'ls change_region (regionName)' where (regionName) is one of the " \
                          "following: BR, EUNE, EUW, JP, KR, LAN, LAS, NA, OCE, RU, TR." \
                          "Right now you can check the following commands: \n\n" \
                          "-ls tips_with '(championName)' - where (championName) should be replaced" \
                          "with the champion name you want to check tips for gameplay of. Also, please" \
                          "don't miss the single quotes. \n\n" \
                          "-ls tips_against '(championName)' - where (championName) should be replaced" \
                          "with the champion you are playing against. Also, please don't miss the single quotes.\n\n" \
                          "-ls match_tips '(summonerName)' - where (summonerName) should be replaced" \
                          "with the summoner name you want to check the live game of. Also, please don't miss" \
                          "the single quotes. \n\n"
            await msg.channel.send(message)
        elif cmd[0] == "change_region":
            if len(cmd) != 2:
                message = "Wrong number of arguments. Check 'ls help' to see the commands."
            else:
                change_reg(cmd[1])
                message = f"Region changed to {curr_region}"
            await msg.channel.send(message)
        elif cmd[0] == "tips_with":
            if len(cmd) != 2:
                message = "Wrong number of arguments. Check 'ls help' to see the commands."
            else:
                message = apiTesting.tips_with_champ(cmd[1], curr_region)
            await msg.channel.send(message)
        elif cmd[0] == "tips_against":
            if len(cmd) != 2:
                message = "Wrong number of arguments. Check 'ls help' to see the commands."
            else:
                message = apiTesting.tips_against_champ(cmd[1], curr_region)
            await msg.channel.send(message)
        elif cmd[0] == "match_tips":
            await msg.channel.send("Let me datamine. Give me one moment...")
            if len(cmd) != 2:
                message = "Wrong number of arguments. Check 'ls help' to see the commands."
            else:
                message = apiTesting.get_match_tips(cmd[1], curr_region)
            await msg.channel.send(message)
        else:
            await msg.channel.send("Sorry, my parents didn't teach me how to answer to this. "
                                   "Try again after consulting 'ls help'.")


def parse(inpt):
    if not inpt.startswith("ls "):
        return []

    result_string = inpt.replace("ls ", "", 1)
    split_list = result_string.split(" ")
    result_list = []
    sp_counter = 0

    while sp_counter < len(split_list):
        if split_list[sp_counter].startswith("'"):
            item = ""
            while not split_list[sp_counter].endswith("'"):
                item += split_list[sp_counter] + " "
                sp_counter += 1
            item += split_list[sp_counter]
            sp_counter += 1
            result_list.append(item.strip("'"))
        else:
            result_list.append(split_list[sp_counter])
            sp_counter += 1

    return result_list


def change_reg(new_region):
    global curr_region
    curr_region = new_region


client.run(TOKEN)

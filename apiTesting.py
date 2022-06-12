import cassiopeia as cass
import cassiopeia_championgg as cgg
import os
import merakicommons
from dotenv import load_dotenv

load_dotenv()
RIOT_API_KEY = os.getenv("RIOT_API_TOKEN")
client = cass.set_riot_api_key(RIOT_API_KEY)


def tips_with_champ(champ_name, region):
    try:
        champ_tips = cass.get_champion(champ_name, region).ally_tips
        result = ""
        for tip in champ_tips:
            result += tip
            result += "\n"
        return result
    except merakicommons.container.SearchError:
        return "Please, enter a valid champion name in League of Legends."


def tips_against_champ(champ_name, region):
    try:
        champ_tips = cass.get_champion(champ_name, region).enemy_tips
        result = ""
        for tip in champ_tips:
            result += tip
            result += "\n"
        return result
    except merakicommons.container.SearchError:
        return "Please, enter a valid champion name in League of Legends."


def get_match_tips(summoner_name, curr_region):
    allowed_queues = ["NORMAL_5x5_DRAFT", "RANKED_FLEX_SR", "RANKED_FLEX_TT", "RANKED_SOLO_5x5"]
    curr_match = cass.Summoner(name=summoner_name, region=curr_region).current_match
    if curr_match.queue.value not in allowed_queues:
        return "This queue type is not supported. By LolStatistico. The allowed queues are: " \
               "Normal Draft, Flex, Solo Queue."

    result = ""
    curr_participant = curr_match.participants[summoner_name]
    curr_champion = curr_participant.champion.name
    result += f"Tips to play as {curr_champion}: \n" + tips_with_champ(curr_champion, curr_region)

    curr_side = curr_participant.side.value
    enemy_team = curr_match.blue_team if curr_side == 200 else curr_match.red_team

    for p in enemy_team.participants:
        enemy_champ = p.champion.name
        result += "\n"
        result += f"Tips for playing against {enemy_champ}:\n"
        result += tips_against_champ(enemy_champ, curr_region)

    return result

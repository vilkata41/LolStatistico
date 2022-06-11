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


def get_matchup_info(summoner_name, curr_region):
    allowed_queues = ["NORMAL_5x5_DRAFT", "RANKED_FLEX_SR", "RANKED_FLEX_TT", "RANKED_SOLO_5x5"]
    curr_summoner = cass.Summoner(name=summoner_name, region=curr_region)
    curr_match = curr_summoner.current_match
    curr_champion = curr_match.participants[summoner_name].champion.name

    if curr_match.queue not in allowed_queues:
        return "This queue type is not supported. By LolStatistico. The allowed queues are: " \
               "Normal Draft, Flex, Solo Queue."

    return ""

import cassiopeia as cass
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

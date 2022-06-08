import cassiopeia as cass
import os
from dotenv import load_dotenv

load_dotenv()
RIOT_API_KEY = os.getenv("RIOT_API_TOKEN")
client = cass.set_riot_api_key(RIOT_API_KEY)


def test():
    vphery = cass.Summoner(name="VPhery", region="EUNE")
    return vphery.level

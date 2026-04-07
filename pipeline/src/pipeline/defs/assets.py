import dagster as dg
from dotenv import load_dotenv
import os

load_dotenv()

METRO_API = os.getenv('METRO_API_KEY')

@dg.asset()
def vehicles_dataset() -> str:
    return f"https://api.ridemetro.org/data/Vehicles?subscription-key={METRO_API}"


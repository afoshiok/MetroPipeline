import dagster as dg
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

METRO_API = os.getenv('METRO_API_KEY')

@dg.asset()
def vehicles_dataset() -> str:
    vehicles_url = f"https://api.ridemetro.org/data/Vehicles?subscription-key={METRO_API}"
    vehicles_df = pd.read_json(vehicles_url)
    return f"Total vehicles: {len(vehicles_df)}"

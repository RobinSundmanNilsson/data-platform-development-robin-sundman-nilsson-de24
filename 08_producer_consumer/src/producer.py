from pathlib import Path
import json
from pprint import pprint

data_path = Path(__file__).parents[1] / "data"

with open(data_path / "jokes.json", "r") as file:
    jokes = json.load(file)
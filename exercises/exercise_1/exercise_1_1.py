# 0. Working with national test data

# a) Start with reading in the file riket2023_åk9_np.xlsx and the sheets for the different subjects.

import pandas as pd
from pathlib import Path

# print(Path(__file__).parent / "data")
# print(data_path / "riket2023_åk9_np.xlsx")

data_path = Path(__file__).parent / "data"

df = pd.read_excel(data_path / "riket2023_åk9_np.xlsx")

print(df.head())


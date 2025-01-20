import pandas as pd
import sys

print(sys.version)

data = {
    "Förnamn" : ["Robin"],
    "Efternamn" : ["Sundman Nilsson"],
    "Ålder" : [28],
    "Stad" : ["Stockholm"],
    "Land" : ["Sverige"]
}

df = pd.DataFrame(data)
print(df)
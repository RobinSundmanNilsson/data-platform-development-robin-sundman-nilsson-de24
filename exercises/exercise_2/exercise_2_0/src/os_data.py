import pandas as pd
import matplotlib.pyplot as plt

# läser in CSV fil som dataframe
df = pd.read_csv("athlete_events.csv")

# skriv ut de första 5 raderna i CSV filen
print(df.head())
print("-"*50)

# skriv ut sammanfattning av datan
print("\nData Summary:")
print(df.describe())
print("-"*50)

# skriv ut antal unika värden per kolumn
print("\nUnique values per column:")
print(df.nunique())
print("-"*50)

#####

# visualisera medaljer per år:

# filtrera bort rader utan medalj
df_with_medals = df[df["Medal"].notna()]

# gruppera per år och medaljtyp
medals_by_year = df_with_medals.groupby(["Year", "Medal"]).size().unstack(fill_value=0)

# plotta stapeldiagram
medals_by_year.plot(kind="bar", stacked=True, figsize=(10, 6))

# lägg till etiketter och titel
plt.title("Medals by Year")
plt.xlabel("Year")
plt.ylabel("Number of Medals")

# spara grafen till png
plt.savefig('/app/src/medals_per_year.png')

# bekräftelse på sparad graf
print("Graph saved as 'medals_by_year.png'")
print("-"*50)
import pandas as pd
import sqlite3

# Extract
df = pd.read_csv ('game-of-thones-deaths.csv')

# Transform
df['Release date']= pd.to_datetime(df['Release date'])
df.drop('Location', axis=1, inplace=True)

# Load
df.to_csv("./Deaths in game of thrones.csv", index=False)

connection = sqlite3.connect("./db")

df.to_sql("Deaths in game of thrones", connection, if_exists="replace")
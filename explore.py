import pandas as pd

df = pd.read_csv("match.csv")
print(df.groupby("striker")["runs_off_bat"].sum())
print(df.groupby("bowler")["extras"].sum())
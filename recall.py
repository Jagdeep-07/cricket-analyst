import pandas as pd
df = pd.read_csv("match.csv")

totals = df.groupby("striker")["runs_off_bat"].sum()
print(totals)
print(df.groupby("bowler")["extras"].sum())
print(totals.sort_values(ascending=False).head(1))
top_name = totals.idxmax()
top_runs = totals.max()
print("Top scorer:", top_name, top_runs)


def top_scorer(df):
    scores = df.groupby("striker")["runs_off_bat"].sum()
    name = scores.idxmax()
    runs = int(scores.max())
    return name, runs

print(top_scorer(df))
import pandas as pd

def top_scorer(df):
    totals = df.groupby("striker")["runs_off_bat"].sum()
    top_name = totals.idxmax()
    top_runs = int(totals.max())
    return top_name, top_runs

df = pd.read_csv("match.csv")
print(top_scorer(df))
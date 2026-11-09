import pandas as pd

df = pd.read_csv("match.csv")

def top_scorer(df):
    scores = df.groupby("striker")["runs_off_bat"].sum()
    name = scores.idxmax()
    runs = int(scores.max())
    return name,runs


print(top_scorer(df))    

def team_total(df):
    total = df["runs_off_bat"].sum() + df["extras"].sum()
    return int(total)

print (team_total(df))

def match_facts(df):
    name, runs = top_scorer(df)
    total = team_total(df)
    return{
        'top_scorer': name,
        'top_runs': runs,
        'team_total': total,
    }

print(match_facts(df))
def runs_from_lines(lines):
    scoreboard = {}
    cols = lines[0].split(",")
    for line in lines[1:]:
        parts = line.split(",")
        batter = parts[cols.index("striker")]
        runs = int(parts[cols.index("runs_off_bat")])

        if batter in scoreboard:
            scoreboard[batter] += runs
        else:
            scoreboard[batter] = runs
    return scoreboard

def team_total(lines):
    total_runs = 0
    cols = lines[0].split(",")
    for line in lines[1:]:
        parts = line.split(",")
        runs_off_bat = int(parts[cols.index("runs_off_bat")])
        extras = int(parts[cols.index("extras")])
        total_runs += runs_off_bat + extras
    return total_runs

if __name__ == "__main__":
    with open("match.csv") as f:
        lines = f.read().splitlines()
    print(runs_from_lines(lines))
    print(team_total(lines))

if __name__ == "__main__":
    df = pd.read_csv("match.csv")
    print(top_scorer(df))
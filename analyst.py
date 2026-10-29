def runs_from_lines(lines):
    scoreboard = {}
    for line in lines[1:]:
        parts = line.split(",")
        batter = parts[3]
        runs = int(parts[6])
        
        if batter in scoreboard:
            scoreboard[batter] += runs
        else:
            scoreboard[batter] = runs
    return scoreboard

def team_total(lines):
    total_runs = 0
    for line in lines[1:]:
        parts = line.split(",")
        runs_off_bat = int(parts[6])
        extras = int(parts[7])
        total_runs += runs_off_bat + extras
    return total_runs

        


with open("match.csv") as f:
    lines = f.read().splitlines()

print(runs_from_lines(lines)) 
print(team_total(lines))
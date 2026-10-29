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

with open("match.csv") as f:
    lines = f.read().splitlines()

print(runs_from_lines(lines)) 

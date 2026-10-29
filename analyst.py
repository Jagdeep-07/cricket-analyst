def runs_from_lines(lines):
    scoreboard = {}
    for line in lines[1:]:
        parts = line.split(",")
        batter = parts[0]
        runs = int(parts[1])
        
        if batter in scoreboard:
            scoreboard[batter] += runs
        else:
            scoreboard[batter] = runs
    return scoreboard

with open("shots.csv") as f:
    lines = f.read().splitlines()

print(runs_from_lines(lines)) 

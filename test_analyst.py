from analyst import runs_from_lines,team_total

lines = [
    "striker,runs_off_bat",
    "Rohit,4",
    "Gill,1",
    "Rohit,2",
]
total_lines = ["runs_off_bat,extras", "4,0", "1,1", "6,2"]

assert runs_from_lines(lines) == {'Rohit': 6, 'Gill': 1}
assert team_total(total_lines) == 14
print("test passed")
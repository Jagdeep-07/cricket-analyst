from analyst import runs_from_lines

lines = [
    "striker,runs_off_bat",
    "Rohit,4",
    "Gill,1",
    "Rohit,2",
]

assert runs_from_lines(lines) == {'Rohit': 6, 'Gill': 1}
print("test passed")
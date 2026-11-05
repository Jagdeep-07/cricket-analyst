# Cricket Analyst

This project reads a cricket match CSV file and gives the team total and the runs scored by each batter.
## Functions

### team_total(lines)
- IN: match lines (rows from the CSV)
- OUT: one number (team total)
- TRICK: start at 0, += bat runs + extras every ball

### runs_from_lines(lines)
- IN: match lines (rows from the CSV)
- OUT: dict of each batter's total runs
- TRICK: start at {}, old batter → += runs, new batter → = runs

## How to run

```
python analyst.py
python test_analyst.py
```
DAY=25_day
python3 $DAY/1_solution.py
fswatch -o $DAY/1_solution.py | xargs -n1 time python3 $DAY/1_solution.py

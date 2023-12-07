DAY=25
python3 $DAY.py
fswatch -o $DAY.py | xargs -n1 time python3 $DAY.py

DAY=`date '+%d'`

python3 $DAY.py
fswatch -o $DAY.py | xargs -n1 -I{} python3 $DAY.py


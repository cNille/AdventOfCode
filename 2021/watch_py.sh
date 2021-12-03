DAY=`date '+%d'`

fswatch -o $DAY.py | xargs -n1 -I{} python $DAY.py


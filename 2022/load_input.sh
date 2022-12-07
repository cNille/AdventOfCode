YEAR=`date '+%Y'`
day=`date '+%d'`

# Get cookie from adventofcode.com
COOKIE=""


sleep 2

curl\
  --silent\
  -H "Cookie: $COOKIE"\
  -o /Users/nille/aoc/$YEAR/$day.input\
  https://adventofcode.com/$YEAR/day/${day#0}/input 

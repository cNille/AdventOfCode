YEAR=`date '+%Y'`
day=`date '+%d'`

# Get cookie from adventofcode.com
COOKIE=""

sleep 5

curl\
  --silent\
  -H "Cookie: $COOKIE"\
  -o $day.input\
  https://adventofcode.com/$YEAR/day/${day#0}/input 

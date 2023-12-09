AOC_DIR=/Users/nille/aoc
YEAR=`date '+%Y'`
day=`date '+%d'`

# Source the .env file in the aoc directory
source $AOC_DIR/.env

sleep 5

curl\
  --silent\
  -H "Cookie: session=$COOKIE"\
  -o $AOC_DIR/$YEAR/$day.input\
  https://adventofcode.com/$YEAR/day/${day#0}/input 

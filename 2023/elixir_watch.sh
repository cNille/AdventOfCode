DAY=06

elixir $DAY.ex
fswatch -o $DAY.ex | xargs -n1 time elixir $DAY.ex


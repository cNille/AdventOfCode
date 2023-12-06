defmodule AdventOfCode do
  def main_timed do
    {time, _} = :timer.tc(AdventOfCode, :main, [])
    milliseconds = time / 1000
    IO.puts("Time: #{milliseconds} milliseconds")
  end

  def main do
    IO.puts("Day 6")
    file_path = "06.input"
    lines = read_input(file_path)

    IO.puts("Part 1 solution: #{solve_part1(lines)}")
    IO.puts("Part 2 solution: #{solve_part2(lines)}")
  end

  def read_input(path) do
    File.read!(path)
    |> String.split("\n")
    |> Enum.map(&String.trim/1)
    |> Enum.filter(&(&1 != ""))
  end

  def parse_line(line) do
    line
    |> String.split()
    |> Enum.drop(1)
    |> Enum.map(&String.to_integer/1)
  end

  def solve_part1(lines) do
    parsed =
      lines |> Enum.map(&parse_line/1)

    times = parsed |> Enum.at(0)
    distances = parsed |> Enum.at(1)
    calculate_all_races(times, distances)
  end

  def solve_part2(lines) do
    parsed =
      lines |> Enum.map(&parse_line/1)

    times = parsed |> Enum.at(0)
    distances = parsed |> Enum.at(1)

    times = [stringify(times)]
    distances = [stringify(distances)]

    calculate_all_races(times, distances)
  end

  def stringify(list) do
    Enum.map(list, fn x -> "#{x}" end)
    |> Enum.join("")
    |> String.to_integer()
  end

  def calculate_all_races(times, distances) do
    Enum.zip(times, distances)
    |> Enum.map(fn {time, distance} -> Task.async(fn -> win_race(time, distance) end) end)
    |> Enum.map(&Task.await/1)
    |> Enum.product()
  end

  def win_race(time, distance) do
    Enum.reduce(1..time, 0, fn i, count_ways_to_win ->
      speed = i
      time_left = time - i
      d = time_left * speed
      if d > distance, do: count_ways_to_win + 1, else: count_ways_to_win
    end)
  end
end

AdventOfCode.main_timed()

ExUnit.start()

defmodule AdventOfCodeTest do
  use ExUnit.Case, async: true

  test "win_race with test input1" do
    assert AdventOfCode.win_race(7, 9) == 4
  end

  test "win_race with test input2" do
    assert AdventOfCode.win_race(15, 40) == 8
  end

  test "win_race with test input3" do
    assert AdventOfCode.win_race(30, 200) == 9
  end
end

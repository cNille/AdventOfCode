defmodule AdventOfCode do
  def main do
    IO.puts("\e[2J\e[H")
    IO.puts("Day 09")
    lines = read_input("09.test")
    lines |> Enum.each(&IO.inspect/1)

    solution = solve1(lines)
    prev = Map.get(solution, :prev)
    next = Map.get(solution, :next)
    IO.puts("Part 1: #{next}")
    IO.puts("Part 2: #{prev}")
  end

  def read_input(filename) do
    File.read!(filename)
    |> String.split("\n")
    |> Enum.filter(&(&1 != ""))
  end

  def solve1(lines) do
    init = %{prev: 0, next: 0}

    lines
    |> Enum.map(&parse_line/1)
    |> Enum.map(&extrapolate/1)
    |> Enum.reduce(init, fn curr, acc ->
      %{
        prev: curr[:prev] + acc[:prev],
        next: curr[:next] + acc[:next]
      }
    end)
  end

  def parse_line(line) do
    line
    |> String.split(" ")
    |> Enum.map(&String.to_integer/1)
  end

  def extrapolate(xs) do
    if only_zeros(xs) do
      %{prev: 0, next: 0}
    else
      zipped = Enum.zip(xs, Enum.drop(xs, 1))
      diffs = Enum.map(zipped, fn {x, y} -> y - x end)

      next_line = extrapolate(diffs)
      prev = Map.get(next_line, :prev)
      next = Map.get(next_line, :next)

      %{prev: Enum.at(xs, 0) + prev, next: Enum.at(xs, -1) + next}
    end
  end

  def only_zeros(xs) do
    Enum.all?(xs, fn x -> x == 0 end)
  end
end

AdventOfCode.main()

ExUnit.start()

defmodule AdventOfCodeTest do
  use ExUnit.Case, async: true

  test "parse first line of AoC test" do
    values = AdventOfCode.parse_line("0 3 6 9 12 15")
    assert AdventOfCode.extrapolate(values) == %{next: 18, prev: 3}
  end

  test "parse second line of AoC test" do
    values = AdventOfCode.parse_line("1 3 6 10 15 21")
    assert AdventOfCode.extrapolate(values) == %{next: 28, prev: 4}
  end

  test "parse third line of AoC test" do
    values = AdventOfCode.parse_line("10 13 16 21 30 45")
    assert AdventOfCode.extrapolate(values) == %{next: 68, prev: 15}
  end
end

defmodule AdventOfCode do
  def main_timed do
    {time, _} = :timer.tc(AdventOfCode, :main, [])
    milliseconds = time / 1000
    IO.puts("Time: #{milliseconds} milliseconds")
  end

  def main do
    IO.puts("Day 07")
    file_path = "07.test"
    # file_path = "07.input"

    lines =
      file_path
      |> read_input()
      |> Enum.map(&parse_line/1)

    IO.puts("Part 1 solution: #{solve_part1(lines)}")
    IO.puts("Part 2 solution: #{solve_part2(lines)}")
  end

  def read_input(path) do
    File.read!(path)
    |> String.split("\n")
    |> Enum.filter(&(&1 != ""))
  end

  def parse_line(line) do
    [head, tail] = String.split(line, ":", parts: 2)

    [
      String.to_integer(head),
      tail
      |> String.trim()
      |> String.split()
      |> Enum.map(&String.to_integer/1)
    ]
  end

  def solve_part1(equations) do
    equations
    |> Enum.filter(&solve1/1)
    |> Enum.map(fn [value | _] -> value end)
    |> Enum.sum()
  end

  def solve1([value, [first]]), do: value == first

  def solve1([value, [first, second | rest]]) do
    solve1([value, [first * second] ++ rest]) or
      solve1([value, [first + second] ++ rest])
  end

  def solve_part2(equations) do
    equations
    |> Enum.filter(&solve2/1)
    |> Enum.map(fn [value | _] -> value end)
    |> Enum.sum()
  end

  def solve2([value, [first]]), do: value == first

  def solve2([value, [first, second | rest]]) do
    solve2([value, [first * second] ++ rest]) or
      solve2([value, [first + second] ++ rest]) or
      solve2([value, [concat(first, second)] ++ rest])
  end

  def concat(a, b) do
    shift =
      :math.pow(
        10,
        Integer.digits(b)
        |> length()
      )
      |> round()

    a * shift + b
  end
end

AdventOfCode.main_timed()

ExUnit.start()

defmodule AdventOfCodeTest do
  use ExUnit.Case, async: true

  describe "parser" do
    test "parse testdata" do
      testdata = "190: 10 19"

      assert AdventOfCode.parse_line(testdata) ==
               [190, [10, 19]]
    end
  end

  describe "Part 1" do
    test "test solve_part1 parser" do
      assert AdventOfCode.solve1([190, [10, 19]]) == true
    end

    test "test solve_part1" do
      testdata = [
        [190, [10, 19]],
        [3267, [81, 40, 27]],
        [83, [17, 5]],
        [156, [15, 6]],
        [7290, [6, 8, 6, 15]],
        [161_011, [16, 10, 13]],
        [192, [17, 8, 14]],
        [21037, [9, 7, 18, 13]],
        [292, [11, 6, 16, 20]]
      ]

      assert AdventOfCode.solve_part1(testdata) == 3749
    end
  end

  describe "Part 2" do
    test "test solve_part2" do
      testdata = [
        [190, [10, 19]],
        [3267, [81, 40, 27]],
        [83, [17, 5]],
        [156, [15, 6]],
        [7290, [6, 8, 6, 15]],
        [161_011, [16, 10, 13]],
        [192, [17, 8, 14]],
        [21037, [9, 7, 18, 13]],
        [292, [11, 6, 16, 20]]
      ]

      assert AdventOfCode.solve_part2(testdata) == 11387
    end
  end
end

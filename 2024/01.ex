defmodule AdventOfCode do
  def main_timed do
    {time, _} = :timer.tc(AdventOfCode, :main, [])
    milliseconds = time / 1000
    IO.puts("Time: #{milliseconds} milliseconds")
  end

  def main do
    IO.puts("Day 01")
    file_path = "01.input"
    lines = read_input(file_path)

    IO.puts("Part 1 solution: #{solve_part1(lines)}")
    IO.puts("Part 2 solution: #{solve_part2(lines)}")
  end

  def read_input(path) do
    File.read!(path)
    |> String.split("\n")
    |> Enum.map(&String.trim/1)
    |> Enum.map(&String.split(&1))
    |> Enum.filter(&(Enum.count(&1) > 0))
  end

  def solve_part1(lines) do
    arr1 =
      lines
      |> Enum.map(&Enum.at(&1, 0))
      |> Enum.map(&String.to_integer(&1))
      |> Enum.sort()

    arr2 =
      lines
      |> Enum.map(&Enum.at(&1, 1))
      |> Enum.map(&String.to_integer(&1))
      |> Enum.sort()

    Enum.zip(arr1, arr2)
    |> Enum.map(fn {first, second} ->
      abs(first - second)
    end)
    |> Enum.sum()
  end

  def solve_part2(lines) do
    arr1 =
      lines
      |> Enum.map(&Enum.at(&1, 0))
      |> Enum.map(&String.to_integer(&1))

    arr2 =
      lines
      |> Enum.map(&Enum.at(&1, 1))
      |> Enum.map(&String.to_integer(&1))
      |> Enum.group_by(& &1)
      |> Map.new(fn {key, value} -> {key, Enum.count(value)} end)

    arr1
    |> Enum.map(&(&1 * Map.get(arr2, &1, 0)))
    |> Enum.sum()
  end
end

AdventOfCode.main_timed()

ExUnit.start()

defmodule AdventOfCodeTest do
  use ExUnit.Case, async: true

  describe "Part 1" do
    test "test solve_part1" do
      testdata = [
        ["3", "4"],
        ["4", "3"],
        ["2", "5"],
        ["1", "3"],
        ["3", "9"],
        ["3", "3"]
      ]

      assert AdventOfCode.solve_part1(testdata) == 11
    end
  end

  describe "Part 2" do
    test "test solve_part2" do
      testdata = [
        ["3", "4"],
        ["4", "3"],
        ["2", "5"],
        ["1", "3"],
        ["3", "9"],
        ["3", "3"]
      ]

      assert AdventOfCode.solve_part2(testdata) == 31
    end
  end
end

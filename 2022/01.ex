IO.puts("\e[H\e[2J")

defmodule AdventOfCode do
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
  end

  def solve_part1(lines) do
    lines
    |> Enum.reduce([], fn curr, acc ->
      case {curr, acc} do
        {"", acc} -> [0 | acc]
        {curr, [head | tail]} -> [head + String.to_integer(curr) | tail]
        {_, acc} -> acc
      end
    end)
    |> Enum.max()
  end

  def solve_part2(lines) do
    lines
    |> Enum.reduce([], fn curr, acc ->
      case {curr, acc} do
        {"", acc} -> Enum.concat([0], acc)
        {curr, [head | tail]} -> Enum.concat([head + String.to_integer(curr)], tail)
        {_, acc} -> acc
      end
    end)
    |> Enum.sort(&>=/2)
    |> Enum.take(3)
    |> Enum.sum()
  end
end

AdventOfCode.main()

ExUnit.start()

defmodule AdventOfCodeTest do
  use ExUnit.Case, async: true

  describe "Part 1" do
    test "parse input" do
      file_path = "01.test"
      lines = AdventOfCode.read_input(file_path)
      assert Enum.count(lines) == 15
      assert Enum.at(lines, 0) == "1000"
    end

    test "test data" do
      file_path = "01.test"
      lines = AdventOfCode.read_input(file_path)
      result = AdventOfCode.solve_part1(lines)
      assert result == 24000
    end
  end

  describe "Part 2" do
    test "test data" do
      file_path = "01.test"
      lines = AdventOfCode.read_input(file_path)
      result = AdventOfCode.solve_part2(lines)
      assert result == 45000
    end
  end
end

defmodule AdventOfCode do
  def main_timed do
    {time, _} = :timer.tc(AdventOfCode, :main, [])
    milliseconds = time / 1000
    IO.puts("Time: #{milliseconds} milliseconds")
  end

  def main do
    IO.puts("Day 03")
    file_path = "03.input"
    lines = read_input(file_path)

    IO.puts("Part 1 solution: #{solve_part1(lines)}")
    IO.puts("Part 2 solution: #{solve_part2(lines)}")
  end

  def read_input(path) do
    File.read!(path)
    |> String.split("\n")
    |> Enum.filter(&(&1 != ""))
  end

  def solve_part1(lines) do
    lines
    |> Enum.map(&parse_line(&1, true))
    |> Enum.map(&multiply_line/1)
    |> Enum.sum()
  end

  def solve_part2(lines) do
    lines
    |> Enum.join("\n")
    |> parse_line(true)
    |> filter_enabled()
    |> Enum.map(&multiply/1)
    |> Enum.sum()
  end

  def parse_line("", _enabled), do: []
  def parse_line("do()" <> rest, _enabled), do: parse_line(rest, true)
  def parse_line("don't()" <> rest, _enabled), do: parse_line(rest, false)
  def parse_line("mul(" <> rest, enabled), do: try_multiply(rest, enabled)
  def parse_line(<<_::utf8, rest::binary>>, enabled), do: parse_line(rest, enabled)

  def try_multiply(rest, enabled) do
    case Regex.run(~r/^(\d+),(\d+)\)/, rest) do
      [_, num1, num2] ->
        [
          {:ok, {String.to_integer(num1), String.to_integer(num2), enabled}}
          | parse_line(rest, enabled)
        ]

      _ ->
        parse_line(rest, enabled)
    end
  end

  def filter_enabled(line) do
    line
    |> Enum.filter(fn
      {:ok, {_, _, true}} -> true
      _ -> false
    end)
  end

  def multiply_line(line), do: Enum.map(line, &multiply/1) |> Enum.sum()
  def multiply({:ok, {num1, num2, _}}), do: num1 * num2
end

AdventOfCode.main_timed()

ExUnit.start()

defmodule AdventOfCodeTest do
  use ExUnit.Case, async: true

  describe "Part 1" do
    test "test solve_part1" do
      testdata = [
        "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
      ]

      assert AdventOfCode.solve_part1(testdata) == 161
    end
  end

  describe "Part 2" do
    test "test solve_part2" do
      testdata = [
        "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
      ]

      assert AdventOfCode.solve_part2(testdata) == 48
    end
  end
end

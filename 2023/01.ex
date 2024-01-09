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
    |> Enum.filter(&(&1 != ""))
  end

  def solve_part1(lines) do
    lines |> Enum.map(&calibration_values/1) |> Enum.sum()
  end

  def solve_part2(lines) do
    lines
    |> Enum.map(&replace_words/1)
    |> Enum.map(&calibration_values/1)
    |> Enum.sum()
  end

  def calibration_values(line) do
    first = first_digit(line)
    reverse_line = String.reverse(line)
    last = first_digit(reverse_line)
    sum = first <> last
    sum |> String.to_integer()
  end

  def first_digit(line) do
    Regex.scan(~r/\d/, line) |> List.first() |> List.first()
  end

  def replace_words(line) do
    line
    |> String.replace("one", "one1one")
    |> String.replace("two", "two2two")
    |> String.replace("three", "three3three")
    |> String.replace("four", "four4four")
    |> String.replace("five", "five5five")
    |> String.replace("six", "six6six")
    |> String.replace("seven", "seven7seven")
    |> String.replace("eight", "eight8eight")
    |> String.replace("nine", "nine9nine")
    |> String.replace("zero", "zero0zero")
  end
end

AdventOfCode.main_timed()

ExUnit.start()

defmodule AdventOfCodeTest do
  use ExUnit.Case, async: true

  describe "Part 1" do
    test "1abc2" do
      assert AdventOfCode.calibration_values("1abc2") == 12
    end

    test "pqr3stu8vwx" do
      assert AdventOfCode.calibration_values("pqr3stu8vwx") == 38
    end

    test "a1b2c3d4e5f" do
      assert AdventOfCode.calibration_values("a1b2c3d4e5f") == 15
    end

    test "treb7uchet" do
      assert AdventOfCode.calibration_values("treb7uchet") == 77
    end

    test "part1 test" do
      lines = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
      assert AdventOfCode.solve_part1(lines) == 142
    end
  end

  describe "Part 2" do
    test "eightwothree" do
      lines = ["eightwothree"]
      assert AdventOfCode.solve_part2(lines) == 83
    end

    test "two1nine" do
      lines = ["two1nine"]
      assert AdventOfCode.solve_part2(lines) == 29
    end

    test "abcone2threexyz" do
      lines = ["abcone2threexyz"]
      assert AdventOfCode.solve_part2(lines) == 13
    end

    test "xtwone3four" do
      lines = ["xtwone3four"]
      assert AdventOfCode.solve_part2(lines) == 24
    end

    test "4nineeightseven2" do
      lines = ["4nineeightseven2"]
      assert AdventOfCode.solve_part2(lines) == 42
    end

    test "part2 test" do
      lines = [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen"
      ]

      assert AdventOfCode.solve_part2(lines) == 281
    end
  end
end

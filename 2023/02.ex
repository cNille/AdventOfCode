defmodule AdventOfCode do
  def main_timed do
    {time, _} = :timer.tc(AdventOfCode, :main, [])
    milliseconds = time / 1000
    IO.puts("Time: #{milliseconds} milliseconds")
  end

  def main do
    IO.puts("Day 02")
    file_path = "02.input"
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
    r = 12
    g = 13
    b = 14

    lines
    |> Enum.map(&parse_line/1)
    |> Enum.map(fn game ->
      if Enum.count(
           game[:game]
           |> Enum.map(fn game -> is_possible_game(game, r, g, b) end)
           |> Enum.filter(&(&1 == false))
         ) == 0 do
        game[:game_id]
      else
        0
      end
    end)
    |> Enum.sum()
  end

  def parse_line(line) do
    [game_data, cubes] = String.split(line, ": ")
    game_id = String.to_integer(List.last(String.split(game_data, " ")))
    game = String.split(cubes, "; ")
    %{game_id: game_id, game: game}
  end

  def is_possible_game(draw, r, g, b) do
    max_draws = get_all_max(draw)

    within_red = max_draws[:red] <= r
    within_green = max_draws[:green] <= g
    within_blue = max_draws[:blue] <= b
    within_red && within_green && within_blue
  end

  def solve_part2(lines) do
    init = %{:red => 0, :green => 0, :blue => 0}

    lines
    |> Enum.map(&parse_line/1)
    |> Enum.map(fn game ->
      game[:game]
      |> Enum.map(&get_all_max/1)
      |> Enum.reduce(init, &reduce_games/2)
    end)
    |> Enum.map(fn max_draws ->
      max_draws[:red] * max_draws[:green] * max_draws[:blue]
    end)
    |> Enum.sum()
  end

  def get_all_max(draw) do
    init = %{:red => 0, :green => 0, :blue => 0}

    res =
      String.split(draw, ", ")
      |> Enum.map(fn cubes -> get_max(cubes) end)
      |> Enum.reduce(init, &reduce_games/2)

    res
  end

  def reduce_games(x, acc) do
    %{
      :red => max(x[:red], acc[:red]),
      :green => max(x[:green], acc[:green]),
      :blue => max(x[:blue], acc[:blue])
    }
  end

  def get_max(draw) do
    [count, color] = String.split(draw, " ")
    count = String.to_integer(count)

    case color do
      "red" -> %{:red => count, :green => 0, :blue => 0}
      "green" -> %{:red => 0, :green => count, :blue => 0}
      "blue" -> %{:red => 0, :green => 0, :blue => count}
      _ -> IO.puts("Error: #{color}")
    end
  end
end

AdventOfCode.main_timed()

ExUnit.start()

defmodule AdventOfCodeTest do
  use ExUnit.Case, async: true

  describe "Part 1" do
    test "Game 1" do
      line = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"]
      assert AdventOfCode.solve_part1(line) == 1
    end

    test "Game 2" do
      line = ["Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"]
      assert AdventOfCode.solve_part1(line) == 2
    end

    test "Game 3" do
      line = ["Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"]
      assert AdventOfCode.solve_part1(line) == 0
    end

    test "Game 4" do
      line = ["Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"]
      assert AdventOfCode.solve_part1(line) == 0
    end

    test "Game 5" do
      line = ["Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]
      assert AdventOfCode.solve_part1(line) == 5
    end
  end

  describe "Part 2" do
    test "Game 2" do
      line = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"]
      assert AdventOfCode.solve_part2(line) == 48
    end
  end
end

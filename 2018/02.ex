defmodule AdventOfCode do

  def main do
    IO.puts("Day 02")
    file_path = "02.input"
    lines = read_input(file_path)

    IO.puts("Part 1 solution: #{solve_part1(lines)}")
  end

  def read_input(path) do
    File.read!(path)
    |> String.split("\n")
    |> Enum.map(&String.trim/1)
    |> Enum.filter(&(&1 != ""))
  end

  def solve_part1(lines) do
    AdventOfCode.checksum(lines)
  end

  def checksum(lines) do
    %{doubles: doubles, triplets: triplets} = lines
    |> Enum.map(&AdventOfCode.count/1)
    |> Enum.reduce(%{ doubles: 0, triplets: 0}, fn (struct, acc)->
        cond do
          struct.has_double and struct.has_triplet -> %{doubles: acc.doubles + 1, triplets: acc.triplets + 1}
          struct.has_double -> %{doubles: acc.doubles + 1, triplets: acc.triplets}
          struct.has_triplet -> %{doubles: acc.doubles, triplets: acc.triplets + 1}
          true -> acc
        end
      end
     )

    doubles * triplets
  end

  def count(text) do
    characters = String.to_charlist(text)
    origin = String.length(text)
    diffs = Enum.map(characters, fn(char) ->
      filtered_text = Enum.filter(characters, fn c ->
        c != char
      end)
      origin - Enum.count(filtered_text)
    end)

    double_count = diffs
    |> Enum.filter(fn size -> size == 2 end)
    |> Enum.count()

    triplet_count = diffs
    |> Enum.filter(fn size -> size == 3 end)
    |> Enum.count()

    %{has_double: double_count >= 1, has_triplet: triplet_count >= 1}
  end

  def diff_count(txt1, txt2) do
    orig = String.to_charlist(txt1)
    res = String.to_charlist(txt2)
    |> Enum.with_index()
    |> Enum.map(fn {ch, idx} ->
      cond do
        ch == Enum.at(orig, idx) -> 0
        true -> 1
      end
    end)
    |> Enum.sum()
  end
end



AdventOfCode.main()

ExUnit.start()

defmodule AdventOfCodeTest do
  use ExUnit.Case, async: true

  describe "Part 2" do
    test "diff-count" do
      res = AdventOfCode.diff_count("abcde", "axcye")
      assert res == 2
    end
  end

  # describe "Part 1" do
  #   test "abcdef" do
  #     count = AdventOfCode.count("abcdef")
  #     # Assert that there are no doubles
  #     assert count.has_double == false
  #     # Assert that there are no triplets
  #     assert count.has_triplet == false
  #   end

  #    test "bababc" do
  #      count = AdventOfCode.count("bababc")
  #      # Assert that there are no doubles
  #      assert count.has_double == true
  #      # Assert that there are no triplets
  #      assert count.has_triplet == true
  #    end

  #    test "checksum" do
  #       lines = [
  #       "abcdef",
  #       "bababc",
  #       "abbcde",
  #       "abcccd",
  #       "aabcdd",
  #       "abcdee",
  #       "ababab",
  #       ]

  #       checksum = AdventOfCode.checksum(lines)
  #       assert checksum == 12
  #    end
  # end
end

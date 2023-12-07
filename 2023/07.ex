defmodule AdventOfCode do
  def main do
    IO.puts("Day 7")
    file_path = "07.test"
    lines = read_input(file_path)

    # IO.puts("Part 1: #{solve(lines, false)}")
    IO.puts("Part 2: #{solve(lines, true)}")
  end

  def solve(lines, part2) do
    lines
    |> Enum.map(fn x -> get_type(x, part2) end)
    |> Enum.sort(&sorter(&1, &2, part2))
    |> Enum.with_index()
    |> Enum.map(fn {hand, i} ->
      IO.puts("#{i + 1}: #{hand[:hand]} #{hand[:bid]} == #{hand[:bid] * (i + 1)}")
      hand[:bid] * (i + 1)
    end)
    |> Enum.sum()
  end

  def read_input(file_path) do
    File.read!(file_path)
    |> String.split("\n")
    |> Enum.map(&String.trim/1)
    |> Enum.filter(&(&1 != ""))
  end

  def sorter(a, b, part2) do
    IO.puts("a: #{a[:hand]} #{a[:value]}")
    IO.puts("b: #{b[:hand]} #{b[:value]}")

    cond do
      a[:value] > b[:value] ->
        false

      a[:value] < b[:value] ->
        true

      true ->
        bet = better_hand_value(a, b, part2)
        IO.puts("a: #{a[:hand]} #{a[:bid]} #{a[:value]}")

        if bet == "a" do
          false
        else
          true
        end
    end
  end

  def better_hand_value(a, b, part2) do
    hand_a = String.graphemes(a[:hand])
    hand_b = String.graphemes(b[:hand])
    card_values = String.graphemes(get_card_values(part2))

    Enum.zip(hand_a, hand_b)
    |> Enum.reduce("none", fn {a, b}, acc ->
      idx_a = Enum.find_index(card_values, fn x -> x == a end)
      idx_b = Enum.find_index(card_values, fn x -> x == b end)

      cond do
        acc != "none" ->
          acc

        idx_a > idx_b ->
          "a"

        idx_a < idx_b ->
          "b"

        true ->
          acc
      end
    end)
  end

  def get_card_values(part2) do
    if part2 do
      "J23456789TQKA"
    else
      "23456789TJQKA"
    end
  end

  def get_type(line, part2) do
    arr = String.split(line)
    hand = Enum.at(arr, 0)
    bid = String.to_integer(Enum.at(arr, 1))

    types = [
      "high_card",
      "one_pair",
      "two_pair",
      "three_of_a_kind",
      "full_house",
      "four_of_a_kind",
      "five_of_a_kind"
    ]

    # Count each unique character in the hand 
    frequencies =
      hand
      |> String.graphemes()
      |> Enum.frequencies()

    value =
      if !part2 do
        hand_type = type_from_frequencies(frequencies)
        hand_value = Enum.find_index(types, &(&1 == hand_type))
        hand_value
      else
        j_count = Enum.count(frequencies, fn {k, _} -> k == "J" end)

        frequencies
        |> Enum.map(fn {k, _} ->
          if k != "J" do
            new_freq =
              Enum.map(frequencies, fn {k2, v2} ->
                cond do
                  k2 == "J" ->
                    {k2, 0}

                  k2 == k ->
                    {k2, v2 + j_count}

                  true ->
                    {k2, v2}
                end
              end)

            hand_type = type_from_frequencies(new_freq)
            hand_value = Enum.find_index(types, &(&1 == hand_type))
            hand_value
          else
            hand_type = type_from_frequencies(frequencies)
            hand_value = Enum.find_index(types, &(&1 == hand_type))
            hand_value
          end
        end)
        |> Enum.max()
      end

    IO.puts("hand: #{hand} bid: #{bid} value: #{value}")
    %{value: value, hand: hand, bid: bid}
  end

  def type_from_frequencies(frequencies) do
    # Get the values of the frequencies
    values = Enum.map(frequencies, fn {_, v} -> v end)

    cond do
      Enum.member?(values, 5) ->
        "five_of_a_kind"

      Enum.member?(values, 4) ->
        "four_of_a_kind"

      Enum.member?(values, 3) and Enum.member?(values, 2) ->
        "full_house"

      Enum.member?(values, 3) ->
        "three_of_a_kind"

      Enum.count(values, fn x -> x == 2 end) == 2 ->
        "two_pair"

      Enum.count(values, fn x -> x == 2 end) == 1 ->
        "one_pair"

      true ->
        "high_card"
    end
  end
end

# AdventOfCode.main()

ExUnit.start()

defmodule AdventOfCodeTest do
  use ExUnit.Case, async: true

  test "Check for five-of-a-kind, part 1" do
    assert AdventOfCode.get_type("AAAAA 1", false) == %{value: 6, hand: "AAAAA", bid: 1}
  end

  test "Check for four-of-a-kind, part 1" do
    assert AdventOfCode.get_type("AAAAK 1", false) == %{value: 5, hand: "AAAAK", bid: 1}
  end

  test "Check for full-house, part 1" do
    assert AdventOfCode.get_type("AAABB 1", false) == %{value: 4, hand: "AAABB", bid: 1}
  end

  test "Check for three-of-a-kind, part 1" do
    assert AdventOfCode.get_type("AAABC 1", false) == %{value: 3, hand: "AAABC", bid: 1}
  end

  test "Check for two-pair, part 1" do
    assert AdventOfCode.get_type("AABBC 1", false) == %{value: 2, hand: "AABBC", bid: 1}
  end

  test "Check for one-pair, part 1" do
    assert AdventOfCode.get_type("AABCD 1", false) == %{value: 1, hand: "AABCD", bid: 1}
  end

  test "Check for high-card, part 1" do
    assert AdventOfCode.get_type("ABCDE 1", false) == %{value: 0, hand: "ABCDE", bid: 1}
  end

  # # Use J as joker
  test "Check for JJJJJ, part 2" do
    assert AdventOfCode.get_type("JJJJJ 1", true) == %{value: 6, hand: "JJJJJ", bid: 1}
  end

  test "Check for JJJJK, part 2" do
    assert AdventOfCode.get_type("JJJJK 1", true) == %{value: 6, hand: "JJJJK", bid: 1}
  end

  test "Check for KKKJQ, part 2" do
    assert AdventOfCode.get_type("KKKJQ 1", true) == %{value: 5, hand: "KKKJQ", bid: 1}
  end

  test "Check for 3355J, part 2" do
    assert AdventOfCode.get_type("3355J 1", true) == %{value: 4, hand: "3355J", bid: 1}
  end

  test "Check for J2279, part 2" do
    assert AdventOfCode.get_type("J2279 1", true) == %{value: 3, hand: "J2279", bid: 1}
  end

  test "Check for J1234, part 2" do
    assert AdventOfCode.get_type("J1234 1", true) == %{value: 2, hand: "J1234", bid: 1}
  end

  test "Check for 4JAK5, part 2" do
    assert AdventOfCode.get_type("4JAK5 1", true) == %{value: 1, hand: "4JAK5", bid: 1}
  end

  test "Check for JJ45A, part 2" do
    assert AdventOfCode.get_type("JJ45A 1", true) == %{value: 3, hand: "JJ45A", bid: 1}
  end
end

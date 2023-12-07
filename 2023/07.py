from typing import Counter


print(chr(27)+'[2j')
print('\033c')
f = open('07.input', 'r')
#f = open('07.test', 'r')
lines = [x.strip() for x in f.readlines()]

print('Day 07')
part2 = False

types = [
    'high_card',
    'one_pair',
    'two_pairs',
    'three_of_a_kind',
    'full_house',
    'four_of_a_kind',
    'five_of_a_kind',
]

def is_full_house(hand):
    if hand[0] == hand[1] and hand[2] == hand[4]:
        return True
    elif hand[0] == hand[2] and hand[3] == hand[4]:
        return True
    return False


def type_from_counts(counts):
    if 5 in counts.values():
        return 'five_of_a_kind' # 6
    elif 4 in counts.values():
        return 'four_of_a_kind' # 5
    elif 3 in counts.values() and 2 in counts.values():
        return 'full_house' # 4
    elif 3 in counts.values():
        return 'three_of_a_kind' # 3
    elif len([x for x in counts.values() if x == 2]) == 2:
        return 'two_pairs' # 2
    elif len([x for x in counts.values() if x == 2]) == 1:
        return 'one_pair' # 1
    else:
         return 'high_card' # 0

def get_type(line):
    hand, bid = line.split()
    bid = int(bid)

    hand_type = 'high_card'
    counts = Counter(hand)
    max_idx = 0
    if part2:
        # Get count of 'J'
        jokers = counts['J']
        # Add jokers to counts of all other cards
        for k in counts:
            counts_copy = counts.copy()
            if k != 'J':
                counts_copy[k] += jokers
                counts_copy['J'] = 0
            hand_type = type_from_counts(counts_copy)
            idx = types.index(hand_type)
            if idx > max_idx:
                max_idx = idx

    hand_type = type_from_counts(counts)
    idx = types.index(hand_type)
    idx = max(idx, max_idx)
    return (idx, hand, bid)

# Tests
assert(get_type('AAAAA 1') == (6, 'AAAAA', 1))
assert(get_type('AAAAK 1') == (5, 'AAAAK', 1))
assert(get_type('AAABB 1') == (4, 'AAABB', 1))
assert(get_type('AAABC 1') == (3, 'AAABC', 1))
assert(get_type('AABBC 1') == (2, 'AABBC', 1))
assert(get_type('AABCD 1') == (1, 'AABCD', 1))
assert(get_type('ABCDE 1') == (0, 'ABCDE', 1))

part2 = True
# Use J as joker
assert(get_type('JJJJJ 1') == (6, 'JJJJJ', 1))
assert(get_type('JJJJK 1') == (6, 'JJJJK', 1))
assert(get_type('KKKJQ 1') == (5, 'KKKJQ', 1))
assert(get_type('3355J 1') == (4, '3355J', 1))
assert(get_type('J2279 1') == (3, 'J2279', 1))
assert(get_type('J1234 1') == (1, 'J1234', 1))
assert(get_type('4JAK5 1') == (1, '4JAK5', 1))
assert(get_type('JJ45A 1') == (3, 'JJ45A', 1))
part2 = False


def hand_sort(x):
    if part2:
        card_values = 'J23456789TQKA'
    else:
        card_values = '23456789TJQKA'

    hand_type, hand, _ = x
    sort_rank = (
        hand_type * 10e10 +
        card_values.index(hand[0]) * 10e8+
        card_values.index(hand[1]) * 10e6+
        card_values.index(hand[2]) * 10e4+
        card_values.index(hand[3]) * 10e2+
        card_values.index(hand[4])
    )
    return sort_rank

def solve(lines):
    hands = [get_type(x) for x in lines]
    hands.sort(key=hand_sort)
    winnings = 0
    for i, hand in enumerate(hands):
        rank = i + 1
        winnings += rank * hand[2]
    return winnings

part2 = False
print('Part 1:', solve(lines))
part2 = True
print('Part 2:', solve(lines))

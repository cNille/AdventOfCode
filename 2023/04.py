print(chr(27)+'[2j')
print('\033c')
f = open('04.input', 'r')
content = [x.strip() for x in f.readlines()]
lines = content

print('Day 04:')

def count_card(winning_numbers: set[int], numbers: list[int]) -> int:
    count = 0
    for number in numbers:
        if number in winning_numbers:
            # Double the number of points. USe bitwise shift to multiply by 2
            if count == 0:
                count = 1
            else:
                count *= 2 
    return count

part1 = 0
cards = {}
max_id = 0
for line in lines:
    card, numbers = line.split(': ')
    card_id = int(card[5:])
    all_numbers = numbers.split(' | ')
    winning_numbers = set([int(x) for x in all_numbers[0].split()])
    numbers = [int(x) for x in all_numbers[1].split()]
    count = count_card(winning_numbers, numbers)
    part1 += count 

    # Divide count into power of 2 and remainder
    power = 0
    while count > 1:
        count /= 2
        power += 1
    remainder = count % 2
    power = int(power + remainder)


    cards[card_id] = {'winning_numbers': winning_numbers, 'numbers': numbers, 'count': power, 'times': 1}
    max_id = max(max_id, card_id)

print('Part 1:', part1)

for card in range(1, max_id+1):

    if cards[card]['count'] == 0:
        continue

    for i in range(cards[card]['count']):
        nxt = card+i+1
        if nxt not in cards:
            continue
        cards[nxt]['times'] += cards[card]['times']

part2 = 0
for card in cards:
    part2 += cards[card]['times']

print('Part 2:', part2)

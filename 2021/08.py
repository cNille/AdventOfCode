from itertools import permutations
# f = open('08.input', 'r')
f = open('08.test', 'r')
lines = [x.strip() for x in f.readlines()]

def part1():
    count = 0
    for line in lines:
        inputs,outputs = line.split(' | ')
        w1478 = [w for w in outputs.split() if len(w) in [2,3,4,7]]
        count += len(w1478)
    return count
print("Solution part 1: %d " % part1())

digits = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9,
}

def translate(translation, string):
    digit = ''.join([translation[letter] for letter in string])
    digit = ''.join(sorted(digit))
    return digit

total = 0
for idx, line in enumerate(lines):
    if idx % 20 == 0:
        print('Line %d' % idx)
    inputs, outputs = line.split(' | ')
    inputs, outputs = inputs.split(), outputs.split()
    # Sort by length to quicker find matches by checking
    # the smaller digits first.
    inputs.sort(key=lambda s: len(s))

    for p in permutations('abcdefg'):
        translation = {
                p[0]: 'a',
                p[1]: 'b',
                p[2]: 'c',
                p[3]: 'd',
                p[4]: 'e',
                p[5]: 'f',
                p[6]: 'g',
        }

        # Test out translation to match digits
        success = True
        for i in inputs:
            digit = translate(translation, i)
            if digit not in digits:
                success = False
                break
        if not success:
            continue

        # Found correct translation
        number = ''
        for output in outputs:
            digit = translate(translation, output)
            number += str(digits[digit])
        total += int(number)
        break
print('Solution part 2: %d' % total)


"""
 0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg
"""

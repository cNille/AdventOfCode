f = open('02.input', 'r')
data = [x.strip() for x in f.readlines()]

# Assumptions:
# - 1010 is not present

def part1(data):
    total = 0
    for x in data:
        span, letter, pw = x.split()
        start, end = map(int, span.split('-'))
        count = pw.count(letter[0])
        if start <= count <= end:
            total +=1
    return total

def part2(data):
    total = 0
    for x in data:
        span, letter, pw = x.split()
        start, end = map(int, span.split('-'))

        position1 = pw[start-1] == letter[0]
        position2 = pw[end-1] == letter[0]
        if position1 != position2:
            total +=1

    return total

print("Solution part 1: %d" % part1(data))
print("Solution part 2: %d" % part2(data))


# Alternate solutions
def part1functional(data):
    def validate(line):
        span, letter, pw = line.split()
        start, end = map(int, span.split('-'))
        count = pw.count(letter[0])
        return start <= count <= end
    valid_passwords = filter(validate, data)
    return len(valid_passwords)

import re
def part1regex(data):
    def validate(line):
        start, end, ch, pw = re.search(r'(\d+)-(\d+) (.): (\w+)', line).groups()
        return int(start) <= pw.count(ch) <= int(end)
    valid_passwords = filter(validate, data)
    return len(valid_passwords)

print(part1regex(data))

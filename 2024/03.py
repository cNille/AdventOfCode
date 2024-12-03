print(chr(27)+'[2j')
print('\033c')
f = open('03.input', 'r')
lines = [x.strip() for x in f.readlines()]
import re

part1 = 0
part2 = 0
enabled = True
for line in lines:
    for i in range(len(line)):
        match = re.search(r"^do\(\)", line[i:])
        if match is not None:
            enabled = True

        match = re.search(r"^don't\(\)", line[i:])
        if match is not None:
            enabled = False

        match = re.search(r"^mul\((\d+),(\d+)\)", line[i:])
        if match is not None:
            m = match.groups()
            part1 += int(m[0]) * int(m[1])
            if enabled:
                part2 += int(m[0]) * int(m[1])

print("Solution part 1:", part1)
print("Solution part 2:", part2)

from collections import defaultdict
from functools import cache
from typing import Counter
print(chr(27)+'[2j')
print('\033c')
f = open('20.test', 'r')
f = open('20.input', 'r')

lines = [x.strip() for x in f.readlines()]

for line in lines:
    print(line)

start = (0,0)
end = None
g = {}
for y, row in enumerate(lines):
    for x,c in enumerate(row):
        g[(x,y)] = c
        if c == 'S':
            start = (x,y)
        if c == 'E':
            end = (x,y)

D = [(0, -1), (1,0), (0, 1), (-1,0)]
pos = start
visited = [pos]
while pos != end:
    x,y = pos 
    for (dx,dy) in D:
        x1, y1 = x+dx, y+dy 
        if g[(x1,y1)] == '#':
            continue
        if (x1,y1) in visited[-2:]:
            continue
        pos = x1,y1
        visited.append(pos)
        break
print('Visited:', len(visited))

print('-'*40)

cheats2 = defaultdict(int) 
cheats1 = defaultdict(int)
c = Counter()
for i, (x1,y1) in enumerate(visited):
    if i % 1000 == 0:
        print(f'{i} of {len(visited)}')
    # Part 1
    STEPS = 2
    for (dx,dy) in D:
        x,y = x1 + dx*STEPS, y1 + dy*STEPS
        if (x,y) not in visited[i:]:
            continue
        j = visited.index((x,y))
        cheat = j - i - STEPS
        cheats1[cheat] += 1

    # Part 2
    for j, (x2,y2) in enumerate(visited[i+100:]):
        d = abs(x2-x1) + abs(y2-y1)
        if d <= 20:
            cheat = j - d + 100
            cheats2[cheat] += 1

part1 = 0
for c in cheats1:
    if c >= 100:
        part1 += cheats1[c]
part2 = 0
for c in cheats2:
    if c >= 100:
        part2 += cheats2[c]


print('Part1:', part1)
print('Part2:', part2)

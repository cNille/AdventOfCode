from itertools import permutations
from heapq import heappush, heappop
print(chr(27)+'[2j')
print('\033c', end='')

print("Day 24")
f = open('24.input', 'r')
# f = open('24.test', 'r')
mtx = [x.strip() for x in f.readlines()]


last_num = 0
y = x = 0
targets = {}
number_by_location = {}
for row, line in enumerate(mtx):
    for col, letter in enumerate(line):
        if letter.isdigit():
            targets[int(letter)] = (col, row)
            number_by_location[(col, row)] = int(letter)
            last_num = max(last_num, int(letter))
        if letter == '0':
            x = col
            y = row

new_t = []
for i in range(len(targets)):
    new_t.append(targets[i])
targets = new_t

pairs = set()
for t1 in targets:
    for t2 in targets:
        if t1 == t2:
            continue
        pairs.add((t1, t2))


def find_shortest_path(x1, y1, x2, y2):
    global mtx

    visited = set()
    q = []
    heappush(q, (0, x1, y1))
    while q:
        steps, x, y = heappop(q)
        if (x, y) == (x2, y2):
            return steps
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            if mtx[y+dy][x+dx] != '#':
                heappush(q, (steps+1, x+dx, y+dy))


paths = {}
for i, (t1, t2) in enumerate(pairs):
    shortest_path = find_shortest_path(t1[0], t1[1], t2[0], t2[1])
    paths[(t1, t2)] = shortest_path


# part 1
min_path = 10000000
for p in permutations(range(1, last_num+1)):
    # Start from 0
    path = paths[((targets[0]), (targets[p[0]]))]
    # Add up all pairs
    distances = []
    for i in range(len(p)-1):
        d = paths[((targets[p[i]]), (targets[p[i+1]]))]
        distances.append(d)
        path += d
    min_path = min(min_path, path)

print("Part 1:", min_path)

# part 2
min_path = 10000000
for p in permutations(range(1, last_num+1)):
    # Start from 0
    path = paths[((targets[0]), (targets[p[0]]))]
    # Add up all pairs
    distances = []
    for i in range(len(p)-1):
        d = paths[((targets[p[i]]), (targets[p[i+1]]))]
        distances.append(d)
        path += d
    path += paths[((targets[p[-1]]), (targets[0]))]
    min_path = min(min_path, path)

print("Part 2:", min_path)

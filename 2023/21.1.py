from heapq import heappush, heappop
print(chr(27)+'[2j')
print('\033c')
f = open('21.test', 'r')
f = open('21.input', 'r')
lines = [x.strip() for x in f.readlines()]
RESET = '\033[0m'
RED = '\033[91m'
GREEN = '\033[92m'


rocks = set()
empty = set()


def print_map(visited, rocks, lines):
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if (x, y) in visited:
                print(GREEN+'O'+RESET, end='')
            elif (x, y) in rocks:
                print(RED + '#' + RESET, end='')
            else:
                print(lines[y][x], end='')
        print()


start = (0, 0)
for y, row in enumerate(lines):
    for x, char in enumerate(row):
        if char == 'S':
            start = (x, y)
        elif char == '#':
            rocks.add((x, y))
        else:
            empty.add((x, y))

# Width 131
# Height 131
# Startpos: 65,65

N, E, W, S = (0, -1), (1, 0), (-1, 0), (0, 1)
DIRECTIONS = [N, E, W, S]
pos = start


visited = set()
queue = []
heappush(queue, (0, pos))
steps = 64
#steps = 26501365
max_steps = 0
step_list = {}
while queue:
    depth, pos = heappop(queue)
    x, y = pos
    if depth > max_steps:
        max_steps = depth
        # print('-'*10)
        # print_map(step_list[depth-1], rocks, lines)
        # reached = len(step_list[depth-1])
        # print('Plots reached', reached, 'after', depth-1)
    if depth > steps:
        continue
    if pos in rocks:
        continue
    # if pos in visited:
    #    continue
    # visited.add(pos)
    if depth not in step_list:
        step_list[depth] = set()
    if pos in step_list[depth]:
        continue
    step_list[depth].add(pos)

    # empty.remove(pos)
    for d in DIRECTIONS:
        dx, dy = d
        new_pos = (x+dx, y+dy)
        new_pos = (new_pos[0] % len(lines[0]), new_pos[1] % len(lines))
        heappush(queue, (depth+1, new_pos))

for i in range(steps+1):
    print('-'*30)
    print('Step', i)
    print('Plots reached', len(step_list[i]))
    #print_map(step_list[i], rocks, lines)

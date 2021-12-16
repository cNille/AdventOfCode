print(chr(27)+'[2j')
print('\033c')
from collections import deque
import heapq
f = open('15.test', 'r')
f = open('15.input', 'r')
lines = [x.strip() for x in f.readlines()]

cave = []
for line in lines:
    cave.append([int(x) for x in line])

def print_cave(cave):
    print('-- Cave')
    for row in cave:
        print(''.join([str(x) for x in row]))

def get_neighbours(cave, position):
    x,y = position
    neighbours = [
        (x + 1, y), (x, y + 1),
        (x - 1, y), (x, y - 1),
    ] 
    return [(nx,ny) 
        for (nx,ny)
        in neighbours
        if 0 <= nx < len(cave[0]) 
        and 0 <= ny < len(cave) 
    ] 

def quickest_path(cave):
    START = (0,0)
    ROWS = len(cave)-1
    COLS = len(cave[0])-1
    queue = [(ROWS+COLS, 0, START)]
    heapq.heapify(queue)
    cache = {(0,0): 0 }
    while len(queue) > 0:
        heuristic, path_score, position = heapq.heappop(queue) 
        if position not in cache or path_score < cache[position]:
            cache[position] = path_score
        if position in cache and path_score > cache[position]:
            continue
        
        neighbours = get_neighbours(cave, position)
        next_step = [
            (path_score + cave[ny][nx], (nx,ny))
            for (nx,ny) in neighbours
        ]
        for step in next_step:
            score, pos = step
            if pos in cache and cache[pos] <= step[0]:
                continue
            heuristic = score + (ROWS - pos[1]) + (COLS - pos[0])
            queue.append((heuristic, score, pos))
    last_pos = (COLS, ROWS)
    result = cache[last_pos]
    return result

print("Solution part1: %d" % quickest_path(cave))

cave2 = []

ROWS = len(cave)
COLS = len(cave[0])
for y in range(ROWS * 5):
    cave2.append([])
    ydelta = int(y / ROWS)
    for x in range(COLS*5):
        xdelta = int(x / COLS)
        old_value = cave[y%ROWS][x%COLS]
        new_value = (old_value + xdelta + ydelta)
        new_value = new_value - 9 if new_value > 9 else new_value
        cave2[y].append(new_value) 

print("Solution part2: %d" % quickest_path(cave2))

# print_cave(cave2)

# for y in range(ROWS+1):
#     print('\t'.join([str(cache[(x,y)]) for x in range(COLS+1)]))

# 360 too low

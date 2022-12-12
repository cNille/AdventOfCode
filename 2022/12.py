print(chr(27)+'[2j')
print('\033c')
f = open('12.test', 'r')
#f = open('12.input', 'r')
lines = [x.strip() for x in f.readlines()]

print("Day 12")

mtx = []
pos = (0,0) 
end = (0,0) 
for y,line in enumerate(lines):
    print(line)
    row = []
    for x, ch in enumerate(line):
        level = ch
        if ch == "S":
            level = "a" 
            # part1
            pos = (x,y)
        elif ch == "E":
            end = (x,y)
            level = "z"
            # part2
            pos = (x,y)
        row.append(ord(level) - 97)
    mtx.append(row)

finished = False

def get_neighbour(mtx,x,y):
    if y < 0 or y >= len(mtx):
        return None
    if x < 0 or x >= len(mtx[0]):
        return None
    return (x,y) 

def get_neighbours(mtx, x,y):
    neighbours = [
        get_neighbour(mtx, x - 1, y + 0),
        get_neighbour(mtx, x + 1, y + 0),
        get_neighbour(mtx, x + 0, y - 1),
        get_neighbour(mtx, x + 0, y + 1),
    ]
    return [n for n in neighbours if n is not None]

def print_map(least_steps):
    for line in least_steps:
        row = ""
        for s in line:
            if s == MOST_STEPS:
                row += "."
            else:
                row += str(s % 10)
        print(row)

MOST_STEPS = 999999999
least_steps = []
for y,line in enumerate(mtx):
    row = []
    for x, ch in enumerate(line):
        row.append(MOST_STEPS)
    least_steps.append(row)

from collections import deque
queue = deque()
queue.append((pos[0], pos[1], 0))

# least_steps = 9999999
visited = set()
print("END", end)
while len(queue) > 0:
    x,y,steps = queue.popleft()
    if least_steps[y][x] <= steps:
        continue
    least_steps[y][x] = steps
    visited.add((x,y))
    print("Q: %d, visited: %d" % (len(queue), len(visited)))

    # part1
    # if end == (x,y):
    # part2
    if mtx[y][x] == 0:
        finished = True
        end = (x,y)
        break

    neighbours = get_neighbours(mtx, x,y)
    curr_level = mtx[y][x]
    
    for nx,ny in neighbours:
        level = mtx[ny][nx]
        # part1
        #if (level - curr_level) <= 1:
        # part2
        if (curr_level - level) <= 1:
            queue.append((nx,ny,steps+1))
    print_map(least_steps)

if not finished:
    print("No solution")
    exit()

print("Solution :", least_steps[end[1]][end[0]])

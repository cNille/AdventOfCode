import sys
sys.setrecursionlimit(50000)
print(chr(27)+'[2j')
print('\033c')
f = open('10.input', 'r')
#f = open('10.test', 'r')
#f = open('10.test2', 'r')
#f = open('10.test3', 'r')
#f = open('10.test4', 'r')
lines = [x.strip() for x in f.readlines()]

print('Day 10')

# Add an edge with '.' around the map. Meaning a first row, last row, first column and last column
def add_edges(lines):
    new_lines = []
    for line in lines:
        new_lines.append('.'+line+'.')
    new_lines.insert(0, '.'*len(new_lines[0]))
    new_lines.append('.'*len(new_lines[0]))
    return new_lines

def get_start_pos(lines) -> tuple[int, int]:
    for y, line in enumerate(lines):
        for x, ch in enumerate(line):
            if ch == 'S':
                return (x, y)
    raise Exception('No start position found')

def get_neighbours(lines, x, y):
    ns = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
    ns = [(nx, ny) for nx, ny in ns if within_bounds(nx, ny, lines)]
    return ns

def within_bounds(x, y, lines):
    return x >= 0 and y >= 0 and x < len(lines[0]) and y < len(lines)

def print_map(lines, loop, ins, outs):
    GREEN = '\033[92m'
    RED = '\033[91m'
    RESET = '\033[0m'
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if (x, y) in loop:
                print(lines[y][x], end='')
            elif (x, y) in ins:
                print(GREEN+'I'+RESET, end='')
            elif (x, y) in outs:
                print(RED+'O'+RESET, end='')
            else:
                print('.', end='')
        print()


def check_connection(lines, x,y, nx, ny):
    to_left = nx < x and ny == y
    to_right = nx > x and ny == y
    to_up = nx == x and ny < y
    to_down = nx == x and ny > y
    connects_east = lines[ny][nx] in ['-', 'F', 'L']
    connects_west = lines[ny][nx] in ['-', 'J', '7']
    connects_south = lines[ny][nx] in ['|', 'F', '7']
    connects_north = lines[ny][nx] in ['|', 'J', 'L']
    if to_left and not connects_east:
        return False
    if to_right and not connects_west:
        return False
    if to_up and not connects_south:
        return False
    if to_down and not connects_north:
        return False
    return True

def solve1(lines):
    max_dist = 0
    curr =  get_start_pos(lines)
    print('Start position:', curr)
    loop = set([curr])
    queue: list[tuple[tuple[int, int], int]] = [(curr, 0)]
    while len(queue) > 0:
        curr, steps = queue.pop(0)
        nxt_steps = steps + 1
        x, y = curr
        for n in get_neighbours(lines, x, y):
            if n in loop:
                continue
            nx, ny = n
            is_connected = check_connection(lines, x, y, nx, ny)
            if not is_connected:
                continue
            queue.append((n, nxt_steps))
            loop.add(n)
            max_dist = max(max_dist, nxt_steps)
    return max_dist 

lines = add_edges(lines)
print("Part 1:", solve1(lines))

# Part 2
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
DIRS = [UP, RIGHT, DOWN, LEFT]
def new_direction(lines, x,y, d):
    ch = lines[y][x]
    if ch == '-':
        return d
    if ch == '|':
        return d
    if ch == 'F' and d == UP:
        return RIGHT
    if ch == 'F' and d == LEFT:
        return DOWN
    if ch == 'L' and d == DOWN:
        return RIGHT
    if ch == 'L' and d == LEFT:
        return UP
    if ch == 'J' and d == RIGHT:
        return UP
    if ch == 'J' and d == DOWN:
        return LEFT
    if ch == '7' and d == RIGHT:
        return DOWN
    if ch == '7' and d == UP:
        return LEFT
    raise Exception('Unknown direction')

def get_new_side(side, curr, direction, new_direction):
    d1_idx = DIRS.index(direction)
    d2_idx = DIRS.index(new_direction)

    # Add new side before turning
    sx, sy = side[-1]
    new_side = side.copy()
    new_side.append((sx+direction[0], sy+direction[1]))
    sx, sy = new_side[-1]
    if d1_idx == d2_idx:
        return new_side

    # Add new side after turning
    cx, cy = curr
    dx, dy = cx - sx, cy - sy
    side_dir = DIRS.index((dx, dy))
    if d1_idx == (d2_idx + 1) % 4:
        side_dir = (side_dir + 1) % 4
        dx, dy = DIRS[side_dir]
        new_side.append((cx+dx, cy+dy))
    elif d1_idx == (d2_idx - 1) % 4:
        side_dir = (side_dir - 1) % 4
        dx, dy = DIRS[side_dir]
        new_side.append((cx+dx, cy+dy))
    return new_side

        

def follow_pipe(lines, loop, curr, direction, side1, side2):
    if curr in loop:
        return loop, side1, side2
    x, y = curr
    loop.add(curr)
    dx, dy = direction
    nx, ny = (x+dx, y+dy)
    if lines[ny][nx] == 'S':
        return loop, side1, side2
    d2 = new_direction(lines, nx, ny, direction)

    curr = (nx, ny)
    new_side1 = get_new_side(side1, curr, direction, d2)
    new_side2 = get_new_side(side2, curr, direction, d2)
    return follow_pipe(lines, loop, curr, d2, new_side1, new_side2)


curr: tuple[int,int] = get_start_pos(lines)
ns = get_neighbours(lines, curr[0], curr[1])
ns = [n for n in ns if check_connection(lines, curr[0], curr[1], n[0], n[1])]
d = (ns[0][0] - curr[0], ns[0][1] - curr[1])
if d == UP or d == DOWN:
    side1 = [(curr[0]+1, curr[1])]
    side2 = [(curr[0]-1, curr[1])]
else:
    side1 = [(curr[0], curr[1]+1)]
    side2 = [(curr[0], curr[1]-1)]
loop = set()
loop, side1, side2 = follow_pipe(lines, loop, curr, d, side1, side2)

side1 = set([x for x in side1 if x not in loop])
side2 = set([x for x in side2 if x not in loop])

dangling = []
for y, line in enumerate(lines):
    for x, ch in enumerate(line):
        if (x, y) in loop:
            continue
        if (x, y) in side1:
            continue
        if (x, y) in side2:
            continue
        dangling.append([(x, y)])

# For all dangling, recursively get neighbours not in loop, and merge with side1 or side2
def get_neighbours_not_in_loop(lines, loop, curr):
    x, y = curr
    ns = get_neighbours(lines, x, y)
    return [n for n in ns if n not in loop]

while len(dangling) > 0:
    curr_set = dangling.pop(0)
    curr = curr_set[-1]
    x, y = curr
    ns = get_neighbours(lines, x, y)
    ns = [n for n in ns if n not in loop]
    ns = [n for n in ns if n not in curr_set]
    if len(ns) == 0:
        raise Exception('No neighbours for', curr)

    is_side1 = False
    is_side2 = False
    for n in ns:
        if n in side1:
            is_side1 = True
            break
        if n in side2:
            is_side2 = True
            break
    if is_side1 and is_side2:
        raise Exception('Dangling', curr, 'has neighbours in both sides')

    if is_side1:
        side1.update(curr_set)
    elif is_side2:
        side2.update(curr_set)
    else:
        dangling.append(curr_set + [ns[0]])

ins = set()
outs = set()
if (0, 0) in side1:
    ins = side2
    outs = side1
else:
    ins = side1
    outs = side2

print_map(lines, loop, ins, outs)

print("Part 2:", len(ins))

import sys
print(chr(27)+'[2j')
print('\033c')
from time import sleep
f = open('06.input', 'r')
#f = open('06.test', 'r')
lines = [x.strip() for x in f.readlines()]
RED = "\033[31m"
BLUE = "\033[34m"
RESET = "\033[0m"
LIGHT_BLUE_BG = "\033[104m"

DIRS = [
        (0, -1),
        (1, 0),
        (0, 1),
        (-1, 0),
]
dir_char = {
        '^': 0,
        '>': 1,
        'v': 2,
        '<': 3,
}
char_dir = ['^', '>', 'v', '<']

grid = {}
pos = None
delta = 0
for y, row in enumerate(lines):
    for x, col in enumerate(row):
        if col != '.' and col != '#':
            pos = (x,y)
            grid[(x,y)] = '.'
            delta = dir_char[col]
        else: 
            grid[(x,y)] = col

def print_map(grid, pos, delta, visited):
    for y, row in enumerate(lines):
        line = ''
        for x in range(len(row)):
            if (x,y) == pos:
                line += LIGHT_BLUE_BG + char_dir[delta] + RESET
            elif (x,y) in visited:
                line += RED + 'X'  + RESET
            else: 
                line += grid[(x,y)]
        print(line)


def solve(grid, pos: tuple[int,int], delta: int):

    visited = set()
    visited.add(pos)
    seen = set()
    is_looping = False
    while True:
        x,y = pos
        dx,dy = DIRS[delta]
        new_pos = (x+dx, y+dy)
        if (new_pos, delta) in seen:
            is_looping = True
            break
        seen.add((new_pos, delta))

        #if len(visited) % 30 == 0:
        #    sleep(0.1)
        #    print_map(grid,pos,delta,visited)

        if new_pos not in grid:
            break
        g = grid[new_pos]

        if g == '#':
            delta = (delta + 1) % 4
            continue
        pos = new_pos
        visited.add(new_pos)

    # print_map(grid,pos,delta,visited)
    return is_looping, visited

if delta is not None and pos is not None:
    print_map(grid, pos, delta, set())
    _, visited = solve(grid, pos,delta)
    print('Solution part 1:', len(visited))

    loopable = 0
    total = len(visited)

    for i, (x,y) in enumerate(visited):
        if grid[(x,y)] == '#':
            continue
        if (x,y) == pos:
            continue

        new_grid = grid.copy()
        new_grid[(x,y)] = '#'
        is_looping, result = solve(new_grid, pos,delta)
        if is_looping:
            loopable += 1

        if i % 100 == 0 or i == total - 1:
            progress = (i + 1) / total
            bar_length = 40  # Length of the progress bar
            filled_length = int(bar_length * progress)
            bar = '=' * filled_length + '-' * (bar_length - filled_length)
            sys.stdout.write(f'\rProgress: [{bar}] {progress:.1%} (Checked {i+1}/{total})')
            sys.stdout.flush()

    sys.stdout.write(f'\rSolution part 2: {loopable}' + ' ' * 60)
    sys.stdout.flush()
    print()

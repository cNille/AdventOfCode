print(chr(27)+'[2j')
print('\033c', end='')
lines = open('./22_day/my.input', 'r').read().split('\n')
lines = lines[:-1]

test = [
    '..#',
    '#..',
    '...',
]
# lines = test

middle = len(lines) // 2
grid = {}
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        grid[(x, y)] = c

initial_grid = grid.copy()
start = (middle, middle)


def print_grid(grid, current_position):
    min_x = min([x for x, _ in grid.keys()])
    max_x = max([x for x, _ in grid.keys()])
    min_y = min([y for _, y in grid.keys()])
    max_y = max([y for _, y in grid.keys()])
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x, y) == current_position:
                if grid[(x, y)] == '#':
                    print('X', end='')
                else:
                    print('x', end='')
            else:
                print(grid[(x, y)], end='')
        print()


directions = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0),
]

# Part 1
current_direction = 0
pos = start
infections = 0

for i in range(10000):
    if pos not in grid:
        grid[pos] = '.'

    if grid[pos] == '#':
        current_direction = (current_direction + 1) % 4
        grid[pos] = '.'
    else:
        current_direction = (current_direction - 1) % 4
        grid[pos] = '#'
        infections += 1

    pos = (pos[0] + directions[current_direction][0],
           pos[1] + directions[current_direction][1])

print("Solution part 1:", infections)

# Part 2
current_direction = 0
pos = start
infections = 0
grid = initial_grid.copy()

for i in range(10000000):
    if pos not in grid:
        grid[pos] = '.'

    if grid[pos] == '#':
        current_direction = (current_direction + 1) % 4
        grid[pos] = 'F'
    elif grid[pos] == '.':
        current_direction = (current_direction - 1) % 4
        grid[pos] = 'W'
    elif grid[pos] == 'W':
        grid[pos] = '#'
        infections += 1
    elif grid[pos] == 'F':
        current_direction = (current_direction + 2) % 4
        grid[pos] = '.'
    else:
        raise Exception("Unknown state")

    pos = (pos[0] + directions[current_direction][0],
           pos[1] + directions[current_direction][1])

print("Solution part 2:", infections)

print(chr(27)+'[2j')
print('\033c')
#f = open('18.input', 'r')
f = open('18.test', 'r')
lines = [x.strip() for x in f.readlines()]

start = (0, 0)
DIR = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}
E, S, W, N = DIR['E'], DIR['S'], DIR['W'], DIR['N']
D = [E, S, W, N]
min_x, min_y = 0, 0
max_x, max_y = 0, 0

pos = start
positions = {}
for l in lines:
    direction, steps, color = l.split(' ')
    color = color[1:-1]
    for i in range(int(steps)):
        pos = (pos[0] + DIR[direction][0], pos[1] + DIR[direction][1])
        min_x = min(min_x, pos[0])
        min_y = min(min_y, pos[1])
        max_x = max(max_x, pos[0])
        max_y = max(max_y, pos[1])

        positions[pos] = color

print_lines = []
for y in range(min_y, max_y + 1):
    line = ''
    prev_edge = None
    for x in range(min_x-2, max_x + 3):
        p = (x, y)
        if p in positions:
            line += '#'
            continue
        # Count how many edges we've crossed. To figure out if we're inside or
        # outside the polygon.
        left_edges, right_edges = 0,  0
        edges = 0
        edge_direction = None
        for i in range(min_x, x):
            if (i, y) in positions:
                neighbor_above = (i, y - 1) in positions
                neighbor_below = (i, y + 1) in positions
                neighbor_left = (i - 1, y) in positions
                if neighbor_above and neighbor_below:
                    edges += 1
                elif neighbor_above:
                    edges += 1 if edge_direction == 'D' else 0
                if neighbor_below:
                    edges += 1 if edge_direction == 'U' else 0
                if neighbor_above:
                    edge_direction = 'U'
                elif neighbor_below:
                    edge_direction = 'D'
            else:
                edge_direction = None
                #is_inside = False

        # Check if we're inside or outside the polygon.
        if edges % 2 == 1:
            line += 'O'
        else:
            line += '.'
    print_lines.append(line)

count = 0
for y, l in enumerate(print_lines):
    for x, ch in enumerate(l):
        if ch != '.':
            count += 1
    print(l)
print(count)

# 48488

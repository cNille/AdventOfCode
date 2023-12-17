print(chr(27)+'[2j')
print('\033c')
#f = open('16.input', 'r')
f = open('16.test', 'r')
lines = [x.strip() for x in f.readlines()]


def within_range(mtx, x, y):
    return x >= 0 and y >= 0 and x < len(mtx) and y < len(mtx[0])


def solve(mtx, start_pos, start_d):
    visited = set()
    tiles = set()
    queue = [(start_pos, start_d)]
    while queue:
        pos, d = queue.pop(0)
        x, y = pos
        if not within_range(mtx, x, y):
            continue
        if (pos, d) in visited:
            continue
        dx, dy = DIRS[d]
        visited.add((pos, d))
        tiles.add(pos)
        tile = mtx[y][x]

        new_d = []
        if tile == '/':
            new_d.append({0: 3, 1: 2, 2: 1, 3: 0}[d])
        elif tile == '|':
            if d == 0 or d == 2:
                new_d.append(1)
                new_d.append(3)
            else:
                new_d.append(d)
        elif tile == "-":
            if d == 1 or d == 3:
                new_d.append(0)
                new_d.append(2)
            else:
                new_d.append(d)
        elif tile == '.':
            new_d.append(d)
        else:
            new_d.append({0: 1, 1: 0, 2: 3, 3: 2}[d])

        for d in new_d:
            dx, dy = DIRS[d]
            nxt = (x+dx, y+dy)
            queue.append((nxt, d))
    return len(tiles)


def solve2(mtx):
    results = []
    for x in range(len(mtx[0])):
        # Top row
        y = 0
        results.append(solve(mtx, (x, y), 1))
        # Bottom row
        y = len(mtx) - 1
        results.append(solve(mtx, (x, y), 3))
    for y in range(len(mtx)):
        # Left column
        x = 0
        results.append(solve(mtx, (x, y), 0))
        # Right column
        x = len(mtx[0]) - 1
        results.append(solve(mtx, (x, y), 2))
    return max(results)


DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
mtx = lines
print('Part 1:', solve(mtx, (0, 0), 0))
print('Part 2:', solve2(mtx))

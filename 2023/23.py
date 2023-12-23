from heapq import heappush, heappop
print(chr(27)+'[2j')
print('\033c')
#f = open('23.input', 'r')
f = open('23.test', 'r')
lines = [x.strip() for x in f.readlines()]

start_pos = (0, 0)
end_pos = (0, 0)
mtx = [line for line in lines]
for x in range(len(mtx[0])):
    if mtx[0][x] == '.':
        start_pos = (x, 0)
    if mtx[-1][x] == '.':
        end_pos = (x, len(mtx) - 1)


def within_range(x, y, mtx):
    return x >= 0 and y >= 0 and x < len(mtx[0]) and y < len(mtx)


def solve1(mtx):
    longest_path = 0
    queue = []
    heappush(queue, (0, start_pos, set()))
    longest = set()
    slopes = {'>': (1, 0), '<': (-1, 0), '^': (0, -1), 'v': (0, 1)}
    while len(queue) > 0:
        steps, pos, visited = heappop(queue)

        if pos == end_pos and len(visited) > longest_path:
            longest_path = max(longest_path, len(visited))
            longest = visited
            continue

        if pos in visited:
            continue
        visited.add(pos)
        x, y = pos
        if mtx[y][x] == '#':
            continue
        if mtx[y][x] == '.':
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if within_range(nx, ny, mtx) and mtx[ny][nx] != '#':
                    heappush(queue, (steps - 1, (nx, ny), visited.copy()))
        if mtx[y][x] in slopes:
            dx, dy = slopes[mtx[y][x]]
            nx, ny = x + dx, y + dy
            if within_range(nx, ny, mtx) and mtx[ny][nx] != '#':
                heappush(queue, (steps - 1, (nx, ny), visited))
    return longest_path, longest


def calc_turns(mtx):
    turns = set()
    turns.add(start_pos)
    turns.add(end_pos)
    for y, line in enumerate(mtx):
        for x, c in enumerate(line):
            if c == '#':
                continue
            neighbors = []
            for dx in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                nx = x + dx[0]
                ny = y + dx[1]
                if within_range(nx, ny, mtx) and mtx[ny][nx] != '#':
                    neighbors.append((nx, ny))
            if len(neighbors) > 2:
                turns.add((x, y))
    return turns


def solve2(mtx):
    turns = calc_turns(mtx)
    turn_distances = {}
    for turn in turns:
        turn_distances[turn] = {}
        queue = []
        heappush(queue, (0, turn, set()))
        while len(queue) > 0:
            steps, pos, visited = heappop(queue)
            if pos in turns and pos != turn:
                turn_distances[turn][pos] = steps
                continue
            if pos in visited:
                continue
            visited.add(pos)
            for dx in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                nx = pos[0] + dx[0]
                ny = pos[1] + dx[1]
                if within_range(nx, ny, mtx) and mtx[ny][nx] != '#':
                    heappush(queue, (steps + 1, (nx, ny), visited.copy()))

    longest_path = 0
    queue = []
    heappush(queue, (0, start_pos, set()))
    longest = set()
    slopes = {'>': (1, 0), '<': (-1, 0), '^': (0, -1), 'v': (0, 1)}
    while len(queue) > 0:
        steps, pos, visited = heappop(queue)
        visited.add(pos)
        if pos == end_pos:
            steps = 0 - steps
            if steps > longest_path:
                longest_path = max(longest_path, steps)
                longest = visited
            continue
        x, y = pos
        if mtx[y][x] == '.' or mtx[y][x] in slopes:
            for tx, ty in turn_distances[pos]:
                if (tx, ty) in visited:
                    continue
                if mtx[ty][tx] == '#':
                    continue
                new_steps = steps - turn_distances[pos][(tx, ty)]
                heappush(queue, (new_steps, (tx, ty), visited.copy()))
    return longest_path, longest


longest_path, longest = solve1(mtx)
print('Part 1: {}'.format(longest_path))

longest_path, longest = solve2(mtx)
print('Part 2: {}'.format(longest_path))

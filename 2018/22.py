# Import data
DATA = [line.strip() for line in open('22.in', 'r').readlines()]

DEPTH = int(DATA[0].split(' ')[1])
TARGET = map(int, DATA[1].split(' ')[1].split(','))

# Test data
if False:
    DEPTH = 510
    TARGET = (10, 10)


# Calculate Geological index
def geo_calc(mtx, x, y):
    if x == 0 and y == 0:
        return 0
    elif x == 0:
        return y * 48271
    elif y == 0:
        return x * 16807
    return mtx[y - 1][x] * mtx[y][x - 1]


def part1():
    cave = []
    geo = []
    ero = []
    tx, ty = TARGET
    for y in range((ty + 1) * 3):
        geo.append([])
        ero.append([])
        cave.append('')
        for x in range((tx + 1) * 20):
            geological_index = geo_calc(ero, x, y)
            geo[-1].append(geological_index)

            erosion = (geological_index + DEPTH) % 20183
            ero[-1].append(erosion)

            region = erosion % 3
            if x == 0 and y == 0:
                cave[-1] += 'M'
            elif x == tx and y == ty:
                cave[-1] += 'T'
            else:
                cave[-1] += ['.', '=', '|'][region]

    risklevel = 0
    for line in cave[:ty + 1]:
        for ch in line[:tx + 1]:
            if ch in '\nMT':
                continue

            risklevel += ['.', '=', '|'].index(ch)

    print 'Part 1 solution: %d' % risklevel
    return cave


CAVE = part1()


class Graph(object):
    def __init__(self, t):
        tx, ty = t
        self.points = []
        for _ in range(ty * 3):
            self.points.append([])
            for _ in range(tx * 10):
                self.points[-1].append([99999, 99999, 999999])
        self.nodes = []
        self.target = t

    def __len__(self):
        return len(self.nodes)

    def add(self, x, y, equipment, d, path):
        if x >= len(self.points[0]):
            return
        if d >= self.points[y][x][equipment]:
            return

        tx, ty = self.target
        heuristic = abs(x - tx) + abs(y - ty)
        cost = int(heuristic + d)

        node = (x, y, equipment, d, cost, path + [(x, y)])
        self.points[y][x][equipment] = d

        # Add node in sorted manner, lowest cost first.
        for i in range(len(self.nodes)):
            if cost <= self.nodes[i][4]:
                self.nodes.insert(i, node)
                break
        else:
            self.nodes.append(node)

    def next(self):
        return self.nodes.pop(0)


def part2(cave):
    possible_equipment = {
        '.': [0, 1],  # torch, gear
        '=': [1, 2],  # gear, neither
        '|': [0, 2],  # torch, neither
        'T': [0, 1],  # Always rocky
        'M': [0, 1],  # Always rocky
    }
    graph = Graph(TARGET)
    graph.add(0, 0, 0, 0, [])

    count = 0
    while True:
        node = graph.next()
        x, y, e, d, c, p = node

        if count % 10000 == 0:
            print('X: %d, Y: %d, E: %d, D: %d, C: %d, Len: %d' %
                  (x, y, e, d, c, len(graph)))
        if x == TARGET[0] and y == TARGET[1]:
            plus = '+0' if e == 0 else '+7'
            print('FOUND AT NODE:', node[:-1], plus)

        neighbours = [
            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1),
        ]

        for (nx, ny) in [n for n in neighbours if n not in p]:
            if nx < 0 or ny < 0:
                continue
            new_region = cave[ny][nx]
            if e in possible_equipment[new_region]:
                for new_e in possible_equipment[new_region]:
                    delta_cost = 1 if e == new_e else 8
                    graph.add(nx, ny, new_e, d + delta_cost, p)
        count += 1
        if count > 500000:
            exit()


part2(CAVE)

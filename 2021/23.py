from collections import deque
import sys
import heapq
sys.setrecursionlimit(10000)
print(chr(27)+'[2j')
print('\033c')
f = open('23.input', 'r')
f = open('23.test', 'r')
data = [x[:-1] for x in f.readlines()]
burrow = [
    (x.replace('A', '.')
        .replace('B', '.')
        .replace('C', '.')
        .replace('D', '.'))
    for x 
    in data
]

def to_str(amphis):
    amphis.sort(key = lambda x: 100 * ord(x[0]) + 10 * x[1][0] + x[1][1])
    return '_'.join([x[0] + ":" + ','.join(map(str, x[1])) for x in amphis])

find = [
    [
        ('A', (9,3)),
        ('A', (3,3)),
        ('B', (4,1)),
        ('B', (3,2)),
        ('C', (5,2)),
        ('C', (7,3)),
        ('D', (9,2)),
        ('D', (5,3)),
    ],
    [
        ('A', (9,3)),
        ('A', (3,3)),
        ('B', (4,1)),
        ('B', (3,2)),
        ('C', (7,2)),
        ('C', (7,3)),
        ('D', (9,2)),
        ('D', (5,3)),
    ],
    [
        ('A', (9,3)),
        ('A', (3,3)),
        ('B', (4,1)),
        ('B', (3,2)),
        ('C', (7,2)),
        ('C', (7,3)),
        ('D', (9,2)),
        ('D', (6,1)),
    ],
    [
        ('A', (9,3)),
        ('A', (3,3)),
        ('B', (5,3)),
        ('B', (3,2)),
        ('C', (7,2)),
        ('C', (7,3)),
        ('D', (9,2)),
        ('D', (6,1)),
    ],
    [
        ('A', (9,3)),
        ('A', (3,3)),
        ('B', (5,3)),
        ('B', (5,2)),
        ('C', (7,2)),
        ('C', (7,3)),
        ('D', (8,1)),
        ('D', (6,1)),
    ],
    [
        ('A', (10,1)),
        ('A', (3,3)),
        ('B', (5,3)),
        ('B', (5,2)),
        ('C', (7,2)),
        ('C', (7,3)),
        ('D', (8,1)),
        ('D', (6,1)),
    ],
    [
        ('A', (10,1)),
        ('A', (3,3)),
        ('B', (5,3)),
        ('B', (5,2)),
        ('C', (7,2)),
        ('C', (7,3)),
        ('D', (9,3)),
        ('D', (6,1)),
    ],
    [
        ('A', (10,1)),
        ('A', (3,3)),
        ('B', (5,3)),
        ('B', (5,2)),
        ('C', (7,2)),
        ('C', (7,3)),
        ('D', (9,3)),
        ('D', (9,2)),
    ],
    [
        ('A', (3,2)),
        ('A', (3,3)),
        ('B', (5,3)),
        ('B', (5,2)),
        ('C', (7,2)),
        ('C', (7,3)),
        ('D', (9,3)),
        ('D', (9,2)),
    ],
]
find_id = [to_str(x) for x in find]

# Get startpositions
amphis = []
for i, line in enumerate(data):
    for j, ch in enumerate(line):
        if ch in ['A','B','C','D']:
            amphis.append((ch, (j,i)))

spaces = set()
for y, line in enumerate(burrow):
    for x, ch in enumerate(line):
        if burrow[y][x] == '.':
            spaces.add((x,y))

def delta(pos1,pos2):
    return abs(pos2[1] - pos1[1]) + abs(pos2[0] - pos1[0])

def get_neighbours(spaces, x,y):
    return [
        (nx,ny)
        for (nx,ny)
        in [
            (x - 1, y),
            (x + 1, y),
            (x, y - 1),
            (x, y + 1),
        ] if (nx,ny) in spaces
    ]

def get_path(spaces, current, end, visited):
    if current == end:
        return [current]
    neigbours = get_neighbours(spaces, current[0], current[1])
    paths = [
        get_path(spaces, n, end, visited + [current])
        for n in neigbours
        if n not in visited
    ]
    paths = [p for p in paths if p is not None]
    if len(paths) == 0:
        return None 
    paths.sort(key = lambda x: len(x))
    return  [current] + paths[0] 

connections = {}
spaces = sorted(spaces, key = lambda x: x[1])
for start in spaces:
    connections[start] = {}
    for end in spaces:
        if start == end:
            continue
        path = get_path(spaces, start, end, [])
        connections[start][end] = path[1:]


valid_cache = {}
def is_valid_burrow(amphis, id):
    if id in valid_cache:
        return valid_cache[id]
    valid_cache[id] = False
    for amphi in amphis:
        name, pos = amphi
        if name == 'A' and pos not in [(3,2), (3,3)]:
            return False
        if name == 'B' and pos not in [(5,2), (5,3)]:
            return False
        if name == 'C' and pos not in [(7,2), (7,3)]:
            return False
        if name == 'D' and pos not in [(9,2), (9,3)]:
            return False
    valid_cache[id] = True
    return True

def get_cost(amphi, steps):
    if amphi == 'A':
        return steps * 1
    if amphi == 'B':
        return steps * 10
    if amphi == 'C':
        return steps * 100
    if amphi == 'D':
        return steps * 1000

heur_cache = {}
def get_heuristic(amphis, id):
    if id in heur_cache:
        return heur_cache[id]
    heuristic = 0
    goals = {
        'A': [(3,3),(3,2)],
        'B': [(5,3),(5,2)],
        'C': [(7,3),(7,2)],
        'D': [(9,3),(9,2)]
    }
    costs = {
        'A': 1,
        'B': 10,
        'C': 100,
        'D': 1000,
    }
    for amphi in amphis:
        name, pos = amphi
        if pos in goals[name]:
            goals[name] = [x for x in goals[name] if x != pos]
            continue
        goal = goals[name][0]

        path = connections[pos][goal]
        left = len(path) * costs[name]
        left += 2000 if pos[1] == 1 else 0
        for other in amphis:
            if other[1] != pos and other[1] in path:
                left += costs[other[0]] * 3
        heuristic += left 

    heur_cache[id] = heuristic
    return heuristic * 2

def get_all_possible_steps(amphis, visited):
    h, current_cost, positions, steps, curr_id = amphis

    possible_steps = []
    blocked_spaces = set([a[1] for a in positions])
    goals = { 'A': 3, 'B': 5, 'C': 7, 'D': 9 }
    rooms_done = { 'A': 0, 'B': 0, 'C': 0, 'D': 0 }
    for i, amphi_pos in enumerate(positions):
        amphi, pos = amphi_pos
        if pos[0] == goals[amphi]:
            rooms_done[amphi] += 1

    for i, amphi_pos in enumerate(positions):
        amphi, pos = amphi_pos
        goal = goals[amphi]
        if pos[1] == 3 and ((pos[0], 2) in blocked_spaces):
            continue

        if rooms_done[amphi] >= 2:
            continue
        for end in spaces:
            if end in [(3,1), (5,1), (7,1), (9,1)]: 
                continue
            if pos == end: 
                continue
            if pos[1] == 1:
                if end[0] != goal:
                    continue
                intruder = False
                for amphi_pos2 in positions:
                    amphi2, pos2 = amphi_pos2
                    if amphi2 == amphi:
                        continue
                    if pos2[0] == goal:
                        intruder = True
                        break
                if intruder:
                    continue
            
            path = connections[pos][end]
            valid_path = len(set(path).intersection(blocked_spaces)) == 0
            if not valid_path:
                continue
            new_positions = positions.copy()
            new_positions[i] = (amphi, end)
            id = to_str(new_positions)
            if id in visited:
                continue
            cost = current_cost + get_cost(amphi, len(path))
            possible_steps.append((
                cost + get_heuristic(new_positions, id) + steps * 2000, 
                cost, 
                new_positions,
                steps + 1,
                id 
            ))


    # print('Possible steps %d' % len(possible_steps))
    # for p in possible_steps:
    #     print(p)
    # exit()

    return possible_steps

amphis = find[0] 
amphis = find[-3] 
id = to_str(amphis)
least_cost = 99999991239
start_amphis = (0, 0, amphis, 0, id)
visited = set(id)


id_cache = {}
count = 0
def get_shortest_path(positions, visited, least_cost):
    global count
    heur, current_cost, amphi_positions , step, curr_id = positions
    if curr_id in id_cache:
        return id_cache[curr_id]
    if is_valid_burrow(amphi_positions, curr_id):
        return 0
    if count % 1000 == 0:
        print(count, 'Checking %s with steps %d' % (curr_id, step))
    count += 1

    possibilities = get_all_possible_steps(positions, visited)
    possibilities.sort(key  = lambda x: x[0])
    
    if curr_id in find_id:
        p_ids = [x[4] for x in possibilities]
        if find_id in p_ids:
            print(curr_id)
            print(p_ids)
            print("ABORT")
            exit()
    for i, next_amphi in enumerate(possibilities):
        heuristic, cost, next_positions, steps, id = next_amphi
        if id in find_id:
            nbr = find_id.index(id)
            print('Second step', nbr, i)

    this_least_cost = least_cost
    for next_amphi in possibilities:
        heuristic, cost, next_positions, steps, id = next_amphi
        if cost > this_least_cost or id in visited or id in id_cache:
            continue
        next_cost = get_shortest_path(next_amphi, visited.union(set([id])), this_least_cost)
        new_cost = next_cost
        if new_cost < this_least_cost:
            print('Update leastcost', cost, next_cost, this_least_cost, step)
            this_least_cost = new_cost + cost
            print('after leastcost',  this_least_cost, step)

    id_cache[curr_id] = current_cost + this_least_cost
    print('return', current_cost , this_least_cost, this_least_cost, step)
    return  this_least_cost

result = get_shortest_path(start_amphis, visited, least_cost)
print('shortest path:', result)



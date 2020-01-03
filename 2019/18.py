class Navigator:
    def __init__(self, x,y, steps, keysleft, keyname):
        self.x = x
        self.y = y
        self.steps = steps
        self.keysleft = keysleft
        self.keyname = keyname

def get_vault_data(vault):
    doors = {}
    locks = {}
    lock_pos = {}
    lock_keys = ""
    pos = []
    for y, row in enumerate(vault):
        for x, c in enumerate(row):
            if c == "@":
                pos.append((x,y))
            if c.isupper():
                doors[c] = (x,y)
            if c.islower():
                locks[(x,y)] = c 
                lock_pos[c] = (x,y)
                lock_keys += c
    return doors, locks, lock_pos, lock_keys, pos

def getNextNonWall(vault,x,y,path, dep=""):
    directions = [ (1,0), (-1,0), (0,-1), (0,1) ]
    next_steps = [] 
    return [
        (x+dx, y+dy, vault[y+dy][x+dx], dep)
        for dx, dy in directions
        if (
            vault[y+dy][x+dx] != '#'       # isEmpty spot
        ) and (x+dx, y+dy) not in path     # not already visited
    ]

def getDependencies(vault, x, y, locks):
    steps = 1
    path = [(x,y)]
    dep = {}
    nextSteps = getNextNonWall(vault,x,y,path, "@")
    while len(nextSteps) > 0:
        newSteps = []
        for a,b,c,d in nextSteps:
            if c.isupper():
                d += c
            if c.islower():
                dep[c] = d
            path.append((a,b))
            newSteps += list(set(getNextNonWall(vault,a,b,path, d)))
        nextSteps = newSteps
        steps += 1
    return dep

def getDistances(vault, x, y, locks):
    steps = 1
    path = []
    dist = {}
    nextSteps = getNextNonWall(vault,x,y,path, "@")
    while len(nextSteps) > 0:
        newSteps = []
        for a,b,c,d in nextSteps:
            if c.islower():
                dist[c] = steps
            path.append((a,b))
            newSteps += list(set(getNextNonWall(vault,a,b,path)))
        nextSteps = newSteps
        steps += 1
    return dist

# ===================================
# ===================================
# Part 1

def get_positions(nav):
    return tuple(nav.x + nav.y)

def find_shortest_path(nav, level, dependencies, distances, lock_pos):
    keysleft = nav.keysleft
    sorted_keys = tuple(sorted(keysleft))
    if (get_positions(nav), sorted_keys) in cache:
        return cache[(get_positions(nav), sorted_keys)]

    shortest = 9999
    keysleft = [k for k in keysleft]
    for key in keysleft:
        
        blocking_doors = [x for x in dependencies[key] if x.lower() in sorted_keys]
        if len(blocking_doors) > 0:
            continue

        distance = None
        curr_i = None
        for i in range(len(nav.x)):
            x,y = nav.x[i], nav.y[i]

            if (x,y) in distances and key in distances[(x,y)]:
                distance = distances[(x,y)][key]
                curr_i = i
                break

        left = [x for x in keysleft if x != key]
        lx,ly = lock_pos[key]
        next_nav = Navigator(
            (nav.x[:curr_i] + [lx] + nav.x[curr_i+1:]), 
            (nav.y[:curr_i] + [ly] + nav.y[curr_i+1:]), 
            distance, 
            left, 
            key
        )
        if len(left) == 0:
            d = distance
            next_key = ''
        else:
            path_distance = find_shortest_path(next_nav, level+1, dependencies, distances, lock_pos)
            d = distance + path_distance 
        if d < shortest:
            shortest = d
            curr_key = key

    cache[(get_positions(nav), sorted_keys)] = shortest
    return shortest

vault = [x.strip() for x in open('18.input', 'r').readlines()]
def part1(vault):
    doors, locks, lock_pos, lock_keys, pos = get_vault_data(vault)
    pos = pos[0]

    distances = {}
    for (lx,ly) in locks:
        distances[(lx,ly)] = getDistances(vault, lx,ly, locks)
    x,y = pos
    distances[(x,y)] = getDistances(vault, x,y,locks)

    dependencies = getDependencies(vault, x,y, locks)
    cache = {}

    navigator = Navigator([x],[y], 0, lock_keys, "@")
    print "Part 1:", find_shortest_path(navigator, 0, dependencies, distances, lock_pos)
cache = {}
part1(vault)

# ===================================
# ===================================

# Part 2
vault = [x.strip() for x in open('18.input_part2', 'r').readlines()]

def part2(vault):
    doors, locks, lock_pos, lock_keys, pos = get_vault_data(vault)

    distances = {}
    for (lx,ly) in locks:
        distances[(lx,ly)] = getDistances(vault, lx,ly, locks)

    dependencies = {}
    for x,y in pos:
        distances[(x,y)] = getDistances(vault, x, y,locks)
        dep = getDependencies(vault, x, y, locks)

        for d in dep:
            assert d not in dependencies
            dependencies[d] = dep[d]

    xs = [x for x,y in pos]
    ys = [y for x,y in pos]
    lock_keys = [k for k in lock_keys]
    
    navigator = Navigator(xs, ys, 0, lock_keys, "@")
    print "Part 2:", find_shortest_path(navigator, 0, dependencies, distances, lock_pos)
cache = {}
part2(vault)

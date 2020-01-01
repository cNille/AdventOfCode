data = [x[:-1] for x in open('20.input', 'r').readlines()]

i = 0
for c in data:
    print(i, c, len(c))
    i +=1 

# inner outer are the offset when the donut starts and ends
i = 0
while data[i][i] != "#":
    i += 1
outer = i
while data[i][i] != " ":
    i += 1
inner = i - 1

def add(entries, name, x,y):
    if name not in entries:
        entries[name] = []
    entries[name].append((x,y))
    return entries

def getEntries():
    entries = {}
    # =============
    # Outer ring
    right = len(data[0]) - outer-1
    outer_max = len(data) - outer
    for X in range(outer,outer_max):
        if data[X][outer] == ".": # Left
            A,B = data[X][outer-2], data[X][outer-1]
            entries = add(entries, A+B, outer,X)
        if data[X][right] == ".": # Right
            A,B = data[X][right+1], data[X][right+2]
            entries = add(entries, A+B, right,X)

    outer_max = len(data[outer]) - outer
    down = len(data) - outer - 1
    for X in range(outer,outer_max):
        if data[outer][X] == ".": # Up
            A,B = data[outer-2][X], data[outer-1][X]
            entries = add(entries, A+B, X, outer)
        if data[down][X] == ".": # Down
            A,B = data[down+1][X], data[down+2][X]
            entries = add(entries, A+B, X, down)
    # =============
    # Inner ring
    right = len(data[0]) - inner-1
    inner_max = len(data) - inner
    for X in range(inner,inner_max):
        if data[X][inner] == ".": # Left
            A,B = data[X][inner+1], data[X][inner+2]
            entries = add(entries, A+B, inner, X)
        if data[X][right] == ".": # Right
            A,B = data[X][right-2], data[X][right-1]
            entries = add(entries, A+B, right, X)

    inner_max = len(data[inner]) - inner
    down = len(data) - inner - 1
    for X in range(inner,inner_max):
        if data[inner][X] == ".": # Up
            A,B = data[inner+1][X], data[inner+2][X]
            entries = add(entries, A+B, X, inner)
        if data[down][X] == ".": # Down
            A,B = data[down-2][X], data[down-1][X]
            entries = add(entries, A+B, X, down)
    return entries

entries = getEntries()

entry_positions = {}
for entry in entries:
    for pos in entries[entry]:
        entry_positions[pos] = entry


def getNextNonWall(vault,x,y,path):
    directions = [ (1,0), (-1,0), (0,-1), (0,1) ]
    next_steps = [] 
    return [
        (x+dx, y+dy, vault[y+dy][x+dx])
        for dx, dy in directions
        if (
            vault[y+dy][x+dx] == '.'       # isEmpty spot
        ) and (x+dx, y+dy) not in path     # not already visited
    ]

def getDistances(entries, x, y):
    steps = 2
    path = [(x,y)]
    dist = {}
    nextSteps = getNextNonWall(vault,x,y,path)
    while len(nextSteps) > 0:
        newSteps = []
        for a,b,c in nextSteps:
            if (a,b) in entry_positions: 
                dist[entry_positions[(a,b)]] = steps
            path.append((a,b))
            newSteps += list(set(getNextNonWall(vault,a,b,path)))
        nextSteps = newSteps
        steps += 1
    return dist

vault = data
distances = {}
for x,y in entry_positions:
    portal = entry_positions[(x,y)]
    dist = getDistances(entries, x, y)

    if portal not in distances:
        distances[portal] = {}
    for d in dist:
        distances[portal][d] = dist[d]

        if d not in distances:
            distances[d] = {}
        distances[d][portal] = dist[d]
print '-'*80
for d in distances:
    print d, distances[d]
print '-'*80


def calculate(distances, path, traveled):
    prev = path[-1]
    possible = distances[prev].keys() 
    shortest = 999999999
    for next_portal in [p for p in possible if p not in path]:
        if next_portal == "ZZ":
            res = traveled + distances[prev][next_portal]
            shortest = min(res, shortest)
            break
        curr = calculate(distances, path + [next_portal], traveled + distances[prev][next_portal])
        shortest = min(shortest, curr)
    return shortest

res = calculate(distances, ["AA"], 0)
res = res - 1 # For skipping first move from AA

print "Part 1: %d " % res

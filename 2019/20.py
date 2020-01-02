data = [x[:-1] for x in open('20a.input', 'r').readlines()]
data = [x[:-1] for x in open('20b.input', 'r').readlines()]
data = [x[:-1] for x in open('20.input', 'r').readlines()]


# inner outer are the offset when the donut starts and ends
i = 0
while data[i][i] != "#":
    i += 1
outer = i
while data[i][i] != " ":
    i += 1
inner = i - 1

def add(entries, name, x,y, inner):
    if inner:
        name = name+"_inner"
    else:
        name = name+"_outer"
    if name not in entries:
        entries[name] = []
    entries[name] = (x,y)
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
            entries = add(entries, A+B, outer,X, False)
        if data[X][right] == ".": # Right
            A,B = data[X][right+1], data[X][right+2]
            entries = add(entries, A+B, right,X, False)

    outer_max = len(data[outer]) - outer
    down = len(data) - outer - 1
    for X in range(outer,outer_max):
        if data[outer][X] == ".": # Up
            A,B = data[outer-2][X], data[outer-1][X]
            entries = add(entries, A+B, X, outer, False)
        if data[down][X] == ".": # Down
            A,B = data[down+1][X], data[down+2][X]
            entries = add(entries, A+B, X, down, False)

    # =============
    # Inner ring
    right = len(data[0]) - inner-1
    inner_max = len(data) - inner
    for X in range(inner,inner_max):
        if data[X][inner] == ".": # Left
            A,B = data[X][inner+1], data[X][inner+2]
            entries = add(entries, A+B, inner, X, True)
        if data[X][right] == ".": # Right
            A,B = data[X][right-2], data[X][right-1]
            entries = add(entries, A+B, right, X, True)

    inner_max = len(data[inner]) - inner
    down = len(data) - inner - 1
    for X in range(inner,inner_max):
        if data[inner][X] == ".": # Up
            A,B = data[inner+1][X], data[inner+2][X]
            entries = add(entries, A+B, X, inner, True)
        if data[down][X] == ".": # Down
            A,B = data[down-2][X], data[down-1][X]
            entries = add(entries, A+B, X, down, True)
    return entries

entries = getEntries()

entry_positions = {}
for entry in entries:
    entry_positions[entries[entry]] = entry

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

def calculate_part1(distances, path, traveled):
    prev = path[-1]
    prev = prev[:2] + ("_outer" if "inner" in prev else "_inner")
    possible = distances[prev].keys() 
    shortest = 999999999
    for next_portal in [p for p in possible if p not in path]:
        #if next_portal == "ZZ_outer":
        if "AA" in next_portal:
            continue
        if "ZZ" in next_portal:
            res = traveled + distances[prev][next_portal]
            shortest = min(res, shortest)
            break

        d = distances[prev][next_portal]
        curr = calculate_part1(distances, path + [next_portal], traveled + d)
        shortest = min(shortest, curr)
    return shortest

res = calculate_part1(distances, ["AA_inner"], 0)
res = res - 1 # For skipping first move from AA

print "Part 1: %d " % res


from collections import deque
def calculate_part2(distances):
    shortest = 999999999
    q = deque()
    q.append((["AA_inner"], 0, 0))

    while len(q) > 0:
        path, traveled, z = q.popleft()
        if traveled > shortest or z > 0:
            continue
        prev = path[-1]
        prev = prev[:2] + ("_outer" if "inner" in prev else "_inner")

        if prev not in distances:
            continue
        possible = distances[prev].keys() 

        for next_portal in possible:
            if z != 0 and ("AA" in next_portal or "ZZ" in next_portal):
                continue
            d = distances[prev][next_portal]
            if z == 0 and "ZZ" in next_portal :
                shortest = min(traveled+d, shortest)
                continue
            new_path = path + [next_portal]
            new_traveled = traveled + d 
            new_z = z + (-1 if "inner" in next_portal else 1)
            
            q.append((new_path, new_traveled, new_z))
    return shortest

res = calculate_part2(distances)
res = res - 1 # For skipping first move from AA
print "Part 2: %d" % res

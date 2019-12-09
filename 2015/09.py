routes = [x.strip() for x in open('09.input', 'r').readlines()]

paths = {}
for route in routes:
    src, to, dest, eq, dist = route.split(' ') 
    if src not in paths:
        paths[src] = []
    if dest not in paths:
        paths[dest] = []
    paths[src].append((dest, dist))
    paths[dest].append((src, dist))

def create_paths(path):
    last = path[-1]
    if last[0] not in paths:
        return [path]

    new_paths = [path]
    nxt = paths[last[0]]
    for n in nxt:
        if n[0] not in [pp[0] for pp in path]:
            new_p =  create_paths(path + [n])
            new_paths +=  new_p

    return new_paths


nbr_cities = len(paths.keys())
shortest = 9999
longest = 0
for path in paths:
    x = [p for p in create_paths([(path, 0)]) if len(p) == nbr_cities ]

    for p in x:
        # print(" -> ".join([route[0] for route in p]))
        # print(" -> ".join([str(route[1]) for route in p]))
        distances = [route[1] for route in p]   
        distance = sum([int(d) for d in distances])
        # print("Dist %d" % distance)
        shortest = shortest if shortest < distance else distance
        longest = longest if longest > distance else distance

print("Part 1 solution: %d" % shortest)
print("Part 2 solution: %d" % longest)

# high: 474
# high: 719 

    



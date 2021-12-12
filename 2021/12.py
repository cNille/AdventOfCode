f = open('12.test2', 'r')
f = open('12.input', 'r')
f = open('12.test', 'r')
lines = [x.strip() for x in f.readlines()]

connections = {}
for line in lines:
    a,b = line.split('-')
    if a not in connections:
        connections[a] = []
    if b not in connections:
        connections[b] = []
    connections[a].append(b)
    connections[b].append(a)

def get_paths(node, visited, allow_double):
    if node == 'end':
        return (1, [['end']])

    double_been_made = not allow_double or node in visited
    if node.lower() == node:
        new_visited = [node] + visited
    else:
        new_visited = visited
    
    
    neighbours = connections[node]
    next_paths = 0
    new_paths = []
    for neighbour in neighbours:
        if not allow_double and node in visited or neighbour == 'start': 
            continue

        path, paths = get_paths(neighbour, new_visited, not double_been_made)
        next_paths += path
        for p in paths:
            new_paths.append([node] + p)
            
    return (next_paths, new_paths)

count, paths = get_paths('start', [], False)
# for idx, p in enumerate(paths):
#     print("%s" % (','.join(p)))
print('Solution part 1: %d' % count)

count, paths = get_paths('start', [], True)
# for idx, p in enumerate(paths):
#     print("%s" % (','.join(p)))
print('Solution part 2: %d' % count)


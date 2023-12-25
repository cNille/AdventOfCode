from itertools import combinations
from collections import Counter, deque

print(chr(27)+'[2j')
print('\033c')
f = open('25.test', 'r')
f = open('25.input', 'r')
lines = [x.strip() for x in f.readlines()]

graph = {}
for line in lines:
    src, dst = line.split(':')
    if src not in graph:
        graph[src] = []
    for d in dst.split():
        d = d.strip()
        if d not in graph:
            graph[d] = []
        graph[src].append(d)
        graph[d].append(src)


def search(graph, start, end):
    visited = set()
    visited.add(start)
    path = []
    queue = deque([(start, path)])
    while queue:
        node, path = queue.popleft()
        if node == end:
            return path
        for n in graph[node]:
            if n not in visited:
                visited.add(n)
                queue.append((n, path + [n]))
    return None


c = Counter([x for x in graph.keys()])
i = 0
for a, b in combinations(graph.keys(), 2):
    path = search(graph, a, b)
    if path:
        for p in path:
            c[p] += 1
        i += 1
        if i > 30000:
            break
a, b, c, d, e, f = c.most_common(6)

del graph[a[0]][graph[a[0]].index(b[0])]
del graph[b[0]][graph[b[0]].index(a[0])]
del graph[c[0]][graph[c[0]].index(d[0])]
del graph[d[0]][graph[d[0]].index(c[0])]
del graph[e[0]][graph[e[0]].index(f[0])]
del graph[f[0]][graph[f[0]].index(e[0])]


def group_size(graph, start):
    visited = set()
    visited.add(start)
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for n in graph[node]:
            if n not in visited:
                visited.add(n)
                queue.append(n)
    return len(visited)


A = group_size(graph, a[0])
B = group_size(graph, b[0])

print('Most common:', a, b, c, d, e, f)
print('Group sizes:', A, B)
print('Part 1:', A * B)

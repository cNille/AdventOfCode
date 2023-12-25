import graphviz
from collections import deque

# print(chr(27)+'[2j')
# print('\033c')
f = open('25.test', 'r')
f = open('25.input', 'r')
lines = [x.strip() for x in f.readlines()]

dot = graphviz.Digraph('aoc-25', comment='Advent of Code day 25', format='svg')

graph = {}

# Manually investigated the graph to find
# which edges combine the groups. Add those to banlist.

banlist = [
    ('dsr', 'xzn'),
    ('qqh', 'xbl'),
    ('tbq', 'qfj'),
    # Test
    #('cmg', 'bvb'),
    #('hfx', 'pzl'),
    #('jqt', 'nvd'),
]

for line in lines:
    src, dst = line.split(':')
    if src not in graph:
        graph[src] = []
        dot.node(src, src)
    for d in dst.split():
        d = d.strip()
        if d not in graph:
            graph[d] = []
            dot.node(d, d)
        if (src, d) not in banlist and (d, src) not in banlist:
            graph[src].append(d)
            graph[d].append(src)
            dot.edge(src, d)

# print(dot.source)
dot.render('output', format='svg', cleanup=True)


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


# Choose a node to start with in each group.
# Choose for example each node of a removed edge

# Test
#a = group_size(graph, 'cmg')
#b = group_size(graph, 'bvb')
#print(a, b, a*b)

a = group_size(graph, 'dsr')
b = group_size(graph, 'xzn')
print(a, b, a*b)

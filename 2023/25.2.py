import networkx as nx

f = open('25.input', 'r')
lines = [x.strip() for x in f.readlines()]


graph = nx.Graph()

for line in lines:
    src, dst = line.split(':')
    for d in dst.strip().split():
        graph.add_edge(src, d)

edges = nx.minimum_edge_cut(graph)
print('Edges to remove:', edges)
graph.remove_edges_from(edges)

tot = 1
for g in nx.connected_components(graph):
    tot *= len(g)
print('Total:', tot)

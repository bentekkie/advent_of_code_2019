from collections import defaultdict
from igraph import Graph
import igraph as ig

lines = [tuple(l.strip().split(')')) for l in open("i","r")]
nodes = {x for line in lines for x in line}
g = Graph(directed=False)
g.add_vertices(list(nodes))
g.add_edges(lines)
start = g.neighbors("YOU")[0]
end = g.neighbors("SAN")[0]

print(g.shortest_paths(g.neighbors("YOU")[0],g.neighbors("SAN")[0]))



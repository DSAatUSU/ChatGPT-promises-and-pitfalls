import networkx
import random

# generate a random graph
g = networkx.fast_gnp_random_graph(50, .04)

for edge in g.edges(data=True):
    edge[2]['weight'] = random.randint(0,10)

try:
    path = networkx.dijkstra_path(g, 0, 49)
except: 
    print("There is no path from node 0 to node 49")
    exit(1)

print(path)

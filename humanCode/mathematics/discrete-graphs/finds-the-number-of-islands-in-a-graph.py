import networkx

# generate a random graph
g = networkx.fast_gnp_random_graph(50, .06)

components = sorted(networkx.connected_components(g), key=len)
print(len(components))

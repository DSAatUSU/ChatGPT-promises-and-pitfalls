import networkx

g = networkx.fast_gnp_random_graph(10, .3)

try:
    ham = networkx.approximation.traveling_salesman_problem(g)
except:
    print("The graph is not hamiltonian")
    exit(1)

print("This graph is hamiltonian")

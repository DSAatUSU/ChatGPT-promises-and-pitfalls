import networkx as nx

def find_largest_cycle(graph):
    """
    Finds the largest cycle in a graph.

    Args:
        graph: A NetworkX graph object.

    Returns:
        A list of nodes representing the largest cycle found.
    """
    largest_cycle = []
    cycles = nx.simple_cycles(graph)
    for cycle in cycles:
        if len(cycle) > len(largest_cycle):
            largest_cycle = cycle
    return largest_cycle

if __name__ == '__main__':
    # Create a graph
    graph = nx.DiGraph()
    
    # Add nodes
    graph.add_nodes_from([1, 2, 3, 4, 5, 6, 7])
    
    # Add edges
    graph.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1), (3, 7)])
    
    # Find the largest cycle
    largest_cycle = find_largest_cycle(graph)
    print("Largest Cycle:", largest_cycle)

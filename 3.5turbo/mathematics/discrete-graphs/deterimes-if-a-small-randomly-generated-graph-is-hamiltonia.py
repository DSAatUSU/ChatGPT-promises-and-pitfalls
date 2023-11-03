# Import necessary libraries
import networkx as nx
import random

# Function to check if a graph is Hamiltonian
def is_hamiltonian(graph):
    # Get all possible Hamiltonian cycles in the graph
    hamiltonian_cycles = list(nx.hamiltonian_cycles(graph))
    if len(hamiltonian_cycles) > 0:  # If there exists a Hamiltonian cycle
        return True
    else:
        return False

# Generate a small random graph
num_nodes = random.randint(3, 6)  # Random number of nodes between 3 and 6
graph = nx.gnm_random_graph(num_nodes, random.randint(num_nodes, num_nodes*(num_nodes-1)//2))

# Check if the graph is Hamiltonian
is_ham = is_hamiltonian(graph)

# Print the graph and the result
print("Generated Graph: ")
print(nx.adjacency_matrix(graph))
print("Is Hamiltonian: ", is_ham)

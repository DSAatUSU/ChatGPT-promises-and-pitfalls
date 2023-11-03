import random
import sys
from collections import defaultdict
from heapq import heappop, heappush

class Graph:
    def __init__(self):
        self.nodes = set()  # Set of all nodes in the graph
        self.edges = defaultdict(list)  # Dictionary to store adjacency list and edge weights
    
    def add_node(self, value):
        self.nodes.add(value)
    
    def add_edge(self, from_node, to_node, weight):
        self.add_node(from_node)
        self.add_node(to_node)
        self.edges[from_node].append((to_node, weight))
     
    def dijkstra(self, start_node):
        # Initialize distance dictionary with infinity for all nodes except the start node
        distances = {node: sys.maxsize for node in self.nodes}
        distances[start_node] = 0
        
        # Priority queue to store nodes and their corresponding distances
        queue = [(0, start_node)]
        
        while queue:
            current_dist, current_node = heappop(queue)  # Get the node with the smallest distance
            
            if current_dist > distances[current_node]:
                continue  # Skip if we have already found a shorter path to the current node
            
            for neighbor, weight in self.edges[current_node]:
                distance = current_dist + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance  # Update the distance
                    
                    # Add the neighbor to the priority queue with the updated distance
                    heappush(queue, (distance, neighbor))
        
        return distances
    
    def generate_random_graph(self, num_nodes, num_edges):
        for i in range(num_nodes):
            self.add_node(i)
        
        for _ in range(num_edges):
            from_node = random.randint(0, num_nodes - 1)
            to_node = random.randint(0, num_nodes - 1)
            weight = random.randint(1, 10)
            
            self.add_edge(from_node, to_node, weight)

if __name__ == "__main__":
    # Generate a random graph with 10 nodes and 20 edges
    graph = Graph()
    graph.generate_random_graph(10, 20)
    
    # Find the shortest path using Dijkstra's algorithm starting from node 0
    shortest_distances = graph.dijkstra(0)
    
    print("Shortest distances from node 0:")
    for node, distance in shortest_distances.items():
        print(f"Node {node}: {distance}")

# Function to find the shortest paths using the Bellman-Ford algorithm
def bellman_ford(graph, start):
    """
    Find the shortest paths from a starting node to all other nodes in a weighted graph.
    
    Parameters:
        graph (list): List of edges in the form (source, destination, weight)
        start (int): Starting node
    
    Returns:
        list: Shortest distances to all nodes from the start node
    """
    num_nodes = max(max(edge[0], edge[1]) for edge in graph) + 1
    distances = [float('inf')] * num_nodes
    distances[start] = 0

    for _ in range(num_nodes - 1):
        for source, destination, weight in graph:
            if distances[source] + weight < distances[destination]:
                distances[destination] = distances[source] + weight

    # Check for negative-weight cycles
    for source, destination, weight in graph:
        if distances[source] + weight < distances[destination]:
            raise ValueError("Graph contains a negative-weight cycle")

    return distances

# Example usage
if __name__ == "__main__":
    edges = [(0, 1, 4), (0, 2, 5), (1, 2, -3), (2, 3, 2)]
    start_node = 0
    try:
        shortest_paths = bellman_ford(edges, start_node)
        print("Shortest distances:", shortest_paths)
    except ValueError as e:
        print(e)

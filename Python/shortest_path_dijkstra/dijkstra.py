# Function to find the shortest path using Dijkstra's algorithm
import heapq

def dijkstra(graph, start):
    """
    Find the shortest paths from a starting node to all other nodes in a weighted graph.
    
    Parameters:
        graph (dict): Adjacency list representation of the graph
        start (str): Starting node
    
    Returns:
        dict: Shortest distances from the start node to all other nodes
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Example usage
if __name__ == "__main__":
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    start_node = 'A'
    shortest_distances = dijkstra(graph, start_node)
    print("Shortest distances from node", start_node, ":", shortest_distances)

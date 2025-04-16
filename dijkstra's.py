import time

start_time = time.time()
# Run your algorithm here
import heapq

def dijkstra(graph, start):
    pq = []  # Priority queue
    heapq.heappush(pq, (0, start))
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Example graph (Adjacency List)
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

source = 'A'
print(dijkstra(graph, source))

end_time = time.time()

print(f"Execution Time: {end_time - start_time:.6f} seconds")


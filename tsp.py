import time

start_time = time.time()
# Run your algorithm here


def tsp_nearest_neighbor(graph, start):
    unvisited = set(graph.keys())
    unvisited.remove(start)
    path = [start]
    current = start

    while unvisited:
        nearest = min(unvisited, key=lambda node: graph[current].get(node, float('inf')))
        path.append(nearest)
        unvisited.remove(nearest)
        current = nearest

    path.append(start)  # Return to the starting point
    return path

# Example graph (Adjacency List)
graph = {
    'A': {'B': 2, 'C': 5, 'D': 7},
    'B': {'A': 2, 'C': 3, 'D': 8},
    'C': {'A': 5, 'B': 3, 'D': 4},
    'D': {'A': 7, 'B': 8, 'C': 4}
}

start_city = 'A'
print(tsp_nearest_neighbor(graph, start_city))

end_time = time.time()

print(f"Execution Time: {end_time - start_time:.6f} seconds")

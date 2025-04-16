import time

start_time = time.time()
# Run your algorithm here


def floyd_warshall(graph):
    nodes = list(graph.keys())
    n = len(nodes)
    dist = {node: {node: float('inf') for node in nodes} for node in nodes}

    for node in nodes:
        dist[node][node] = 0
        for neighbor, weight in graph[node].items():
            dist[node][neighbor] = weight

    for k in nodes:
        for i in nodes:
            for j in nodes:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

# Example graph
graph = {
    'A': {'B': 3, 'C': 6},
    'B': {'A': 3, 'C': 2, 'D': 5},
    'C': {'A': 6, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

print(floyd_warshall(graph))

end_time = time.time()

print(f"Execution Time: {end_time - start_time:.6f} seconds")

import time

start_time = time.time()
# Run your algorithm here

import heapq
import math

def heuristic(a, b):  
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def a_star(graph, start, goal, coordinates):
    pq = []
    heapq.heappush(pq, (0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}

    while pq:
        _, current = heapq.heappop(pq)
        
        if current == goal:
            break

        for neighbor, weight in graph[current].items():
            new_cost = cost_so_far[current] + weight
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(coordinates[neighbor], coordinates[goal])
                heapq.heappush(pq, (priority, neighbor))
                came_from[neighbor] = current

    return came_from, cost_so_far

# Example graph
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Coordinates (x, y) for heuristic
coordinates = {'A': (0, 0), 'B': (1, 1), 'C': (2, 2), 'D': (3, 3)}

start = 'A'
goal = 'D'
print(a_star(graph, start, goal, coordinates))

end_time = time.time()

print(f"Execution Time: {end_time - start_time:.6f} seconds")

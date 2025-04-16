from flask import Flask, request, jsonify
import heapq

app = Flask(__name__)

# Sample graph (Replace with real data later)
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Dijkstra Algorithm Function
def dijkstra(graph, start):
    pq = []
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

# Flask Route for Dijkstra API
@app.route('/dijkstra', methods=['POST'])
def dijkstra_api():
    data = request.json
    source = data.get('source')

    if source not in graph:
        return jsonify({'error': 'Invalid source node'}), 400

    result = dijkstra(graph, source)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

import heapq

def dijkstra(graph, start):
    distances = {vertex: float("inf") for vertex in graph}
    distances[start] = 0
    queue = [(0, start)]
    while queue:
        current_distance, current_vertex = heapq.heappop(queue)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    return distances

graph = {
    "Moscow": {"St. Petersburg": 635, "Nizhny Novgorod": 400},
    "St. Petersburg": {"Nizhny Novgorod": 400},
    "Nizhny Novgorod": {"Kazan": 200, "Cheboksary": 250},
    "Kazan": {"Cheboksary": 800},
    "Cheboksary": {"Samara": 300},
    "Samara": {"Volgograd": 500},
    "Volgograd": {}
}

distances = dijkstra(graph, "Nizhny Novgorod")
print(distances["Volgograd"])

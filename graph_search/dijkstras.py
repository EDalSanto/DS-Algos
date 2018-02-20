import heapq

def calculate_distances(graph, starting_vertex):
    # Initialize distances starting_vertex to other vertices to infinity
    distances = {vertex: float('infinity') for vertex in graph}
    # starting to itself is of course 0
    distances[starting_vertex] = 0

    entry_lookup = {}
    pq = []

    #
    for vertex, distance in distances.items():
        entry = [distance, vertex]
        # Maintain a mapping of vertices to entries in our queues
        entry_lookup[vertex] = entry
        # heaps => binary trees for which every parent node has a value less than
        # or equal to any of its children
        # using heap ensures always getting smallest distance
        heapq.heappush(pq, entry)

    while len(pq) > 0:
        # Get the neighbor vertex with the lowest overall cost,
        # which bubbles its way to the top of priority queue
        current_distance, current_vertex = heapq.heappop(pq)

        # Check to see if vertices distances to neighbors less than already found
        for neighbor, neighbor_distance in graph[current_vertex].items():
            # account for distance from previous vertex
            distance = distances[current_vertex] + neighbor_distance
            # if new found distance to vertice less than already found
            if distance < distances[neighbor]:
                # update distances
                distances[neighbor] = distance
                entry_lookup[neighbor][0] = distance

    print(entry_lookup)
    return distances


example_graph = {
    'U': {'V': 2, 'W': 5, 'X': 1},
    'V': {'U': 2, 'X': 2, 'W': 3},
    'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
    'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
    'Y': {'X': 1, 'W': 1, 'Z': 1},
    'Z': {'W': 5, 'Y': 1},
}

print(calculate_distances(example_graph, 'U'))

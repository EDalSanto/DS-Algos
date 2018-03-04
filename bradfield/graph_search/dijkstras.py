import heapq

# Brute forces to find absolute shortest paths
def calculate_shortest(graph, starting_vertex):
    # Initialize distances starting_vertex to other vertices to infinity
    res = {vertex: { "distance": float('infinity'), "previous_vertex": None } for vertex in graph}
    # starting_vertex to itself is of course 0
    res[starting_vertex]["distance"] = 0

    # Initialize priority queue as heap with first node
    pq = []
    heapq.heappush(pq, [0, starting_vertex])

    while len(pq) > 0:
        # Get the vertex from the pq with the lowest overall cost,
        # which bubbles its way to the top because minheap
        current_distance, current_vertex = heapq.heappop(pq)

        # Check to see if vertices distances to neighbors less than already found
        for neighbor, neighbor_distance in graph[current_vertex].items():
            new_distance = res[current_vertex]["distance"] + neighbor_distance

            # update neighbors shortest distance and prev to start
            if new_distance < res[neighbor]["distance"]:
                res[neighbor]["distance"] = new_distance
                res[neighbor]["previous_vertex"] =  current_vertex

                # add neighbor to queue to further explore
                heapq.heappush(pq, [new_distance, neighbor])

    return res


example_graph = {
    'U': {'V': 2, 'W': 5, 'X': 1},
    'V': {'U': 2, 'X': 2, 'W': 3},
    'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
    'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
    'Y': {'X': 1, 'W': 1, 'Z': 1},
    'Z': {'W': 5, 'Y': 1}
}

print(calculate_shortest(example_graph, 'U'))

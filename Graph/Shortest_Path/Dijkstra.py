from collections import defaultdict
import heapq


def dijkstra(graph, source, destination):
    if source == destination:
        return [source], 0

    # Graph conversion to adj list
    adj_list = adj_list_ify(graph, directed=True)

    # Initialize distance and parent dictionaries
    distance = defaultdict(lambda: float('inf'))
    distance[source] = 0
    parent = defaultdict(lambda: None)

    # Priority queue and visited set
    pq = []
    visited = set()

    # Kickstart the algorithm
    heapq.heappush(pq, (0, source))

    while pq:
        dist, curr_node = heapq.heappop(pq)
        if curr_node in visited:
            continue

        visited.add(curr_node)

        for neighbor, neighbor_distance in adj_list[curr_node]:
            # Do three things when updating nodes:
            # - Update the distance dictionary
            # - Update the parent dictionary for path reconstruction
            # - Enqueue the min heap
            if dist + neighbor_distance < distance[neighbor]:
                distance[neighbor] = dist + neighbor_distance # Relaxation
                parent[neighbor] = curr_node
                heapq.heappush(pq, (dist + neighbor_distance, neighbor))

    # Path reconstruction:
    if distance[destination] == float('inf'):
        return None, float('inf')  # Destination unreachable

    path = []
    current = destination
    while current:
        path.append(current)
        current = parent[current]
    return path[::-1], distance[destination]


def adj_list_ify(edges, directed=False):
    adj_list = defaultdict(list)
    if directed:
        for u, v, w in edges:
            adj_list[u].append((v, w))
    else:
        for u, v, w in edges:
            adj_list[u].append((v, w))
            adj_list[v].append((u, w))
    return adj_list


def test_case():
    test_cases = [
        # (graph, source, destination, expected_path, expected_distance)
        ([(1, 2, 3), (1, 3, 5), (2, 4, 2), (2, 5, 4), (3, 5, 1)], 1, 4, [1, 2, 4], 5),
        ([], 1, 1, [1], 0),
        ([(1, 2, 2), (3, 4, 1)], 1, 4, None, float('inf')),
        ([(1, 2, 3), (1, 4, 5), (2, 3, 4), (5, 2, 6), (3, 5, 1), (5, 4, 6)], 1, 5, [1, 2, 3, 5], 8),
        ([(1, 2, 2), (1, 3, 6), (2, 4, 3), (3, 4, 2)], 1, 4, [1, 2, 4], 5),
        ([], 1, 3, None, float('inf')),
        ([(1, 2, 3), (1, 4, 4), (2, 3, 2), (2, 4, 1), (4, 5, 1), (5, 3, 1)], 1, 3, [1, 2, 3], 5)
    ]

    for i, (graph, source, destination, expected_path, expected_distance) in enumerate(test_cases, 1):
        path, dist = dijkstra(graph, source, destination)
        assert path == expected_path and dist == expected_distance, f"Test case {i} failed"
    print("All test cases passed!")


def main():
    test_case()


if __name__ == '__main__':
    main()

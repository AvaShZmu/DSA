from collections import defaultdict
import heapq


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


def dijkstra(graph, source):
    # Graph conversion to adj list
    adj_list = adj_list_ify(graph, directed=True)

    # Initialize distance and parent dictionaries
    distance = defaultdict(lambda: float('inf'))
    distance[source] = 0
    edgeto = defaultdict(lambda: None)

    # Priority queue and visited set
    pq = []
    visited = set()
    print("Khởi tạo dist, edgeto, pq, visited")

    # Kickstart the algorithm
    print(f"Bắt đầu: Cho {(0, source)} vào pq")
    heapq.heappush(pq, (0, source))
    print("-"*20)
    while pq:
        dist, curr_node = heapq.heappop(pq)
        print(f"Xét pq element: {(curr_node, dist)}")
        if curr_node in visited:
            continue

        print("Add vào visited set")
        visited.add(curr_node)

        for neighbor, neighbor_distance in adj_list[curr_node]:
            # Do three things when updating nodes:
            # - Update the distance dictionary
            # - Update the parent dictionary for path reconstruction
            # - Enqueue the min heap
            if dist + neighbor_distance < distance[neighbor]:
                print(f"update dist: dist[{neighbor}] = {dist + neighbor_distance}")
                distance[neighbor] = dist + neighbor_distance  # Relaxation
                print(f"update edgeto: edgeto[{neighbor}] = {(curr_node, neighbor)}")
                edgeto[neighbor] = (curr_node, neighbor)
                print(f"push {(neighbor, dist + neighbor_distance)} vào ")
                heapq.heappush(pq, (dist + neighbor_distance, neighbor))
        print(f"visited set: {visited}")
        print("-"*20)
    print("Dist:", dict(distance))
    print("Edgeto:", dict(edgeto))
    print(f"Shortest Path Tree: {list(edgeto.values())}")


if __name__ == "__main__":
    graph = [(0, 1, 4), (0, 7, 8), (1, 2, 8), (1, 7, 11),
(2, 3, 7), (2, 5, 4), (2, 8, 2), (3, 4, 9),
(3, 5, 14), (5, 6, 2), (6, 7, 1), (6, 8, 6),
(7, 8, 7), (8, 7, 3), (7, 0, 12), (4, 5, 10),
(0, 2, 5), (2, 0, 3), (3, 2, 9), (2, 4, 6)]

    form = ""
    for u, v, w in graph:
        form += f"{u}-({w})>{v}\n"
    print(form)
    dijkstra(graph, 3)

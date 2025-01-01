import heapq
from collections import defaultdict


def adj_list_convert(edges, directed=False):
    adj_list = defaultdict(list)
    if not directed:
        for u, v, w in edges:
            adj_list[u].append((v, w))
            adj_list[v].append((u, w))
    else:
        for u, v, w in edges:
            adj_list[u].append((v, w))
    return adj_list


def prim_mst(graph, vertices):
    start = 0
    mst = []
    visited = set()
    pq = []

    # Initialize
    visited.add(start)
    for neighbor, weight in graph[start]:
        heapq.heappush(pq, (weight, start, neighbor))

    # Process edges in increasing weight order
    while pq and len(visited) < vertices:
        weight, u, v = heapq.heappop(pq)
        if v not in visited:
            # Add edge to MST
            mst.append((u, v, weight))
            visited.add(v)

            for neighbor, weight in graph[v]:
                heapq.heappush(pq, (weight, v, neighbor))

    return mst


def main():
    edges = [
        (0, 1, 7),
        (0, 2, 8),
        (1, 2, 3),
        (1, 3, 6),
        (2, 4, 5),
        (3, 4, 4),
        (3, 5, 2),
        (4, 5, 1)
    ]
    adj_list = adj_list_convert(edges)
    vertices = len(adj_list)
    print(prim_mst(adj_list, vertices))


if __name__ == '__main__':
    main()

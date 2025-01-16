from collections import defaultdict


def bellmanford(V, edges, src):
    dist = defaultdict(lambda: float('inf'))
    dist[src] = 0
    parent = defaultdict(lambda: None)

    for i in range(V):
        for edge in edges:
            u, v, wt = edge
            if dist[u] != float('inf') and dist[u] + wt < dist[v]:
                if i == V - 1:
                    return -1
                dist[v] = dist[u] + wt
                parent[v] = u

    return dict(dist), dict(parent)


def main():
    edgelist = [
        (0, 1, 2),
        (0, 2, 4),
        (1, 2, -2),
        (1, 3, 1),
        (2, 4, 3),
        (3, 4, 1),
        (4, 1, -1)
    ]

    vertices = set()
    for i in edgelist:
        vertices.add(i[0])
        vertices.add(i[1])
    V = len(vertices)
    try:
        dist, parent = bellmanford(V, edgelist, 0)
        print(dist)
        print(parent)
    except TypeError:
        print("A negative cycle exists in this graph.")


if __name__ == '__main__':
    main()

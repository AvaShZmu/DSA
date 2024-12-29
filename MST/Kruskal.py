from Union.UnionCode import UF


def count_vertices(graph):
    vertices = set()
    for edge in graph:
        vertices.add(edge[0])
        vertices.add(edge[1])
    return len(vertices)


def kruskal_mst(graph, vertices):
    new_graph = sorted(graph, key=lambda x: x[2])
    mst = []
    uf = UF(vertices)
    for u, v, w in new_graph:
        if uf.find(u) != uf.find(v):
            mst.append((u, v, w))
            uf.union(u, v)
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
    vertices = count_vertices(edges)
    mst = kruskal_mst(edges, vertices)
    print(edges)
    print(mst)


if __name__ == '__main__':
    main()

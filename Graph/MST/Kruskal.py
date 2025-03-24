from Union.UnionCode import UF


def count_vertices(graph):
    vertices = set()
    for edge in graph:
        vertices.add(edge[0])
        vertices.add(edge[1])
    return max(vertices) + 1


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
        (0, 1, 4), (0, 7, 8), (1, 2, 8), (1, 7, 11), (2, 3, 7), (2, 5, 4),
        (2, 8, 2), (3, 4, 9), (3, 5, 14), (4, 5, 10), (5, 6, 2), (6, 7, 1),
        (6, 8, 6), (7, 8, 7), (7, 9, 6), (8, 9, 5), (1, 6, 5), (0, 2, 5)
    ]
    vertices = count_vertices(edges)
    mst = kruskal_mst(edges, vertices)
    print(mst)


if __name__ == '__main__':
    main()

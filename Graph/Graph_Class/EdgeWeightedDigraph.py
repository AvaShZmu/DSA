class EdgeWeightedDigraph:
    def __init__(self, graph, V):
        self.V = V
        self.adj_matrix = [[0 for _ in range(V)] for _ in range(V)]
        for u, v in graph:
            self.adj_matrix[u][v] = 1


def main():
    edge_list = [
        (0, 1),
        (1, 2),
        (1, 3),
        (2, 4)
    ]
    digraph = EdgeWeightedDigraph(edge_list, 5)


if __name__ == "__main__":
    main()

class UF:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        else:  # Equals
            self.parent[root_y] = root_x
            self.rank[root_x] += 1


def check_cycle(graph): # Usage Example
    graph_size = max(max(x, y) for x, y in graph) + 1
    union = UF(graph_size)
    for x, y in graph:
        if union.find(x) == union.find(y):
            return True
        union.union(x, y)
    else:
        return False


def main():  # Usage: Check for cycles
    graph = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 1), (2, 5)]
    print(check_cycle(graph))


if __name__ == '__main__':
    main()

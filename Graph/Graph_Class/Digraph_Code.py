from collections import defaultdict, deque


class Digraph:
    def __init__(self):
        self.adjacency_list = defaultdict(set)

    def add_edge(self, v, w):
        self.adjacency_list[v].add(w)

    def adjacent(self, adjacent):
        return self.adjacency_list[adjacent]

    def __str__(self):
        print_list = list()
        for i in range(len(self.adjacency_list)):
            for k in self.adjacency_list[i]:
                edge = f'({i}, {k})'
                print_list.append(edge)
        return "\n".join(sorted(print_list))

    def delete_edge(self, v, w):
        if self.adjacency_list[v] and w in self.adjacency_list[v]:
            self.adjacency_list[v].remove(w)
        else:
            raise ValueError(f"The edge ({v}, {w}) was not found.")

    def dfs(self, start):
        stack = [start]
        path = []
        visited = set()
        visited.add(start)

        while stack:
            current = stack.pop()
            path.append(current)
            for neighbor in self.adjacency_list[current]:
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)
        return f"DFS: {' -> '.join(list(map(str, path)))}"

    def bfs(self, start):
        queue = deque([start])
        path = []
        visited = set()
        visited.add(start)

        while queue:
            current = queue.popleft()
            path.append(current)
            for neighbor in self.adjacency_list[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return f"BFS: {' -> '.join(list(map(str, path)))}"


if __name__ == "__main__":
    g = Digraph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 3)
    g.add_edge(1, 2)
    g.add_edge(1, 0)
    g.add_edge(2, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 4)
    g.add_edge(3, 5)
    g.add_edge(4, 5)
    g.add_edge(5, 6)
    g.add_edge(6, 7)
    print(g)
    print(g.adjacency_list)
    print(g.dfs(3))
    print(g.bfs(3))

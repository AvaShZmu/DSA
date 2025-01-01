from collections import defaultdict


def topological_sort(g):
    def dfs(current):
        visited.add(current)
        for neighbor in g[current]:
            if neighbor not in visited:
                dfs(neighbor)
        # Marks the end of assessing a node
        stack.append(current)

    visited = set()
    stack = []

    for curr in list(g.keys()):
        if curr not in visited:
            dfs(curr)
    return stack[::-1]


if __name__ == '__main__':
    # Graph representation as an adjacency list
    graph = defaultdict(list)
    graph[1].append(0)
    graph[0].append(2)
    graph[2].append(3)
    graph[1].append(4)
    graph[4].append(3)
    print(dict(graph))
    sorted_order = topological_sort(graph)
    print(sorted_order)

import heapq
from collections import defaultdict


def adj_list_ify(input_graph):
    adj_list = defaultdict(list)
    for u, v, weight in input_graph:
        adj_list[u].append((weight, v))
        adj_list[v].append((weight, u))
    return adj_list


def uniform_cost_search(adj_list, start, goal):
    visited = set()
    pq = [(0, start)]
    parent = {start: None}
    distance = defaultdict(lambda: float("inf"))
    distance[start] = 0

    while pq:
        curr_dist, node = heapq.heappop(pq)
        if node == goal:
            path = []
            while node:
                path.append(node)
                node = parent[node]
            path = path[::-1]
            return ' -> '.join(path)
        visited.add(node)
        for neighbor in adj_list[node]:
            new_dist, new_node = neighbor
            if new_node not in visited and new_dist + curr_dist < distance[new_node]:
                heapq.heappush(pq, (new_dist + curr_dist, new_node))
                parent[new_node] = node
                distance[new_node] = new_dist + curr_dist


if __name__ == '__main__':
    graph = [
        ('A', 'B', 4),
        ('A', 'C', 2),
        ('B', 'C', 5),
        ('B', 'D', 10),
        ('C', 'D', 3),
        ('C', 'E', 8),
        ('D', 'E', 1),
        ('D', 'F', 6),
        ('E', 'F', 2)
    ]
    start = 'A'
    end = 'F'
    adj_list = adj_list_ify(graph)
    print(dict(adj_list))
    path = uniform_cost_search(adj_list, start, end)
    print(path)

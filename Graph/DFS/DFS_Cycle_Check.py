from collections import defaultdict


def dfs_cycle_check(graph, graph_size):
    def dfs(graph, node, recur, visited):
        visited[node] = True
        recur[node] = True

        for neighbor in graph.get(node, []):
            if not visited[neighbor]:
                if dfs(graph, neighbor, recur, visited):
                    return True
            elif recur[neighbor]:
                return True

        recur[node] = False
        return False

    visited = [False] * graph_size
    recur = [False] * graph_size

    for node in range(graph_size):
        if not visited[node]:
            if dfs(graph, node, recur, visited):
                return True
    return False


def adj_list_convert(graph, directed=False):
    adj_list = defaultdict(list)
    if not directed:
        for u, v in graph:
            adj_list[u].append(v)
            adj_list[v].append(u)
    else:
        for u, v in graph:
            adj_list[u].append(v)
    return adj_list


def main():
    graph = [(0, 1), (1, 2), (2, 3), (3, 4)]
    graph_size = len(set(u for edge in graph for u in edge))
    adj_list = adj_list_convert(graph, directed=True)
    print(dict(adj_list))
    print(dfs_cycle_check(adj_list, graph_size))


if __name__ == '__main__':
    main()

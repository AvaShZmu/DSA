from collections import defaultdict


def adj_list_convert(edges):
    adj_list = defaultdict(list)
    for i, j in edges:
        adj_list[j].append(i)
        adj_list[i].append(j)
    return adj_list


def dfs(adj_list):
    if adj_list == {}:
        raise KeyError
    start = min(adj_list.keys())
    visited = set()
    visited.add(start)
    stack = [start]
    while stack:
        mark = True
        current = stack.pop()
        for i in adj_list[current]:
            if i not in visited:
                mark = False
                stack.append(i)
                visited.add(i)
        if mark:
            return current
    return None


def main():
    graph_edges = [(1, 2), (2, 3), (3, 4), (4, 5), (1, 5)]
    adj_list = adj_list_convert(graph_edges)
    print(adj_list)
    print(f"The node that, when removed, still maintains the graph's connectivity is: {dfs(adj_list)}")


if __name__ == '__main__':
    try:
        main()
    except KeyError:
        print("The given graph is empty.")

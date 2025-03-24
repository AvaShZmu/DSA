from collections import defaultdict


def adj_list_ify(edgelist):
    adj_list = defaultdict(list)
    for u, v in edgelist:
        if v not in adj_list[u]:
            adj_list[u].append(v)
    return adj_list


def ids(start, goal, graph):
    MAX_DEPTH = 10
    for depth in range(MAX_DEPTH + 1):
        result = dls(start, goal, depth, graph)
        if result is not None:
            return result
    return "result not found"


def dls(start, goal, depth, graph):
    frontier = [(start, depth)]
    visited = set()
    parent = {start: None}

    while frontier:
        curr_node, curr_depth = frontier.pop()
        if curr_node == goal:
            # Reconstructs path
            path = []
            while curr_node:
                path.append(curr_node)
                curr_node = parent[curr_node]
            path.append(start)
            path = path[::-1]
            return " -> ".join(map(str, path))
        if curr_depth != 0:
            for neighbor in graph[curr_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    frontier.append((neighbor, curr_depth - 1))
                    parent[neighbor] = curr_node


if __name__ == '__main__':
    edges = [
        (0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6),
        (3, 7), (3, 8), (4, 9), (4, 10), (5, 11), (5, 12),
        (6, 13), (6, 14), (7, 15), (7, 16), (8, 17), (8, 18),
        (9, 19), (9, 20), (10, 21), (10, 22), (11, 23), (11, 24),
        (12, 25), (12, 26), (13, 27), (13, 28), (14, 29), (14, 30),
        (15, 31), (15, 32), (16, 33), (16, 34), (17, 35), (17, 36),
        (18, 37), (18, 38), (19, 39), (19, 40), (20, 41), (20, 42),
        (21, 43), (21, 44), (22, 45), (22, 46), (23, 47), (23, 48),
        (24, 49), (24, 50), (25, 51), (25, 52), (26, 53), (26, 54),
        (27, 55), (27, 56), (28, 57), (28, 58), (29, 59), (29, 60),
        (30, 61), (30, 62), (31, 63), (31, 64), (32, 65), (32, 66),
        (33, 67), (33, 68), (34, 69), (34, 70), (35, 71), (35, 72),
        (36, 73), (36, 74), (37, 75), (37, 76), (38, 77), (38, 78),
        (39, 79), (39, 80), (40, 81), (40, 82), (41, 83), (41, 84),
        (42, 85), (42, 86), (43, 87), (43, 88), (44, 89), (44, 90),
        (45, 91), (45, 92), (46, 93), (46, 94), (47, 95), (47, 96),
        (48, 97), (48, 98), (49, 99), (49, 100), (50, 101), (50, 102),
        (51, 103), (51, 104), (52, 105), (52, 106), (53, 107), (53, 108),
        (54, 109), (54, 110), (55, 111), (55, 112), (56, 113), (56, 114),
        (57, 115), (57, 116), (58, 117), (58, 118), (59, 119), (59, 120),
        (60, 121), (60, 122), (61, 123), (61, 124), (62, 125), (62, 126),
        (63, 127), (63, 128), (64, 129), (64, 130), (65, 131), (65, 132),
        (66, 133), (66, 134), (67, 135), (67, 136), (68, 137), (68, 138),
        (69, 139), (69, 140), (70, 141), (70, 142), (71, 143), (71, 144),
        (72, 145), (72, 146), (73, 147), (73, 148), (74, 149),
        (1, 5), (3, 9), (5, 10), (7, 14), (10, 19),
        (15, 30), (21, 40), (35, 50), (40, 60), (60, 100),
        (65, 120), (80, 130), (110, 140)
    ]

    start_node = 0
    end_node = 149

    adj_list = adj_list_ify(edges)
    print(dict(adj_list))
    result = ids(start_node, end_node, adj_list)
    print(result)

from collections import defaultdict, deque


def adj_list_convert(edges):
    adj_list = defaultdict(list)
    for i, j in edges:
        adj_list[j].append(i)
        adj_list[i].append(j)
    return adj_list


class GraphProperties:
    def __init__(self, graph):
        self.graph = graph
        self.diameter = float("-inf")
        self.radius = float("inf")
        self.center = []
        if not self.__check_connectivity():
            raise ValueError
        self.__process()

    def __check_connectivity(self):
        graph_length = len(self.graph)
        start_node = min(self.graph.keys())
        check_queue = deque([start_node])
        visited = set()
        visited.add(start_node)

        while check_queue:
            current = check_queue.popleft()

            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    check_queue.append(neighbor)
        return len(visited) == graph_length

    def __eccentricity(self, node):
        queue = deque([node])
        visited = set()
        visited.add(node)
        distance = {node: 0}
        max_distance = 0

        while queue:
            current = queue.popleft()
            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
                    distance[neighbor] = distance[current] + 1
                    max_distance = max(max_distance, distance[neighbor])
        return max_distance

    def __process(self):
        track_keeper = defaultdict(int)
        for i in self.graph:
            curr_eccentricity = self.__eccentricity(i)
            track_keeper[i] = curr_eccentricity
            if self.diameter < curr_eccentricity:
                self.diameter = curr_eccentricity
            if self.radius > curr_eccentricity:
                self.radius = curr_eccentricity
        for node, value in track_keeper.items():
            if value == self.radius:
                self.center.append(str(node))


def main():
    graph_edge = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
    adj_list = adj_list_convert(graph_edge)
    try:
        graph = GraphProperties(adj_list)
        radius, diameter, center = graph.radius, graph.diameter, sorted(graph.center)
        print(f"radius: {radius}, diameter: {diameter}, center: ({"), (".join(center)})")
    except ValueError:
        print("The given graph is not connected.")


if __name__ == '__main__':
    main()

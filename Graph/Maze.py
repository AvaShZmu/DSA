# Stimulated maze using BFS
from collections import deque

Directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def find_neighbors(maze, vertex):
    x, y = vertex
    neighbors = []

    for dx, dy in Directions:
        neighbor_x = x + dx
        neighbor_y = y + dy

        if 0 <= neighbor_x < len(maze) and 0 <= neighbor_y < len(maze[0]) and maze[neighbor_x][neighbor_y] == 0:
            neighbors.append((neighbor_x, neighbor_y))

    return neighbors


def dfs(maze, start, end):
    x, y = start
    if maze[x][y] == 1:
        return None
    stack = [start]
    visited = set()
    visited.add(start)

    parent = {start: None}

    # BFS loop
    while stack:
        current = stack.pop()

        if current == end:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]

        else:
            for neighbor in find_neighbors(maze, current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
                    parent[neighbor] = current
    return None


if __name__ == "__main__":
    maze = [
        [0, 1, 0, 0, 0, 0, 0, 1],
        [0, 1, 0, 1, 1, 0, 0, 1],
        [0, 1, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 0, 0, 1, 0],
        [0, 0, 0, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 0, 0]
    ]
    start = (0, 0)
    end = (7, 7)
    path = dfs(maze, start, end)
    print("Found the path:", path)

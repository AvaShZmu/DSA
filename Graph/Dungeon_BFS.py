from collections import deque


def find_neighbors(maze, vertex):
    neighbors = []
    x, y = vertex
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dx, dy in directions:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] != '#':
            neighbors.append((nx, ny))
    return neighbors


def bfs(maze, start, end):
    curr_queue = deque([start])
    visited = set()
    visited.add(start)

    parent = {start: None}

    while curr_queue:
        current = curr_queue.popleft()
        if current == end:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            path = path[::-1]
            return path
        for neighbor in find_neighbors(maze, current):
            if neighbor not in visited:
                visited.add(neighbor)
                curr_queue.append(neighbor)
                parent[neighbor] = current
    return None


def find_start_end(maze):
    start = None
    end = None
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                start = (i, j)
            if maze[i][j] == 'E':
                end = (i, j)
    return start, end


if __name__ == '__main__':
    maze = [['S', '.', '.', '#', '.', '.', '.'],
            ['.', '#', '.', '.', '.', '#', '.'],
            ['.', '#', '.', '.', '.', '.', '.'],
            ['.', '.', '#', '#', '.', '.', '.'],
            ['#', '.', '#', 'E', '.', '#', '.']]
    start, end = find_start_end(maze)
    path = bfs(maze, start, end)

    print("Path:", path)
    print(f"Time: {len(path)} minutes.")

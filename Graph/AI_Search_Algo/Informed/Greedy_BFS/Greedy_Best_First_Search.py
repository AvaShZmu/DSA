import heapq
import os


def read_map():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    file_dir = os.path.join(parent_dir, 'map.txt')
    search_map = []
    with open(file_dir, 'r') as f:
        for line in f:
            if '+' in line:
                header = line
            temp = []
            for i in line.rstrip():
                temp.append(i)
            temp = temp[1:]
            temp = temp[:-1]
            search_map.append(temp)
    search_map = search_map[1:]
    search_map = search_map[:-1]
    return search_map, header


# Heuristic: Manhattan distance
def manhattan(curr, goal):
    x1, x2 = curr[0], goal[0]
    y1, y2 = curr[1], goal[1]
    return abs(x1 - x2) + abs(y1 - y2)


def find_neighbor(curr, maze):
    neighbors = []
    curr_x, curr_y = curr
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for dx, dy in moves:
        new_x, new_y = curr_x + dx, curr_y + dy
        if 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and maze[new_x][new_y] in [" ", "G"]:
            neighbors.append((new_x, new_y))
    return neighbors


def best_first(start, goal, maze):
    pq = [(manhattan(start, goal), start)]
    visited = {start}
    parent = {start: None}

    while pq:
        _, node = heapq.heappop(pq)
        if node == goal:
            path = []
            current_path = parent[goal]
            while current_path:
                path.append(current_path)
                current_path = parent[current_path]
            return path[::-1]

        for neighbor in find_neighbor(node, maze):
            if neighbor not in visited:
                visited.add(neighbor)
                heapq.heappush(pq, (manhattan(neighbor, goal), neighbor))
                parent[neighbor] = node
    return None


def find_coordinates(maze):
    goal = None
    start = None
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'G':
                goal = (i, j)
            if maze[i][j] == 'S':
                start = (i, j)
    return start, goal


def print_maze(answer, header, script_dir):
    file_dir = os.path.join(script_dir, 'greedy_bfs_solution.txt')
    with open(file_dir, 'w') as f:
        f.write(f"{header}")
        for i in answer:
            temp = f"|{''.join(i)}|\n"
            f.write(temp)
        f.write(f"{header}")
    f.close()


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    maze, header = read_map()

    start, goal = find_coordinates(maze)
    try:
        path = best_first(start, goal, maze)[1:]
        new_maze = maze[:]
        for i in range(len(maze)):
            for j in range(len(maze[0])):
                if (i, j) in path:
                    new_maze[i][j] = "."
        print_maze(new_maze, header, script_dir)
    except TypeError:
        print("There is no available path.")


if __name__ == '__main__':
    main()

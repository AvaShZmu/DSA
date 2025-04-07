import pygame
import time
from collections import deque
import heapq
import math

# >>> This is only for educational purpose only. A product from ChatGPT slop. <<<
                                                   # (And some modifications)

# Options:
only_show_path = False
# If this option is enabled, hide the visited and frontier cells after path reconstruction


# Function to draw the grid with various colors for visualization
def draw_grid(screen, maze, cell_size, start, goal, visited, frontier, path=[]):
    """Draw the grid for the maze, including walls, start, goal, visited cells, and path."""
    rows, cols = len(maze), len(maze[0])
    colors = {
        0: (230, 247, 255),  # Open cell (light blue)
        1: (211, 211, 211),  # Wall (light gray)
        "start": (168, 230, 207),  # Start (pastel green)
        "goal": (255, 182, 185),  # Goal (light coral)
        "visited": (230, 217, 247),  # Visited (light lavender)
        "path": (173, 216, 230),  # Path (light blue)
        "queue": (255, 249, 196),  # Frontier (light yellow)
    }

    for r in range(rows):
        for c in range(cols):
            if (r, c) == start:
                color = colors["start"]
            elif (r, c) == goal:
                color = colors["goal"]
            elif (r, c) in path:
                color = colors["path"]
            elif (r, c) in visited:
                color = colors["visited"]
            elif (r, c) in frontier:
                color = colors["queue"]
            elif maze[r][c] == 1:
                color = colors[1]  # Wall (black)
            else:
                color = colors[0]  # Open space (white)

            pygame.draw.rect(screen, color, (c * cell_size, r * cell_size, cell_size, cell_size))

    pygame.display.flip()


# A* Algorithm
def astar(maze, start, goal, rows, cols, screen, cell_size, clock):
    """Optimized A* algorithm with step-by-step visualization."""

    def heuristic(a, b):
        return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

    visited = set()
    frontier = []  # Priority queue for A*
    heapq.heappush(frontier, (0, start))  # (f-cost, node)
    g_costs = {start: 0}  # Store g-costs
    f_costs = {start: heuristic(start, goal)}  # f-cost = g-cost + h-cost
    parent = {start: None}  # Store parent nodes for path reconstruction
    path = []
    in_frontier = {start: True}  # Set for checking if a node is in the frontier

    while frontier:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        _, current = heapq.heappop(frontier)

        if current in visited:
            continue

        visited.add(current)
        in_frontier[current] = False

        if current == goal:
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1], visited, set(in_frontier.keys())

        r, c = current
        directions = [
            (0, 1),  # right
            (1, 0),  # down
            (0, -1),  # left
            (-1, 0),  # up
            (1, 1),  # down-right (diagonal)
            (1, -1),  # down-left (diagonal)
            (-1, 1),  # up-right (diagonal)
            (-1, -1),  # up-left (diagonal)
        ]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols) and maze[nr][nc] == 0 and (nr, nc) not in visited:
                new_g_cost = g_costs[current] + 1
                new_f_cost = g_costs[current] + 1.5 * heuristic((nr, nc), goal)

                if (nr, nc) not in g_costs or new_g_cost < g_costs[(nr, nc)]:
                    g_costs[(nr, nc)] = new_g_cost
                    f_costs[(nr, nc)] = new_f_cost
                    parent[(nr, nc)] = current

                    if (nr, nc) not in in_frontier:
                        heapq.heappush(frontier, (new_f_cost, (nr, nc)))
                        in_frontier[(nr, nc)] = True
                    else:
                        for i, (f_cost, node) in enumerate(frontier):
                            if node == (nr, nc):
                                frontier[i] = (new_f_cost, (nr, nc))
                                heapq.heapify(frontier)
                                break

        # Draw the grid and update the screen, passing the frontier as a set for visualization
        draw_grid(screen, maze, cell_size, start, goal, visited, set(in_frontier.keys()), path)
        pygame.display.update()  # Update the display
        clock.tick(60)  # Control the speed of the algorithm (60 FPS)

    return None


def bfs(maze, start, goal, rows, cols, screen, cell_size, clock):
    visited = set()
    frontier = deque([start])  # Queue for BFS
    parent = {start: None}  # Store parent nodes for path reconstruction
    path = []

    while frontier:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        current = frontier.popleft()

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1], visited, frontier

        r, c = current
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0 and (nr, nc) not in visited:
                frontier.append((nr, nc))  # Add to the frontier
                parent[(nr, nc)] = (r, c)

        # Draw the grid and update the screen
        draw_grid(screen, maze, cell_size, start, goal, visited, set(frontier))
        pygame.display.update()  # Update the display
        clock.tick(60)  # Control the speed of the algorithm (60 FPS)

    return None


def dfs(maze, start, goal, rows, cols, screen, cell_size, clock):
    visited = set()
    frontier = [start]  # Stack for DFS
    parent = {start: None}  # Store parent nodes for path reconstruction
    path = []

    while frontier:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        current = frontier.pop()

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1], visited, frontier

        r, c = current
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0 and (nr, nc) not in visited:
                frontier.append((nr, nc))  # Add to the frontier
                parent[(nr, nc)] = (r, c)

        # Draw the grid and update the screen
        draw_grid(screen, maze, cell_size, start, goal, visited, set(frontier))
        pygame.display.update()  # Update the display
        clock.tick(60)  # Control the speed of the algorithm (60 FPS)

    return None


# Function to create the maze interactively (unchanged)
def create_maze(rows, cols, cell_size, screen, clock):
    """Let the user draw the maze interactively."""
    maze = [[0 for _ in range(cols)] for _ in range(rows)]
    start, goal = (0, 0), (rows - 1, cols - 1)

    running = True
    drawing_wall = False
    erasing_wall = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                r, c = y // cell_size, x // cell_size

                if event.button == 1:  # Left click to draw walls
                    if (r, c) == start or (r, c) == goal:
                        continue
                    maze[r][c] = 1
                    drawing_wall = True

                elif event.button == 3:  # Right click to erase walls
                    if (r, c) == start or (r, c) == goal:
                        continue
                    maze[r][c] = 0
                    erasing_wall = True

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Stop drawing walls
                    drawing_wall = False
                elif event.button == 3:  # Stop erasing walls
                    erasing_wall = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:  # Set start point
                    x, y = pygame.mouse.get_pos()
                    r, c = y // cell_size, x // cell_size
                    if maze[r][c] == 0:
                        start = (r, c)

                elif event.key == pygame.K_g:  # Set goal point
                    x, y = pygame.mouse.get_pos()
                    r, c = y // cell_size, x // cell_size
                    if maze[r][c] == 0:
                        goal = (r, c)

                elif event.key == pygame.K_1:  # Finish drawing and start visualization
                    return maze, start, goal

        # Handle continuous wall drawing or erasing
        if drawing_wall or erasing_wall:
            x, y = pygame.mouse.get_pos()
            r, c = y // cell_size, x // cell_size
            if 0 <= r < rows and 0 <= c < cols and (r, c) != start and (r, c) != goal:
                maze[r][c] = 1 if drawing_wall else 0

        # Draw the grid
        screen.fill((0, 0, 0))
        draw_grid(screen, maze, cell_size, start, goal, visited=set(), frontier=set())
        clock.tick(60)

    pygame.quit()


# The function to visualize the pathfinding algorithms
def visualize_pathfinding(maze, start, goal, algorithm="BFS"):
    """Visualize the pathfinding process using Pygame."""
    pygame.init()
    cell_size = 20
    rows, cols = len(maze), len(maze[0])
    screen = pygame.display.set_mode((cols * cell_size, rows * cell_size))
    pygame.display.set_caption(f"Maze Pathfinding Visualization - {algorithm}")
    clock = pygame.time.Clock()


    # Run the selected algorithm
    try:
        if algorithm == "BFS":
            path, visited, frontier = bfs(maze, start, goal, rows, cols, screen, cell_size, clock)
        elif algorithm == "A*":
            path, visited, frontier = astar(maze, start, goal, rows, cols, screen, cell_size, clock)
        elif algorithm == "DFS":
            path, visited, frontier = dfs(maze, start, goal, rows, cols, screen, cell_size, clock)
    except TypeError:
        print("There is no available path.")
        pygame.quit()
        return
    global only_show_path
    if only_show_path:
        visited = set()
        frontier = set()
    # Visualize the final path (mark it blue)
    if path:
        print("Path found!")
        draw_grid(screen, maze, cell_size, start, goal, visited, frontier, path)
        time.sleep(0.05)  # Pause to visualize the path step by step

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    rows, cols = 30, 30
    cell_size = 20

    # Initialize Pygame to allow user input to choose the algorithm
    while True:
        try:
            input_choice = int(input("Choose your algorithm:\n"
                                     "1. A* (Fastest)\n"
                                     "2. BFS (Mid)\n"
                                     "3. DFS (Dumbass)\n"))
            if 1 <= input_choice <= 3:
                algorithm = ['A*', 'BFS', 'DFS', 'Bidirectional'][input_choice - 1]
                break
            print("Wrong input")
        except ValueError:
            print("Wrong input")

    # Initialize the Pygame window for maze creation
    pygame.init()
    screen = pygame.display.set_mode((cols * cell_size, rows * cell_size))
    clock = pygame.time.Clock()

    # Let the user draw the maze
    maze, start, goal = create_maze(rows, cols, cell_size, screen, clock)

    # Visualize the selected algorithm
    visualize_pathfinding(maze, start, goal, algorithm=algorithm)

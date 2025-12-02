import collections
import heapq

def solve_maze_bfs(maze, start, end):
    """Resuelve el laberinto usando el algoritmo de Búsqueda en Amplitud (BFS)."""
    rows, cols = len(maze), len(maze[0])
    queue = collections.deque([(start, [start])])
    visited = set()
    visited.add(start)

    while queue:
        (curr_row, curr_col), path = queue.popleft()

        if (curr_row, curr_col) == end:
            return path

        # Movimientos posibles: derecha, izquierda, abajo, arriba
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_row, next_col = curr_row + dr, curr_col + dc
            
            if 0 <= next_row < rows and 0 <= next_col < cols and \
               maze[next_row][next_col] == 0 and (next_row, next_col) not in visited:
                visited.add((next_row, next_col))
                new_path = list(path)
                new_path.append((next_row, next_col))
                queue.append(((next_row, next_col), new_path))
    
    return None  # No se encontró camino


def solve_maze_dfs(maze, start, end):
    """Resuelve el laberinto usando el algoritmo de Búsqueda en Profundidad (DFS)."""
    rows, cols = len(maze), len(maze[0])
    stack = [(start, [start])]
    visited = set()
    visited.add(start)

    while stack:
        (curr_row, curr_col), path = stack.pop()

        if (curr_row, curr_col) == end:
            return path

        # Movimientos posibles: derecha, izquierda, abajo, arriba
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_row, next_col = curr_row + dr, curr_col + dc

            if 0 <= next_row < rows and 0 <= next_col < cols and \
               maze[next_row][next_col] == 0 and (next_row, next_col) not in visited:
                visited.add((next_row, next_col))
                new_path = list(path)
                new_path.append((next_row, next_col))
                stack.append(((next_row, next_col), new_path))

    return None  # No se encontró camino


def heuristic(a, b):
    """Heurística de Manhattan para A*."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def solve_maze_astar(maze, start, end):
    """Resuelve el laberinto usando el algoritmo A*."""
    rows, cols = len(maze), len(maze[0])

    # open_set: (f, g, (row, col), path)
    open_set = []
    start_h = heuristic(start, end)
    heapq.heappush(open_set, (start_h, 0, start, [start]))

    # Costos g conocidos para cada nodo visitado
    g_cost = {start: 0}

    while open_set:
        f, g, (curr_row, curr_col), path = heapq.heappop(open_set)

        if (curr_row, curr_col) == end:
            return path

        # Movimientos posibles: derecha, izquierda, abajo, arriba
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_row, next_col = curr_row + dr, curr_col + dc

            if not (0 <= next_row < rows and 0 <= next_col < cols):
                continue

            if maze[next_row][next_col] != 0:
                continue

            neighbor = (next_row, next_col)
            tentative_g = g + 1  # cada paso vale 1

            if neighbor not in g_cost or tentative_g < g_cost[neighbor]:
                g_cost[neighbor] = tentative_g
                new_path = list(path)
                new_path.append(neighbor)
                h = heuristic(neighbor, end)
                new_f = tentative_g + h
                heapq.heappush(open_set, (new_f, tentative_g, neighbor, new_path))

    return None  # No se encontró camino


# Representación del laberinto (0: camino libre, 1: muro)
# Puedes sustituir este MAZE por el que cargas desde tu archivo TXT si lo deseas.
MAZE = [
    [0,1,0,0,0,0,1,0,0,0],
    [0,1,0,1,1,0,1,0,1,0],
    [0,0,0,0,1,0,0,0,1,0],
    [1,1,1,0,1,1,1,0,1,0],
    [0,0,0,0,0,0,0,0,1,0],
    [0,1,1,1,1,1,1,0,1,0],
    [0,0,0,0,0,0,1,0,1,0],
    [0,1,1,1,1,0,1,0,1,0],
    [0,0,0,0,1,0,0,0,1,0],
    [0,1,1,0,0,0,1,0,0,0]
]

START = (0, 0)
END = (9, 9)


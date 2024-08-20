import heapq
import math

def heuristic(a, b): # Manhattan heuristic function
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    open_set = [(0, start)]
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), 
                  (1, 1), (1, -1), (-1, 1), (-1, -1)]
    while open_set:
        _, current = heapq.heappop(open_set)
        if current == goal:
            path = []
            while current in came_from:
                path.insert(0, current)
                current = came_from[current]
            path.insert(0, start)
            return path, g_score[goal]
        
        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and maze[neighbor[0]][neighbor[1]] == 1:
                move_cost = math.sqrt(2) if direction in directions[4:] else 1
                tentative_g_score = g_score[current] + move_cost
                if tentative_g_score < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
    
    return None

#input example:
maze = [
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1, 0, 0, 1]
]

start = (0, 0)
goal = (8, 9)
if astar(maze, start, goal):
    path, cost = astar(maze, start, goal)

    print("Path:", path)
    print("Cost:", cost)

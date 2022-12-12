import numpy as np


# Function to read the grid from the input file
def read_grid(file):
    grid = np.array([list(line.strip()) for line in file])

    start = tuple(np.transpose(np.where(grid == 'S'))[0])
    end = tuple(np.transpose(np.where(grid == 'E'))[0])
    grid[start] = 'a'
    grid[end] = 'z'

    return grid, start, end


# Function to calculate the Manhattan distance between two points (heuristic function)
def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# Function to get the neighbors of a given position
def get_neighbors(position, grid):
    x, y = position
    return [(i, j) for i, j in [(x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y)] if
            0 <= i < grid.shape[0] and 0 <= j < grid.shape[1] and ord(grid[i, j]) <= (ord(grid[x, y]) + 1)]


# Function to perform the A* search algorithm
def a_star_search(grid, start, end):
    g = {}
    f = {}

    g[start] = 0
    f[start] = g[start] + manhattan_distance(start, end)

    open_list = [start]

    while open_list:

        current = min(open_list, key=lambda x: f[x])
        open_list.remove(current)

        if current == end:
            return f[current]

        for successor in get_neighbors(current, grid):
            successor_cost = g[current] + 1
            if successor not in g or successor_cost < g[successor]:
                g[successor] = successor_cost
                f[successor] = g[successor] + manhattan_distance(successor, end)
                open_list.append(successor)

    return float('inf')


# Solution to Problem 1
def problem1():
    with open("data/input12.txt") as file:
        grid, start, end = read_grid(file)

        return a_star_search(grid, start, end)


# Solution to Problem 2
def problem2():
    with open("data/input12.txt") as file:
        grid, start, end = read_grid(file)

        starting_points = np.transpose(np.where(grid == 'a'))
        return min([a_star_search(grid, tuple(point), end) for point in starting_points])


# Execute the two problems solutions
print("Result to problem 1: ", problem1())
print("Result to problem 2: ", problem2())

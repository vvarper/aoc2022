import math


# Function to read the grid from the input file
def read_grid(file):
    grid = []

    for line in file:
        line = list(line.strip())[1:-1]
        if line[1] != '#':
            grid += [line]

    return grid


# class to represent a node in the search tree
class Node:
    # Constructor
    def __init__(self, position, step, normalized_step):
        self.position = position
        self.step = step
        self.normalized_step = normalized_step

    # Equality operator
    def __eq__(self, other):
        return self.position == other.position and self.normalized_step == other.normalized_step

    # Hash function
    def __hash__(self):
        return hash((self.position, self.normalized_step))


# Function to get the neighbors of a node
def get_neighbors(state, grid, interesting_steps, start, end):
    neighbors = []
    new_step = state.step + 1
    new_normalized_step = new_step % interesting_steps
    x, y = state.position

    for i, j in [(x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y), (x, y)]:
        if (i, j) == start or (i, j) == end or \
                (i >= 0 and j >= 0 and i < len(grid) and j < len(grid[i]) and \
                 grid[(i - new_step) % len(grid)][j] != 'v' and \
                 grid[(i + new_step) % len(grid)][j] != '^' and \
                 grid[i][(j - new_step) % len(grid[i])] != '>' and grid[i][
                     (j + new_step) % len(grid[i])] != '<'):
            neighbors.append(Node((i, j), new_step, new_normalized_step))

    return neighbors


# Function to perform the breadth first search algorithm
def breadth_first_search(grid, start, end, initial_step):
    interesting_steps = math.lcm(len(grid), len(grid[0]))
    queue = [Node(start, initial_step, initial_step)]
    visited = set()

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            if node.position == end:
                return node.step
            for neighbor in get_neighbors(node, grid, interesting_steps, start, end):
                queue.append(neighbor)

    return -1


# Solution to Problem 1
def problem1():
    with open("data/input24.txt") as file:
        grid = read_grid(file)
        start = (-1, 0)
        end = (len(grid), len(grid[0]) - 1)

        return breadth_first_search(grid, start, end, 0)


# Solution to Problem 2
def problem2():
    with open("data/input24.txt") as file:
        grid = read_grid(file)
        start = (-1, 0)
        end = (len(grid), len(grid[0]) - 1)

        return breadth_first_search(grid, start, end,
                                    breadth_first_search(grid, end, start,
                                                         breadth_first_search(grid, start, end, 0)))


# Execute the two problems solutions
print("Result to problem 1: ", problem1())
print("Result to problem 2: ", problem2())

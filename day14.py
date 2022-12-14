import numpy as np


# Function to read paths from file
def read_paths(file):
    cave = []
    for line in file:
        sequence = np.array([point.split(',') for point in line.strip().split(' -> ')], dtype=int)
        cave.append(sequence)
    return cave


# Function to create a cave from a list of paths
def create_cave(paths, floor=False):
    # 1. Initialize cave

    # 1.1 Get dimensions
    min_x = min([min(path[:, 0]) for path in paths])
    max_x = max([max(path[:, 0]) for path in paths])
    min_y = min([min(path[:, 1]) for path in paths] + [0])
    max_y = max([max(path[:, 1]) for path in paths])

    # * 1.2 If floor is required, adjust dimensions and add floor to paths
    if floor:
        max_y += 2
        max_x = max(max_x, 500 + max_y)
        min_x = min(min_x, 500 - max_y)
        paths += [np.array([[min_x, max_y], [max_x, max_y]])]

    # 1.3 Create an empty cave and set the source
    cave = np.array([['.' for x in range(max_x - min_x + 1)] for y in range(max_y - min_y + 1)])
    point = lambda x, y: (y - min_y, x - min_x)
    cave[point(500, 0)] = '+'

    # 2. Add paths to cave
    for path in paths:
        previous_x, previous_y = path[0]
        for x, y in path:
            if x != previous_x:
                for i in range(min(previous_x, x), max(previous_x, x) + 1):
                    cave[point(i, previous_y)] = '#'
            elif y != previous_y:
                for i in range(min(previous_y, y), max(previous_y, y) + 1):
                    cave[point(previous_x, i)] = '#'
            previous_x, previous_y = x, y

    return cave


# Function to check if a char is ground
def is_ground(char):
    return char == '#' or char == 'o'


# Function to check if a point is the abyss (out of bounds)
def is_abyss(cave, row, col):
    return row < 0 or row >= cave.shape[0] or col < 0 or col >= cave.shape[1]


# Function to simulate falling sand until it reaches the abyss
def simulate_falling_sand_to_abyss(cave):
    start = tuple(np.transpose(np.where(cave == '+'))[0])
    in_ground = True
    count = 0

    # While the source falls into the ground: simulate new falling sand
    while in_ground:
        current = start
        falling = True

        # While the sand not reaches the abyss or the ground: continue falling
        while falling and in_ground:
            if is_abyss(cave, current[0] + 1, current[1]):
                in_ground = False
            elif is_ground(cave[current[0] + 1, current[1]]):
                if is_abyss(cave, current[0] + 1, current[1] - 1):
                    in_ground = False
                elif is_ground(cave[current[0] + 1, current[1] - 1]):
                    if is_abyss(cave, current[0] + 1, current[1] + 1):
                        in_ground = False
                    elif is_ground(cave[current[0] + 1, current[1] + 1]):
                        falling = False
                        cave[current] = 'o'
                        count += 1
                    else:
                        current = (current[0], current[1] + 1)
                else:
                    current = (current[0], current[1] - 1)
            else:
                current = (current[0] + 1, current[1])

    return count


# Function to simulate falling sand until it blocks the source
def simulate_falling_sand_to_source(cave):
    start = tuple(np.transpose(np.where(cave == '+'))[0])
    source_blocked = False
    count = 0

    # While the source is not blocked by sand: simulate new falling sand
    while not source_blocked:
        current = start
        falling = True

        # While the sand not reaches the ground: continue falling
        while falling:
            if is_ground(cave[current[0] + 1, current[1]]):
                if is_ground(cave[current[0] + 1, current[1] - 1]):
                    if is_ground(cave[current[0] + 1, current[1] + 1]):
                        falling = False
                        cave[current] = 'o'
                        count += 1
                        source_blocked = current == start
                    else:
                        current = (current[0], current[1] + 1)
                else:
                    current = (current[0], current[1] - 1)
            else:
                current = (current[0] + 1, current[1])

    return count


# Solution to Problem 1
def problem1():
    with open("data/input14.txt") as file:
        # Read paths
        paths = read_paths(file)

        # Initialize cave without floor
        cave = create_cave(paths)

        return simulate_falling_sand_to_abyss(cave)


# Solution to Problem 2
def problem2():
    with open("data/input14.txt") as file:
        # Read paths
        paths = read_paths(file)

        # Initialize cave with floor
        cave = create_cave(paths, floor=True)

        return simulate_falling_sand_to_source(cave)


# Execute the two problems solutions
print("Result to problem 1: ", problem1())
print("Result to problem 2: ", problem2())

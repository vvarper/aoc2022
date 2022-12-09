import numpy as np


# Function to check if two points are adjacent
def are_adjacent(a, b):
    return abs(a[0] - b[0]) <= 1 and abs(a[1] - b[1]) <= 1


# Function to get the move to make from tail to head (head is not adjacent to tail)
def get_move(head, tail):
    return np.clip(np.array(head) - np.array(tail), a_min=-1, a_max=1)


# Dictionary of functions to apply moves to head
apply_move = {'U': lambda x: (x[0], x[1] + 1),
              'D': lambda x: (x[0], x[1] - 1),
              'L': lambda x: (x[0] - 1, x[1]),
              'R': lambda x: (x[0] + 1, x[1])}


# Solution to Problem 1
def problem1():
    with open("data/input9.txt") as file:
        head = [0, 0]
        tail = [0, 0]
        visited = set()
        visited.add(tuple(tail))

        for line in file:
            line = line.strip().split()
            for _ in range(int(line[1])):
                head = apply_move[line[0]](head)

                if not are_adjacent(head, tail):
                    tail += get_move(head, tail)
                    visited.add(tuple(tail))

        return len(visited)


# Solution to Problem 2
def problem2():
    with open("data/input9.txt") as file:
        n_knots = 10
        knots = [[0, 0] for _ in range(n_knots)]
        visited = set()
        visited.add(tuple(knots[-1]))

        for line in file:
            line = line.strip().split()
            for _ in range(int(line[1])):
                knots[0] = apply_move[line[0]](knots[0])

                for h in range(n_knots - 1):
                    if not are_adjacent(knots[h], knots[h + 1]):
                        knots[h + 1] += get_move(knots[h], knots[h + 1])

                visited.add(tuple(knots[-1]))

        return len(visited)


# Execute the two problems solutions
print("Result to problem 1: ", problem1())
print("Result to problem 2: ", problem2())

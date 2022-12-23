import numpy as np


# Function to read the board
def read_board(file):
    margin = 100  # Arbitrary margin to ease the board expansion
    board = np.array([list(line.strip()) for line in file])

    # Horizontal expansion
    empty = np.array([['.'] for _ in range(board.shape[0])])
    for _ in range(margin):
        board = np.c_[empty, board, empty]

    # Vertical expansion
    empty = np.transpose(np.array([['.'] for _ in range(board.shape[1])]))
    for _ in range(margin):
        board = np.r_[empty, board, empty]

    return board


# Function to calculate the cell proposed by an elf
def get_proposal(elf, board, order):
    # Check if there is any elf in the adjacent cells
    adjacent_positions = [(elf[0] + x, elf[1] + y) for x in range(-1, 2) for y in range(-1, 2) if (x, y) != (0, 0)]

    if '#' not in [board[position] for position in adjacent_positions]:
        return -1

    # Generate possible proposals
    north_positions = [(elf[0] - 1, elf[1] + x) for x in range(-1, 2)]
    south_positions = [(elf[0] + 1, elf[1] + x) for x in range(-1, 2)]
    west_positions = [(elf[0] + x, elf[1] - 1) for x in range(-1, 2)]
    east_positions = [(elf[0] + x, elf[1] + 1) for x in range(-1, 2)]

    positions = [north_positions, south_positions, west_positions, east_positions]
    returns = [(elf[0] - 1, elf[1]), (elf[0] + 1, elf[1]), (elf[0], elf[1] - 1), (elf[0], elf[1] + 1)]

    # Iterate positions in the given order
    for i in order:
        if '#' not in [board[position] for position in positions[i]]:
            return returns[i]

    return -1


# Function to perform a round and check if any elf is moving
def perform_round(board, round_number):
    order = [(pos + round_number) % 4 for pos in [0, 1, 2, 3]]
    elves_proposals = {}
    proposals_count = {}
    moving = False

    elves = np.transpose(np.where(board == '#'))

    # First half: get proposals
    for elf in elves:
        proposal = get_proposal(elf, board, order)

        if proposal != -1:
            elves_proposals[tuple(elf)] = proposal
            if proposal in proposals_count:
                proposals_count[proposal] += 1
            else:
                proposals_count[proposal] = 1

    # Second half: apply proposals if there is no collision
    for elf in elves_proposals.keys():
        proposal = elves_proposals[tuple(elf)]
        if proposals_count[proposal] < 2:
            board[elf] = '.'
            board[proposal] = '#'
            moving = True

    return moving


# Solution to Problem 1
def problem1():
    with open("data/input23.txt") as file:
        board = read_board(file)

        for round in range(10):
            perform_round(board, round)

        elves = np.transpose(np.where(board == '#'))
        shape = np.amax(elves, axis=0) - np.amin(elves, axis=0)
        return (shape[0] + 1) * (shape[1] + 1) - elves.shape[0]


# Solution to Problem 2
def problem2():
    with open("data/input23.txt") as file:
        board = read_board(file)
        round = 0

        while perform_round(board, round):
            round += 1

        return round + 1


# Execute the two problems solutions
print("Result to problem 1: ", problem1())
print("Result to problem 2: ", problem2())

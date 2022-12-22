import numpy as np

# Dictionary to rotate direction
rotation = {
    'R': lambda x: (x + 1) % 4,
    'L': lambda x: (x - 1) % 4
}

# Dictionary to translate the direction id to the actual direction (string)
direction_string = {
    0: '>',
    1: 'v',
    2: '<',
    3: '^'
}

# Dictionary to move in the board
move = {
    0: lambda row, col: (row, col + 1),
    1: lambda row, col: (row + 1, col),
    2: lambda row, col: (row, col - 1),
    3: lambda row, col: (row - 1, col)
}


# Function to read the monkey's notes
def read_notes(file):
    board = []
    path = []
    reading_board = True
    for line in file:
        if not line.strip():
            max_len = 0
            for row in board:
                max_len = max(max_len, len(row))

            for row in board:
                row += [' '] * (max_len - len(row))

            reading_board = False
            continue

        if reading_board:
            board.append(list(line[:-1]))
        else:
            current_string = ''
            for char in line.strip():
                if char.isnumeric():
                    current_string += char
                else:
                    if current_string:
                        path.append(int(current_string))
                        current_string = ''

                    path.append(char)

            if current_string:
                path.append(int(current_string))

    return np.array(board), path


# Function to check if a position is valid
def is_valid_position(board, new_position):
    return 0 <= new_position[0] < board.shape[0] and 0 <= new_position[1] < board.shape[1] and board[
        new_position] != ' '


# Function to handle the not valid position in a 2D board
def wrap_around(board, current_direction, position):
    if current_direction == 0:
        new_position = (position[0], 0)
    elif current_direction == 1:
        new_position = (0, position[1])
    elif current_direction == 2:
        new_position = (position[0], board.shape[1] - 1)
    else:
        new_position = (board.shape[0] - 1, position[1])

    while board[new_position] == ' ':
        new_position = move[current_direction](*new_position)

    return new_position, current_direction


# Function to handle the not valid position when the board is a cube
def proceed_around_the_cube(board, current_direction, position):
    previous_row, previous_col = position
    row, col = 0, 0
    new_direction = 0

    # Fold 2 to 5
    if previous_col == 150:
        row = 149 - previous_row
        col = 99
        new_direction = 2

    # Fold 3 to 2
    elif previous_col == 100 and (50 <= previous_row < 100):
        row = 49
        col = 50 + previous_row
        new_direction = 3

    # Fold 5 to 6
    elif previous_row == 150 and (50 <= previous_col < 100):
        row = previous_col + 100
        col = 49
        new_direction = 2

    # Fold 6 to 1
    elif previous_col == -1 and (150 <= previous_row < 200):
        row = 0
        col = previous_row - 100
        new_direction = 1

    # Fold 4 to 1
    elif previous_col == -1 and (100 <= previous_row < 150):
        col = 50
        row = 149 - previous_row
        new_direction = 0

    # Fold 4 to 3
    elif previous_row == 99 and (0 <= previous_col < 50):
        col = 50
        row = previous_col + 50
        new_direction = 0

    # Fold 6 to 2
    elif previous_row == 200 and (0 <= previous_col < 50):
        row = 0
        col = previous_col + 100
        new_direction = 1

    # Fold 5 to 2
    elif previous_col == 100 and (100 <= previous_row < 150):
        row = 149 - previous_row
        col = 149
        new_direction = 2

    # Fold 2 to 3
    elif previous_row == 50 and (100 <= previous_col < 150):
        row = previous_col - 50
        col = 99
        new_direction = 2

    # Fold 6 to 5
    elif previous_col == 50 and (150 <= previous_row < 200):
        row = 149
        col = previous_row - 100
        new_direction = 3

    # Fold 1 to 6
    elif previous_row == -1 and (50 <= previous_col < 100):
        col = 0
        row = previous_col + 100
        new_direction = 0

    # Fold 1 to 4
    elif previous_col == 49 and (0 <= previous_row < 50):
        col = 0
        row = 149 - previous_row
        new_direction = 0

    # Fold 3 to 4
    elif previous_col == 49 and (50 <= previous_row < 100):
        row = 100
        col = previous_row - 50
        new_direction = 1

    # Fold 2 to 6
    elif previous_row == -1 and (100 <= previous_col < 150):
        row = 199
        col = previous_col - 100
        new_direction = 3

    return (row, col), new_direction


# Function to follow the path in the board given a function to handle the not valid positions
def follow_path(board, path, move_dimension):
    row_size = board.shape[0]

    # Find the starting position
    current_position = (0, 0)
    for i in range(row_size):
        if board[0, i] == '.':
            current_position = (0, i)
            break

    current_direction = 0

    for step in path:
        if type(step) == int:
            for _ in range(step):
                # Move in the current direction
                new_position = move[current_direction](*current_position)
                new_direction = current_direction
                board[current_position] = direction_string[current_direction]

                # If we go out of the board, we wrap around
                if not is_valid_position(board, new_position):
                    new_position, new_direction = move_dimension(board, current_direction, new_position)

                # If we hit a wall, we stop
                if board[new_position] == '#':
                    break
                else:
                    current_position = new_position
                    current_direction = new_direction

        else:
            current_direction = rotation[step](current_direction)

    return current_position[0], current_position[1], current_direction


# Function to print the board
def print_board(board):
    for row in board:
        print(row)


# Solution to Problem 1
def problem1():
    with open("data/input22.txt") as file:
        board, path = read_notes(file)

        row, col, dir = follow_path(board, path, wrap_around)

        return 1000 * (row + 1) + 4 * (col + 1) + dir


# Solution to Problem 2
def problem2():
    with open("data/input22.txt") as file:
        board, path = read_notes(file)

        row, col, dir = follow_path(board, path, proceed_around_the_cube)

        return 1000 * (row + 1) + 4 * (col + 1) + dir


# Execute the two problems solutions
print("Result to problem 1: ", problem1())
print("Result to problem 2: ", problem2())

# Function to mix the encrypted sequence
def mix_sequence(sequence):
    length = len(sequence)
    for previous_pos in range(length):

        current_pos = [i for i in range(length) if sequence[i][0] == previous_pos][0]
        element = sequence[current_pos]
        movement = sequence[current_pos][1]
        new_pos = (current_pos + movement)

        if new_pos >= length:
            extra = (movement - (length - current_pos)) // (length - 1) + 1
            new_pos = (new_pos + extra) % length
        if new_pos <= 0 and new_pos != current_pos:
            extra = (abs(movement) - current_pos) // (length - 1) + 1
            new_pos = (new_pos - extra) % length

        sequence.pop(current_pos)
        sequence.insert(new_pos, element)


# Function to add the coordinates of the grove
def add_grove_coordinates(sequence):
    length = len(sequence)
    current_pos = [i for i in range(length) if sequence[i][1] == 0][0]
    a = (current_pos + 1000) % length
    b = (current_pos + 2000) % length
    c = (current_pos + 3000) % length

    return sequence[a][1] + sequence[b][1] + sequence[c][1]


# Solution to Problem 1
def problem1():
    with open("data/input20.txt") as file:
        sequence = [(i, int(line.strip())) for i, line in enumerate(file)]
        mix_sequence(sequence)

        return add_grove_coordinates(sequence)


# Solution to Problem 2
def problem2():
    with open("data/input20.txt") as file:
        sequence = [(i, int(line.strip()) * 811589153) for i, line in enumerate(file)]

        for _ in range(10):
            mix_sequence(sequence)

        return add_grove_coordinates(sequence)


# Execute the two problems solutions
print("Result to problem 1: ", problem1())
print("Result to problem 2: ", problem2())

# Solution to Day 5 using stacks and queues
from collections import deque


# Function to read the initial data of all the stacks
def read_initial_stacks(file):
    # Process first line and check the number of queues
    level_elements = file.readline()[1::4]
    queues = [deque() for _ in range(len(level_elements))]

    # Auxiliary function to push all elements of a level
    def push_to_queues(elements):
        for queue, element in zip(queues, elements):
            if element != ' ':
                queue.append(element)

    push_to_queues(level_elements)

    # Process the rest of the lines
    finished = False
    while not finished:
        level_elements = file.readline()[1::4]

        # Check if the line is the last one
        if level_elements[0] == '1':
            finished = True
        else:  # Push each element to the corresponding queue
            push_to_queues(level_elements)

    return queues


# Function to read a move line
def read_move(line, queues):
    move = line.strip().split(' ')[1::2]
    repetitions = int(move[0])
    source = queues[int(move[1]) - 1]
    destination = queues[int(move[2]) - 1]

    return repetitions, source, destination


# Solution to Problem 1
def problem1():
    with open("data/input5.txt") as file:

        queues = read_initial_stacks(file)
        file.readline()

        for line in file:
            repetitions, source, destination = read_move(line, queues)

            for i in range(repetitions):
                destination.appendleft(source.popleft())

        return [queue[0] for queue in queues]


# Solution to Problem 2
def problem2():
    with open("data/input5.txt") as file:
        queues = list(read_initial_stacks(file))
        file.readline()

        for line in file:
            repetitions, source, destination = read_move(line, queues)

            elements = [source.popleft() for _ in range(repetitions)]
            while elements:
                destination.appendleft(elements.pop())

        return [queue[0] for queue in queues]


# Execute the two problems solutions
print("Result to problem 1: ", problem1())
print("Result to problem 2: ", problem2())

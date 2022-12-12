import numpy as np


# Solution to Problem 1
def problem1():
    with open("data/input08.txt") as file:
        data = np.matrix([[int(x) for x in line.strip()] for line in file])

        # Count borders
        counter = 2 * (data.shape[0] + (data.shape[1] - 2))

        # Itereate matrix skipping borders
        for row in range(1, data.shape[0] - 1):
            for col in range(1, data.shape[1] - 1):
                counter += np.all(data[:row, col] < data[row, col]) or np.all(
                    data[row + 1:, col] < data[row, col]) or np.all(
                    data[row, :col] < data[row, col]) or np.all(
                    data[row, col + 1:] < data[row, col])

        return counter


# Solution to Problem 2
def problem2():
    with open("data/input08.txt") as file:
        data = np.matrix([[int(x) for x in line.strip()] for line in file])

        highest_score = 0
        # Itereate matrix
        for row in range(data.shape[0]):
            for col in range(data.shape[1]):
                scores = np.array([0, 0, 0, 0])

                # Iterate up
                for k in range(row - 1, -1, -1):
                    scores[0] += 1
                    if data[k, col] >= data[row, col]:
                        break
                # Iterate down
                for k in range(row + 1, data.shape[0]):
                    scores[1] += 1
                    if data[k, col] >= data[row, col]:
                        break
                # Iterate left
                for k in range(col - 1, -1, -1):
                    scores[2] += 1
                    if data[row, k] >= data[row, col]:
                        break
                # Iterate right
                for k in range(col + 1, data.shape[1]):
                    scores[3] += 1
                    if data[row, k] >= data[row, col]:
                        break

                highest_score = max(highest_score, np.prod(scores))

        return highest_score


# Execute the two problems solutions
print("Result to problem 1: ", problem1())
print("Result to problem 2: ", problem2())

# Function to count letters from a stream until a sequences without repetition is found
def count_letters_until_no_repetition(file, length):
    last_letters = file.read(length)
    reads = length
    letter = last_letters[-1]

    while letter and len(set(last_letters)) != length:
        letter = file.read(1)
        last_letters = last_letters[1:] + letter
        reads += 1

    return reads


# Solution to Problem 1
def problem1():
    with open("data/input06.txt") as file:
        return count_letters_until_no_repetition(file, 4)


# Solution to Problem 2
def problem2():
    with open("data/input06.txt") as file:
        return count_letters_until_no_repetition(file, 14)


# Execute the two problems solutions
print("Result to problem 1: ", problem1())
print("Result to problem 2: ", problem2())

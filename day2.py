# Dictionary to determine the score to each possible result:
#   0: Tie (3 points)
#   1: Lose (0 point)
#   2: Win (6 points)
resultingScore = {0: 3, 1: 0, 2: 6}


# Function to map a letter to a number given a base letter
def letter2number(letter, base):
    return ord(letter) - ord(base)


# Function to get the score of a game
def get_score(oponent_choice, your_choice):
    return your_choice + resultingScore[(oponent_choice - your_choice) % 3] + 1


# Function to get the required move given the oponent's move and the required result
def get_move(oponent_choice, required_result):
    return (oponent_choice + required_result - 1) % 3


# Solution to Problem 1
def problem1():
    with open("data/input2.txt") as file:
        score = 0
        for line in file:
            game = line.strip().split()
            score += get_score(letter2number(game[0], 'A'), letter2number(game[1], 'X'))

    return score


# Solution to Problem 2
def problem2():
    with open("data/input2.txt") as file:
        score = 0
        for line in file:
            game = line.strip().split()
            oponent_choice = letter2number(game[0], 'A')
            your_choice = get_move(oponent_choice, letter2number(game[1], 'X'))
            score += get_score(oponent_choice, your_choice)

    return score


# Execute the two problems solutions
print("Result to problem 1: ", problem1())
print("Result to problem 2: ", problem2())

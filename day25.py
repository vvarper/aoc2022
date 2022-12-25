# Function to read the snafu numbers
def read_snafu(file):
    return [line.strip() for line in file.readlines()]


# Dictionary to convert symbols to numbers
symbol_to_number = {
    '2': 2,
    '1': 1,
    '0': 0,
    '-': -1,
    '=': -2
}


# Function to convert a snafu number to a normal number
def snafu_to_normal(snafu):
    number = 0
    for i, c in enumerate(reversed(snafu)):
        number += symbol_to_number[c] * (5 ** i)

    return number


# List to convert the result of the modulo operation to the next symbol
mod_to_symbol = ['0', '1', '2', '=', '-']


# Function to convert a normal number to a snafu number
def normal_to_snafu(number):
    snafu = ''
    while number > 0:
        next_symbol = mod_to_symbol[number % 5]
        number //= 5

        if next_symbol == '-' or next_symbol == '=':
            number += 1

        snafu = next_symbol + snafu

    return snafu


# Solution to Problem 1
def problem1():
    with open("data/input25.txt") as file:
        snafu_numbers = read_snafu(file)

        return normal_to_snafu(sum([snafu_to_normal(snafu) for snafu in snafu_numbers]))


# Execute the two problems solutions
print("Result to problem 1: ", problem1())

# Solution to Problem 1
def problem1():
    with open("data/input1.txt") as file:
        max_calories = 0
        current_calories = 0

        # Read the file line by line to store only the calories of the current Elf 
        # and the highest amount so far
        for line in file:

            # If the line is not empty, add the calories to the current Elf
            if line.strip():
                current_calories += int(line)

            # If the line is empty, we have read all the calories of the current Elf,
            # so we have to update the maximum
            else:
                max_calories = max(current_calories, max_calories)
                current_calories = 0

        # Check the last Elf, since the file does not end with an empty line 
        # and therefores is not processed in the previous loop
        max_calories = max(current_calories, max_calories)

    return max_calories


# Solution to Problem 2
def problem2():
    with open("data/input1.txt") as file:
        three_max_calories = [0, 0, 0]
        min_max_calories = 0
        current_calories = 0

        # Read the file line by line to store only the calories of the current Elf 
        # and the three highest amounts so far
        for line in file:

            # If the line is not empty, add the calories to the current Elf
            if line.strip():
                current_calories += int(line)

            # If the line is empty, we have read all the calories of the current Elf,
            # so we have to update the three maximum comparing the current value
            # the minimum of the three
            else:
                three_max_calories[three_max_calories.index(min_max_calories)] = max(current_calories, min_max_calories)
                min_max_calories = min(three_max_calories)
                current_calories = 0

    # Check the last Elf, since the file does not end with an empty line
    # and therefores is not processed in the previous loop
    three_max_calories[three_max_calories.index(min_max_calories)] = max(current_calories, min_max_calories)

    return sum(three_max_calories)


# Execute the two problems solutions
print("Result to problem 1: ", problem1())
print("Result to problem 2: ", problem2())

from itertools import islice


# Function to get the priority value of an item
def get_priority(item):
    return ord(item) - (ord('A') - 27 if item < 'a' else ord('a') - 1)


# Solution to Problem 1
def problem1():
    with open("data/input03.txt") as file:
        priority_sum = 0

        # Each line is a rucksack
        for line in file:
            rucksack = line.strip()
            middle = len(rucksack) // 2

            # We split the rucksack in its two compartments
            compartment1 = rucksack[:middle]
            compartment2 = rucksack[middle:]

            # We find the item that is in both compartment and get its priority
            for item in compartment1:
                if item in compartment2:
                    priority_sum += get_priority(item)
                    break
    return priority_sum


# Solution to Problem 2
def problem2():
    with open("data/input03.txt") as file:

        priority_sum = 0

        # We iterate the file in chunks of 3 lines to process each group
        for group in iter(lambda: list(islice(file, 3)), []):
            rucksack1, rucksack2, rucksack3 = [rucksack.strip() for rucksack in group]

            # We find the item that is in the three rucksacks and get its priority
            for letter in rucksack1.strip():
                if letter in rucksack2 and letter in rucksack3:
                    priority_sum += get_priority(letter)
                    break
    return priority_sum


# Execute the two problems solutions
print("Result to problem 1: ", problem1())
print("Result to problem 2: ", problem2())

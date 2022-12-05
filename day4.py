# Function to check if a range (range1) is contained in another (range2)
def is_contained(range1, range2):
    return int(range1[0]) >= int(range2[0]) and int(range1[1]) <= int(range2[1])


# Function to check if two ranges overlap
def are_overlapped(range1, range2):
    return min(int(range1[1]), int(range2[1])) - max(int(range1[0]), int(range2[0])) >= 0


# Solution to Problem 1
def problem1():
    with open("data/input4.txt") as file:
        containments = 0
        for line in file:  # linea
            elf1, elf2 = [elf.split('-') for elf in line.strip().split(',')]

            containments += is_contained(elf1, elf2) or is_contained(elf2, elf1)

    return containments


# Solution to Problem 2
def problem2():
    with open("data/input4.txt") as file:
        overlaps = 0
        for line in file:  # linea
            elf1, elf2 = [elf.split('-') for elf in line.strip().split(',')]

            overlaps += are_overlapped(elf1, elf2)

    return overlaps


# Execute the two problems solutions
print("Result to problem 1: ", problem1())
print("Result to problem 2: ", problem2())

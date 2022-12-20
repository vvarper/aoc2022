# Solution to Problem 1
def problem1():
    with open("data/input18.txt") as file:
        cubes = [[int(value) for value in line.strip().split(',')] for line in file]
        total_free = 0

        for cube in cubes:
            for i in range(len(cube)):
                j = (i + 1) % len(cube)
                k = (i + 2) % len(cube)
                free = 2
                for other_cube in cubes:
                    if cube != other_cube and cube[j] == other_cube[j] and cube[k] == other_cube[k] and abs(
                            cube[i] - other_cube[i]) == 1:
                        free -= 1
                        if free == 0:
                            break
                total_free += free

        return total_free


# Execute the problem solution
print("Result to problem 1: ", problem1())

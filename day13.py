import ast
import functools


# Recursive function to compare two packages
# Returns 1 if package1 > package2
# Returns -1 if package1 < package2
# Returns 0 if package1 == package2
def compare_packages(package1, package2):
    # go through the elements recursively
    for item1, item2 in zip(package1, package2):
        p1_int = isinstance(item1, int)
        p2_int = isinstance(item2, int)
        p1_list = isinstance(item1, list)
        p2_list = isinstance(item2, list)

        # Direct comparison if both items are integers
        if p1_int and p2_int:
            if item1 > item2:
                return 1
            elif item1 < item2:
                return -1

        # If one of the items is a list, call the function recursively
        elif p1_list or p2_list:
            if p1_int:
                item1 = [item1]
            if p2_int:
                item2 = [item2]

            result = compare_packages(item1, item2)
            if result != 0:
                return result

    return 1 if len(package1) > len(package2) else -1 if len(package1) < len(package2) else 0


# Solution to Problem 1
def problem1():
    with open("data/input13.txt") as file:
        result = 0
        idx = 1
        current_pair = []
        for line in file:
            line = line.strip()
            if line:
                current_pair.append(ast.literal_eval(line))
            else:
                if compare_packages(current_pair[0], current_pair[1]) != 1:
                    result += idx
                current_pair = []
                idx += 1

        return result


# Solution to Problem 2
def problem2():
    with open("data/input13.txt") as file:
        packages = []
        for line in file:
            line = line.strip()
            if line:
                packages.append(ast.literal_eval(line))

        packages.append([[2]])
        packages.append([[6]])
        packages.sort(key=functools.cmp_to_key(compare_packages))

        first = packages.index([[2]]) + 1
        second = packages.index([[6]]) + 1

        return first * second


# Execute the two problems solutions
print("Result to problem 1: ", problem1())
print("Result to problem 2: ", problem2())

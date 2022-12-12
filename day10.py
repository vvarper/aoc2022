# Solution to Problem 1
def problem1():
    cycle = 1
    X = 1
    interesting_cycle = 20
    sum = 0
    with open("data/input10.txt") as file:
        for line in file:
            line = line.strip().split()
            cycle += 1

            if cycle == interesting_cycle:
                sum += X * interesting_cycle
                if interesting_cycle < 220:
                    interesting_cycle += 40
                else:
                    break

            if line[0] == 'addx':
                X += int(line[1])
                cycle += 1

                if cycle == interesting_cycle:
                    sum += X * interesting_cycle
                    if interesting_cycle < 220:
                        interesting_cycle += 40
                    else:
                        break

        return sum


# Function to print the CRT (matrix)
def print_crt(crt):
    for row in crt:
        print(row)


# Function to get the CRT position corresponding to a cycle
def get_crt_pos(cycle):
    return int((cycle - 1) // 40), int((cycle - 1) % 40)


# Solution to Problem 2
def problem2():
    crt = [[0 for x in range(40)] for y in range(6)]
    cycle = 1
    X = 1

    with open("data/input10.txt") as file:
        for line in file:
            line = line.strip().split()

            pos = get_crt_pos(cycle)
            crt[pos[0]][pos[1]] = '#' if abs(pos[1] - X) < 2 else '.'

            cycle += 1

            if line[0] == 'addx':
                pos = get_crt_pos(cycle)
                crt[pos[0]][pos[1]] = '#' if abs(pos[1] - X) < 2 else '.'

                X += int(line[1])
                cycle += 1

        return crt


# Execute the two problems solutions
print("Result to problem 1: ", problem1())
print_crt(problem2())

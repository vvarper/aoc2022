from sympy import symbols, solve


# Function to read the input file and build the monkeys' jobs
def read_monkeys(file):
    monkeys = {}
    for line in file:
        line = line.strip().split(':')
        job = line[1].strip().split()

        if len(job) == 1:
            job = int(job[0])

        monkeys[line[0]] = job

    return monkeys


# Recursive function to evaluate the monkey's job
def yell_number(monkeys, monkey):
    operation = monkeys[monkey]
    if type(operation) == int:
        return operation
    elif operation[1] == '+':
        return yell_number(monkeys, operation[0]) + yell_number(monkeys, operation[2])
    elif operation[1] == '*':
        return yell_number(monkeys, operation[0]) * yell_number(monkeys, operation[2])
    elif operation[1] == '-':
        return yell_number(monkeys, operation[0]) - yell_number(monkeys, operation[2])
    else:
        return yell_number(monkeys, operation[0]) / yell_number(monkeys, operation[2])


# Recursive function to build the complete expression corresponding to the monkey's job
def build_expr(monkeys, monkey):
    if monkey == 'humn':
        return 'x'

    operation = monkeys[monkey]
    if type(operation) == int:
        return str(operation)
    else:
        return '(' + build_expr(monkeys, operation[0]) + ' ' + operation[1] + ' ' + build_expr(monkeys,
                                                                                               operation[2]) + ')'


# Solution to Problem 1
def problem1():
    with open("data/input21.txt") as file:
        monkeys = read_monkeys(file)

        return yell_number(monkeys, 'root')


# Solution to Problem 2
def problem2():
    with open("data/input21.txt") as file:
        monkeys = read_monkeys(file)

        x = symbols('x')
        expr = eval(build_expr(monkeys, monkeys['root'][0])) - eval(build_expr(monkeys, monkeys['root'][2]))

        return solve(expr)[0]


# Execute the two problems solutions
print("Result to problem 1: ", problem1())
print("Result to problem 2: ", problem2())

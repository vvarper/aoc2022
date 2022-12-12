# Class to represent a monkey and its operations
class Monkey:
    # Constructor
    def __init__(self, starting_items, operation, test, relief):
        self.items = starting_items
        self.factor = operation[1]
        if self.factor == 'old':
            self.operation = lambda x: operation[0](x, x)
        else:
            self.factor = int(self.factor)
            self.operation = lambda x: operation[0](x, self.factor)

        self.test = test[0]
        self.positive = test[1]
        self.negative = test[2]
        self.relief = relief
        self.inspects = 0

    # Method to check if the monkey has any items left
    def has_items(self):
        return len(self.items) > 0

    # Method to add an item to the monkey's inventory
    def add_item(self, item):
        self.items.append(item)

    # Method to inspect an item. Return its new value and the new target monkey
    def inspect(self):
        self.inspects += 1
        item = (self.operation(self.items.pop(0)) // self.relief) % self.overflow_limit
        monkey = self.positive if item % self.test == 0 else self.negative

        return item, monkey


def read_monkeys(file, relief):
    monkeys = []
    items = []
    operation = test = positive = factor = None
    overflow_limit = 1
    for line in file:
        line = line.strip().replace(',', '').split()
        if line:
            if line[0] == 'Starting':
                items = [int(item) for item in line[2:]]
            elif line[0] == 'Operation:':
                if line[4] == '+':
                    operation = lambda x, y: x + y
                    factor = line[5]
                else:
                    operation = lambda x, y: x * y
                    factor = line[5]
            elif line[0] == 'Test:':
                test = int(line[3])
                overflow_limit *= test
            elif line[1] == 'true:':
                positive = int(line[5])
            elif line[1] == 'false:':
                negative = int(line[5])
                monkeys.append(Monkey(items, (operation, factor), (test, positive, negative), relief))

    for monkey in monkeys:
        monkey.overflow_limit = overflow_limit

    return monkeys


# Solution to Problem 1
def problem1():
    with open("data/input11.txt") as file:
        monkeys = read_monkeys(file, 3)

        for _ in range(20):
            for monkey in monkeys:
                while monkey.has_items():
                    item, obj_monkey = monkey.inspect()
                    monkeys[obj_monkey].add_item(item)

        max_inspections = sorted([monkey.inspects for monkey in monkeys])
        return max_inspections[-2] * max_inspections[-1]


# Solution to Problem 2
def problem2():
    with open("data/input11.txt") as file:
        monkeys = read_monkeys(file, 1)

        for _ in range(10000):
            for monkey in monkeys:
                while monkey.has_items():
                    item, obj_monkey = monkey.inspect()
                    monkeys[obj_monkey].add_item(item)

        max_inspections = sorted([monkey.inspects for monkey in monkeys])
        return max_inspections[-2] * max_inspections[-1]


# Execute the two problems solutions
print("Result to problem 1: ", problem1())
print("Result to problem 2: ", problem2())

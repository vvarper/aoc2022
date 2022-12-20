import networkx as nx
from queue import PriorityQueue

shortest_paths = None
rates = None
max_steps = 30
start_node = 'AA'


# Function to evaluate a path solution
def evaluate_solution(path):
    global shortest_paths, max_steps, rates, start_node

    current_pressure = 0
    remaining_steps = max_steps
    previous_node = start_node

    for node in path:
        if node == previous_node:
            remaining_steps -= 1
        else:
            remaining_steps -= (len(shortest_paths[previous_node][node]))

        if remaining_steps > 0:
            current_pressure += remaining_steps * rates[node]

        previous_node = node

    return current_pressure


# Function to build a greedy solution
def greedy_solution(interesting_valves):
    global start_node

    solution = []

    while len(interesting_valves) > len(solution):
        best_valve = None
        best_pressure = 0
        for valve in interesting_valves:
            if valve not in solution:
                pressure = evaluate_solution(solution + [valve])
                if pressure > best_pressure:
                    best_valve = valve
                    best_pressure = pressure

        solution += [best_valve]

    return solution


# Function to read valves info from file
def read_valves(file):
    rates = {}
    connections = {}

    for line in file:
        line = line.strip().split()
        valve = line[1]
        rates[valve] = int(line[4].split('=')[1][:-1])
        connections[valve] = ' '.join(line[9:]).split(', ')

    return rates, connections


# Class to represent a solution for a branch and bound algorithm
class Solution:
    # Constructor to build an empty solution
    def __init__(self, remaining_steps, available_nodes):
        self.path = []
        self.remaining_steps = remaining_steps
        self.available_nodes = available_nodes
        self.f = 0
        self.__calculate_max_estimate()

    # Method to compare two solutions
    def __lt__(self, other):
        return self.local_bound() < other.local_bound()

    # Method to calculate the maximum estimate for a solution
    def __calculate_max_estimate(self):
        global rates

        available_rates = sorted([rates[node] for node in self.available_nodes], reverse=True)
        self.max_estimate = 0
        remaining_steps = self.remaining_steps

        for rate in available_rates:
            remaining_steps -= 2
            if remaining_steps > 0:
                self.max_estimate += remaining_steps * rate

    # Method to expand a solution
    def add(self, node):
        global shortest_paths, rates

        new_solution = Solution(self.remaining_steps, self.available_nodes.copy())

        # Update path and available nodes
        new_solution.path = self.path + [node]
        new_solution.available_nodes.remove(node)

        # Update ramaining steps
        last_node = self.path[-1] if self.path else start_node
        new_solution.remaining_steps -= len(shortest_paths[last_node][node])

        # Update f
        new_solution.f = self.f
        if new_solution.remaining_steps > 0:
            new_solution.f += new_solution.remaining_steps * rates[node]

        # Update max estimate
        new_solution.__calculate_max_estimate()

        return new_solution

    # Method to check if a solution is complete
    def is_complete(self):
        return len(self.available_nodes) == 0

    # Method get the local max bound of a solution
    def local_bound(self):
        return self.f + self.max_estimate


# Solution to Problem 1
def problem1():
    with open("data/input16.txt") as file:
        global shortest_paths, rates, max_steps, start_node

        rates, connections = read_valves(file)

        # Build a graph with the connections
        graph = nx.Graph()
        graph.add_nodes_from(connections.keys())
        for node, connections in connections.items():
            for connection in connections:
                graph.add_edge(node, connection)

        # Get the shortest paths between all nodes and the valves with rate not 0
        shortest_paths = dict(nx.all_pairs_shortest_path(graph))
        interesting_valves = [rate[0] for rate in rates.items() if rate[1] != 0]

        # Create a greedy solution as a starting point
        initial_solution = greedy_solution(interesting_valves)
        global_bound = evaluate_solution(initial_solution)

        # Create a priority queue to store the solution and add an empty one
        q = PriorityQueue()
        q.put(Solution(max_steps, interesting_valves))

        # Branch and bound algorithm
        while True:
            solution = q.get()

            for node in solution.available_nodes:
                next_solution = solution.add(node)
                evaluation = next_solution.local_bound()

                if next_solution.is_complete() and evaluation > global_bound:
                    global_bound = evaluation
                elif evaluation > global_bound:
                    q.put(next_solution)

            if q.empty() or q.queue[0].local_bound() < global_bound:
                break

        return global_bound


# Execute the problem solution
print("Result to problem 1: ", problem1())

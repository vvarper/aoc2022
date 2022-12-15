# Function to calculate the Manhattan distance between two points
def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# Function to read sensor info from file
def read_sensors_with_closest_beacons(file):
    sensors = []
    for line in file:
        line = line.strip().split()
        sensor = (int(line[2][:-1].split('=')[1]), int(line[3][:-1].split('=')[1]))
        beacon = (int(line[8][:-1].split('=')[1]), int(line[9].split('=')[1]))
        sensors.append([sensor, beacon, manhattan_distance(sensor, beacon)])

    return sensors


# Function to get the range covered by a sensor in a row
def range_in_row_by_sensor(row, sensor, min_distance, max_threshold=None):
    x_dist = min_distance - abs(row - sensor[1])
    if x_dist < 0:
        return None
    else:
        min_x = sensor[0] - x_dist
        max_x = sensor[0] + x_dist
        if max_threshold:
            min_x = max(min_x, 0)
            max_x = min(max_x, max_threshold)
        return min_x, max_x


# Function to get the ranges covered by different sensors in a row
# The ranges are ordered by the minimum value
def ranges_in_row(row, sensors, distances, max_threshold=None):
    ranges = []

    for sensor, dist in zip(sensors, distances):
        space = range_in_row_by_sensor(row, sensor, dist, max_threshold)
        if space:
            ranges.append(space)

    ranges = sorted(ranges)
    return ranges


# Solution to Problem 1
def problem1():
    with open("data/input15.txt") as file:

        # Read sensors and set the row to check
        data = read_sensors_with_closest_beacons(file)
        sensors = [entry[0] for entry in data]
        distances = [entry[2] for entry in data]
        row = 2000000

        # Get the positions where there is a sensor or a beacon in the row
        sensor_x = set([sensor[0] for sensor in sensors if sensor[1] == row])
        beacon_x = set([entry[1][0] for entry in data if entry[1][1] == row])

        # Get the ranges covered by the sensors in the row
        ranges = ranges_in_row(row, sensors, distances, max_threshold=None)

        # Count the number of positions that are covered by a sensor
        size = 0
        current_max = -float('inf')
        for space in ranges:
            if space[1] > current_max:
                size += space[1] - max(space[0], current_max) + (space[0] > current_max)
            current_max = max(current_max, space[1])

        return size - len(sensor_x) - len(beacon_x)


# Solution to Problem 2
def problem2():
    with open("data/input15.txt") as file:

        # Read sensors and set maximum for x and y
        data = read_sensors_with_closest_beacons(file)
        sensors = [sensor[0] for sensor in data]
        distances = [sensor[2] for sensor in data]
        maximum = 4000000

        # Iterate over all the rows
        for row in range(maximum):
            # Get the ranges covered by the sensors in the row
            ranges = ranges_in_row(row, sensors, distances, max_threshold=None)

            # Check if some point is not covered by any sensor
            current_max = 0
            for space in ranges:
                if space[0] > current_max:
                    break
                current_max = max(current_max, space[1])

            if current_max < maximum:
                x = current_max + 1
                return x * 4000000 + row

        return -1


# Execute the two problems solutions
print("Result to problem 1: ", problem1())
print("Result to problem 2: ", problem2())

# Dummy class to store the info of a folder
class folder:
    def __init__(self):
        self.files = {}  # Dictionary of files (name: size)
        self.subfolders = set()  # Set of subfolders (name)
        self.space = 0  # Total space used by the folder and its subfolders


# Recursive function to calculate the space used by a folder and its subfolders
def calculate_space(folders, current_folder):
    folders[current_folder].space = sum(folders[current_folder].files.values())

    for subfolder in folders[current_folder].subfolders:
        folders[current_folder].space += calculate_space(folders, subfolder)

    return folders[current_folder].space


# Function to load the filesystem data from a file
def load_filesystem_data(file):
    folders = {}  # Dictionary of folders (name: folder data)
    current_folder = ""  # Name of the current folder

    # 1. Read the file line by line to store the basic data of the filesystem
    for line in file:
        line = line.strip().split()

        # Movement to another directory
        if line[1] == "cd":
            if line[2] == "..":  # Go to the parent directory
                current_folder = current_folder.rsplit('/', 2)[0] + "/"
            elif line[2] == "/":  # Go to the root directory
                current_folder = "/"
            else:  # Go to a subdirectory
                current_folder += line[2] + "/"

            # If the directory doesn't exist, create it
            if not current_folder in folders:
                folders[current_folder] = folder()

        # Create a subfolder in the current folder
        elif line[0] == "dir":
            folders[current_folder].subfolders.add(current_folder + line[1] + "/")

        # Create a file in the current folder
        elif line[1] != "ls" and not line[1] in folders[current_folder].files:
            folders[current_folder].files[line[1]] = int(line[0])

    # 2. Calculate the space used by each folder and its subfolders
    calculate_space(folders, "/")

    return folders


# Solution to Problem 1
def problem1():
    with open("data/input07.txt") as file:
        folders = load_filesystem_data(file)
        return sum([folders[key].space for key in folders if folders[key].space <= 100000])


# Solution to Problem 2
def problem2():
    with open("data/input07.txt") as file:
        folders = load_filesystem_data(file)

        total_space = 70000000
        update_space = 30000000
        current_space = folders['/'].space
        necessary_space = update_space + current_space - total_space

        return min([folders[key].space for key in folders if folders[key].space >= necessary_space])


# Execute the two problems solutions
print("Result to problem 1: ", problem1())
print("Result to problem 2: ", problem2())

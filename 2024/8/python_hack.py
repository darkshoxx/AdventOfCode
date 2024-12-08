import os
HERE = os.path.dirname(__file__)
print(HERE)
INPUT_FILE = os.path.join(HERE, "input_small.txt")
with open(INPUT_FILE) as my_file:
    input_data = my_file.read()
    input_lines = input_data.split("\n")
print(input_lines.pop())

antenna_locations = {}
height = len(input_lines)
width = len(input_lines[0])
for row, line in enumerate(input_lines):
    for column, entry in enumerate(line):
        if entry != ".":
            if entry in antenna_locations.keys():
                antenna_locations[entry].append([row, column])
            else:
                antenna_locations[entry] = [[row, column]]

def add_antinode(antinode, antinode_locations):
    if (0 <= antinode[0] < height) and (0 <= antinode[1] < width):
        if antinode not in antinode_locations:
            antinode_locations.append(antinode)
    return antinode_locations

        
print(antenna_locations)
antinode_locations = []
for _, locations in antenna_locations.items():
    for first in range(len(locations)-1):
        for second in range(first+1, len(locations)):
            dx = locations[second][0] - locations[first][0]
            dy = locations[second][1] - locations[first][1]
            first_antenna = [None, None]
            first_antenna[0] = locations[second][0]+dx
            first_antenna[1] = locations[second][1]+dy
            second_antenna = [None, None]
            second_antenna[0] = locations[first][0]-dx
            second_antenna[1] = locations[first][1]-dy

            antinode_locations = add_antinode(first_antenna, antinode_locations)
            antinode_locations = add_antinode(second_antenna, antinode_locations)
# print(f"W:{width}, H:{height}")

print(len(antinode_locations))
print(antinode_locations)

# Part 2
def test_gridpoint(location):
    if (0 <= location[0] < height) and (0 <= location[1] < width):
        return True
    return False

def add_tested_antinode(antinode, antinode_locations: list):
    if antinode not in antinode_locations:
        antinode_locations.append(antinode[:])
    return antinode_locations

antinode_locations = []
for _, locations in antenna_locations.items():
    if len(locations)>1:
        for location in locations:
            antinode_locations = add_tested_antinode(location, antinode_locations)
    for first in range(len(locations)-1):
        for second in range(first+1, len(locations)):
            dx = locations[second][0] - locations[first][0]
            dy = locations[second][1] - locations[first][1]

            first_antenna = [None, None]
            first_antenna[0] = locations[second][0]+dx
            first_antenna[1] = locations[second][1]+dy
            while test_gridpoint(first_antenna):
                antinode_locations = add_tested_antinode(first_antenna, antinode_locations)
                first_antenna[0] += dx
                first_antenna[1] += dy 

            second_antenna = [None, None]
            second_antenna[0] = locations[first][0]-dx
            second_antenna[1] = locations[first][1]-dy
            while test_gridpoint(second_antenna):
                antinode_locations = add_tested_antinode(second_antenna, antinode_locations)
                second_antenna[0] -= dx
                second_antenna[1] -= dy


# print(antinode_locations)
# print(f"W:{width}, H:{height}")
# print(len(antinode_locations))

# import os
# HERE = os.path.dirname(__file__)
# print(HERE)
# INPUT_FILE = os.path.join(HERE, "input_small_complete.txt")
# with open(INPUT_FILE) as my_file:
#     input_data = my_file.read()
#     input_lines = input_data.split("\n")
# print(input_lines.pop())

# nodes = []
# height = len(input_lines)
# width = len(input_lines[0])
# for row, line in enumerate(input_lines):
#     for column, entry in enumerate(line):
#         if entry == "#":
#             nodes.append((row, column))
# print(nodes)
# print(len(nodes))

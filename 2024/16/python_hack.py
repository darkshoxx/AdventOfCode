
import os
import re
import math
HERE = os.path.dirname(__file__)
print(HERE)
DRAWFILES = os.path.join(HERE, "drawfiles")
INPUT_FILE = os.path.join(HERE, "input.txt")
with open(INPUT_FILE) as my_file:
    input_data = my_file.read()
    input_lines = input_data.split("\n")
print(input_lines.pop())

new_grid = [list(line) for line in input_lines]
width = len(input_lines[0])
height = len(input_lines)

for row in range(height):
    for column in range(width):
        entry = input_lines[row][column]
        if entry == "S":
            start_x, start_y = column, row
        elif entry == "E":
            end_x, end_y = column, row

def test_outside_grid(x_pos, y_pos):
    return x_pos < 0 or x_pos > width-1 or y_pos<0 or y_pos > height-1

# removing dead ens
directions = {
    "N": (0,-1),
    "S": (0,1),
    "W": (-1,0),
    "E": (1,0)
}

opposite = {
    "N": "S",
    "S": "N",
    "W": "E",
    "E": "W"
}


def plug_dead_ends():
    exit_code = False
    for row in range(height):
        for column in range(width):
            entry = new_grid[row][column]
            if entry == ".":
                neighbours = []
                for _, value in directions.items():
                    new_x, new_y = column + value[0], row + value[1]
                    neighbour_entry = new_grid[new_y][new_x]
                    neighbours.append(neighbour_entry)
                pound_list =  [i for i, val in enumerate(neighbours) if val == "#"]
                if len(pound_list) == 3:
                    exit_code = True
                    new_grid[row][column] = "#"
    return exit_code

still_fixing = True
while still_fixing:
    still_fixing = plug_dead_ends()


print_grid = ["".join(line) for line in new_grid]
drawfile_path = os.path.join(HERE, f"plugged_maze.txt")
with open(drawfile_path, "w") as drawfile:
    drawfile.write("".join("\n".join(print_grid)))                   

def available_directions(pos_x, pos_y, direction):
    neighbours = []
    for cardinal, value in directions.items():
        if cardinal != opposite[direction]:
            new_x, new_y = pos_x + value[0], pos_y + value[1]
            neighbour_entry = new_grid[new_y][new_x]
            if neighbour_entry == ".":
                neighbours.append(((new_x, new_y), cardinal))
    return neighbours

def go_to_next_node(init_x, init_y, cardinal):
    score = 0
    next_node_found = False
    movement = directions[cardinal]
    current_cardinal = cardinal
    cur_x, cur_y = init_x + movement[0], init_y + movement[1]
    score += 1
    while not next_node_found:
        possible = available_directions(cur_x, cur_y, current_cardinal)
        if len(possible) == 1:
            if possible[0][1] == current_cardinal:
                score += 1
            else: 
                score += 1001
            current_cardinal = possible[0][1]
            cur_x, cur_y = possible[0][0]
        else:
            next_node_found = True
    return score, cur_x, cur_y, current_cardinal

print(start_x, start_y)
print(go_to_next_node(start_x, start_y, "E"))


# continue_exploring = True
# while continue_exploring:
#     pass
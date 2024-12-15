
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

grid, instructions = input_data.split("\n\n")
grid_lines = grid.split("\n")
grid_lines = [list(line) for line in grid_lines]
width = len(grid_lines[0])
height = len(grid_lines)

print(height)
print(width)

directions = {
    "^": (0,-1),
    "v": (0,1),
    "<": (-1,0),
    ">": (1,0)
}

for row in range(height):
    for column in range(width):
        if grid_lines[row][column] == "@":
            rob_x = column
            rob_y = row
print(rob_x, rob_y)

def test_for_movement(char):
    dir_x, dir_y = directions[char]
    decision_to_be_made = True
    rob_pos_x, rob_pos_y = rob_x, rob_y
    while decision_to_be_made:
        rob_pos_x, rob_pos_y = dir_x + rob_pos_x, dir_y + rob_pos_y
        entry = grid_lines[rob_pos_y][rob_pos_x]
        if entry == "O":
            continue
        elif entry == ".":
            return True
        elif entry == "#":
            return False
        else:
            raise Exception("How did you get here!??!?!")

def execute_move(char, rob_x, rob_y):
    movement_incomplete = True
    pos_x, pos_y = rob_x, rob_y
    dir_x, dir_y = directions[char]
    old_entry = "."
    while movement_incomplete:
        current_entry = grid_lines[pos_y][pos_x] 
        grid_lines[pos_y][pos_x] = old_entry
        new_pos_x, new_pos_y = dir_x + pos_x, dir_y + pos_y
        new_entry = grid_lines[new_pos_y][new_pos_x] 
        if new_entry == ".":
            movement_incomplete = False
            grid_lines[new_pos_y][new_pos_x] = current_entry
            rob_x, rob_y = dir_x + rob_x, dir_y + rob_y
        else:
            pos_y, pos_x = new_pos_y, new_pos_x
            old_entry = current_entry
    return rob_x, rob_y

number_of_instructions = 0
number_of_moves = 0
for instruction in instructions:
    if instruction in "^v<>":
        number_of_instructions += 1
        move_possible = test_for_movement(instruction)
        if move_possible:
            number_of_moves +=1
            rob_x, rob_y = execute_move(instruction, rob_x, rob_y)


accumulator = 0
for row in range(height):
    for column in range(width):
        if grid_lines[row][column] == "O":
            accumulator += column + row*100
print(accumulator)

# Part 2

grid_lines_2 = grid.split("\n")
the_grid = []
for line in grid_lines_2:
    line_list = []
    for entry in line:
        if entry == "@":
            line_list.append("@")
            line_list.append(".")
        elif entry == "O":
            line_list.append("[")
            line_list.append("]")
        elif entry == ".":
            line_list.append(".")
            line_list.append(".")
        elif entry == "#":
            line_list.append("#")
            line_list.append("#")
        else:
            raise Exception("How did you get here!??!?!")
    the_grid.append(line_list)

g_width = len(the_grid[0])
g_height = len(the_grid)


for row in range(g_height):
    for column in range(g_width):
        if the_grid[row][column] == "@":
            rob_x = column
            rob_y = row
print(rob_x, rob_y)

def test_for_movement_2(char, pos_x, pos_y):
    dir_x, dir_y = directions[char]
    new_pos_x, new_pos_y = pos_x + dir_x, pos_y + dir_y
    entry = the_grid[new_pos_y][new_pos_x]
    if entry == ".":
        return True
    elif entry == "#":
        return False
    if char in "^v":
        if entry == "[":
            possible = True
            possible = possible and test_for_movement_2(char, new_pos_x, new_pos_y)
            possible = possible and test_for_movement_2(char, new_pos_x +1, new_pos_y)
            return possible
        elif entry == "]":
            possible = True
            possible = possible and test_for_movement_2(char, new_pos_x, new_pos_y)
            possible = possible and test_for_movement_2(char, new_pos_x -1, new_pos_y)
            return possible
        else: 
            raise Exception("How did you get here!??!?!")
    else:
        if entry == "[":
            return test_for_movement_2(char, new_pos_x +1, new_pos_y)
        elif entry == "]":
            return test_for_movement_2(char, new_pos_x -1, new_pos_y)
        else: 
            raise Exception("How did you get here!??!?!")

def execute_move_vertical(char, pos_x, pos_y, carry):
    dir_x, dir_y = directions[char]
    new_pos_x, new_pos_y = dir_x + pos_x, dir_y + pos_y
    new_entry = the_grid[new_pos_y][new_pos_x]
    the_grid[pos_y][pos_x] = "."
    if new_entry == ".":
        the_grid[new_pos_y][new_pos_x] = carry
        return
    elif new_entry == "[":
        execute_move_vertical(char, new_pos_x, new_pos_y, "[")
        the_grid[new_pos_y][new_pos_x] = carry
        execute_move_vertical(char, new_pos_x+1, new_pos_y, "]")
        the_grid[new_pos_y][new_pos_x+1] = "."
    elif new_entry == "]":
        execute_move_vertical(char, new_pos_x, new_pos_y, "]")
        the_grid[new_pos_y][new_pos_x] = carry
        execute_move_vertical(char, new_pos_x-1, new_pos_y, "[")
        the_grid[new_pos_y][new_pos_x-1] = "."
    else:
        raise Exception("How did you get here!??!?!")



def execute_move_2(char, rob_x, rob_y):
    dir_x, dir_y = directions[char]
    if char in "^v":
        entry = the_grid[rob_y][rob_x]
        execute_move_vertical(char, rob_x, rob_y, entry)
        rob_x, rob_y = dir_x + rob_x, dir_y + rob_y
    else:
        movement_incomplete = True
        pos_x, pos_y = rob_x, rob_y
        old_entry = "."
        while movement_incomplete:
            current_entry = the_grid[pos_y][pos_x] 
            the_grid[pos_y][pos_x] = old_entry
            new_pos_x, new_pos_y = dir_x + pos_x, dir_y + pos_y
            new_entry = the_grid[new_pos_y][new_pos_x] 
            if new_entry == ".":
                movement_incomplete = False
                the_grid[new_pos_y][new_pos_x] = current_entry
                rob_x, rob_y = dir_x + rob_x, dir_y + rob_y
            else:
                pos_y, pos_x = new_pos_y, new_pos_x
                old_entry = current_entry
    return rob_x, rob_y        

draw = True

number_of_instructions = 0
number_of_moves = 0
total_ins = len(instructions)
for instruction in instructions:
    if instruction in "^v<>":
        number_of_instructions += 1
        move_possible = test_for_movement_2(instruction, rob_x, rob_y)
        if draw == True:
            index = 5
            drawfile_path = os.path.join(DRAWFILES, f"drawing_{index}.txt")
            with open(drawfile_path, "w") as drawfile:
                print_grid = ["".join(line) for line in the_grid]
                print_grid.append(f"Next: {instruction} Possible: {move_possible}")
                print_grid.append(f"Instruction: {number_of_instructions} of {total_ins}")
                drawfile.write("".join("\n".join(print_grid)))   
        if move_possible:
            number_of_moves +=1
            rob_x, rob_y = execute_move_2(instruction, rob_x, rob_y)

accumulator = 0
for row in range(g_height):
    for column in range(g_width):
        if the_grid[row][column] == "[":
            accumulator += column + row*100
print(accumulator)
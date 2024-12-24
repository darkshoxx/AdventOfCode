
from collections import defaultdict
import os
import re
import math

from time import sleep


from functools import cache
HERE = os.path.dirname(__file__)
print(HERE)
DRAWFILES = os.path.join(HERE, "drawfiles")
filename = "input_small.txt"
INPUT_FILE = os.path.join(HERE, filename)

with open(INPUT_FILE) as my_file:
    input_data = my_file.read()
    input_lines = input_data.split("\n")
print(input_lines.pop())

keypad_big = [["7","8","9"],["4","5","6"],["1","2","3"],["X","0","A"]]
keypad_small = [["X","^","A"],["<","v",">"]]

def get_key(keypad, pos_x, pos_y):
    entry = keypad[pos_y][pos_x]
    if entry == "X":
        raise Exception("Invalid Position")
    return entry

def find_coords_of_button(keypad, symbol):
    for y_pos, row in enumerate(keypad):
        for x_pos, column in enumerate(row):
            if column == symbol:
                return (x_pos, y_pos)

print(find_coords_of_button(keypad_big,"6"))

directions = {
    "^":  (0,-1),
    "v": (0,1),
    "<":(-1,0),
    ">": (1,0)
}

def simulate(keypad_destination, start_x_dest, start_y_dest, path):
    cur_x, cur_y = start_x_dest, start_y_dest
    valid = True
    for movement in path:
        mov_x, mov_y = directions[movement]
        cur_x, cur_y = cur_x + mov_x, cur_y + mov_y
        if keypad_destination[cur_y][cur_x] == "X":
            valid = False
    return valid




def navigate_to_next_button(keypad_destination, start_x_dest, start_y_dest, target_symbol_dest):
    dest_tar_x, dest_tar_y = find_coords_of_button(keypad_destination, target_symbol_dest)
    # if start_x_dest == 0:
    #     row_first = True
    # else:
    #     row_first = False
    # if lookaheads:
    #     for entry in lookaheads:
    #         x_same = False
    #         y_same = False
    #         ahead_x, ahead_y = find_coords_of_button(keypad_destination, entry)
    #         if ahead_x == dest_tar_x:
    #             x_same = True
    #         if ahead_y == dest_tar_y:
    #             y_same = True
    #         both_same = x_same and y_same
    #         if not both_same:
    #             break
    #     if x_same:
    #         row_first = True
    #     else:
    #         row_first = False
            
    dist_x = dest_tar_x - start_x_dest
    path_x = [">"]*max(0,dist_x) + ["<"]*max(0, -dist_x)
    dist_y = dest_tar_y - start_y_dest
    path_y = ["v"]*max(0,dist_y) + ["^"]*max(0, -dist_y)
    path_unsorted = path_x + path_y

    from sympy.utilities.iterables import multiset_permutations

    sorted_paths = multiset_permutations(path_unsorted)
    return_paths = []
    for path in sorted_paths:
        if simulate(keypad_destination, start_x_dest, start_y_dest, path):
            return_paths.append(path)
    return return_paths, dest_tar_x, dest_tar_y

    # if row_first:
    #     path = path_x + path_y + ["A"]
    # else:
    #     path = path_y + path_x + ["A"]
    
    return path, dest_tar_x, dest_tar_y
test_string = "029A"

def get_next_string(string, keypad):
    start_x, start_y = find_coords_of_button(keypad, "A")
    path = []
    for letter in string:
        # if i != len(string)-1:
        #     lookaheads = string[(i+1):]
        # else:
        #     lookaheads = None
        temp_path, start_x, start_y = navigate_to_next_button(keypad, start_x, start_y,letter)
        path += temp_path
    return path

def start_to_end(string):
    print(string)
    path = get_next_string(string, keypad_big)
    print("".join(path))
    path = get_next_string(path, keypad_small)
    print("".join(path))
    path = get_next_string(path, keypad_small)
    print("".join(path))
    return path

accumulator = 0
for line in input_lines:
    line = input_lines[4]
    value = int(line[:-1])
    path = start_to_end(line)
    # print("".join(path))
    print(len(path))
    print(value)
    accumulator += len(path)*value

print("Accumulator:", accumulator)
# path = start_to_end(test_string)

                                         



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
the_grid = [list(line) for line in input_lines]
width = len(input_lines[0])
height = len(input_lines)


def test_outside_grid(x_pos, y_pos):
    return x_pos < 0 or x_pos > width-1 or y_pos<0 or y_pos > height-1

for row in range(height):
    for column in range(width):
        entry = input_lines[row][column]
        if entry == "S":
            start_x, start_y = column, row
        elif entry == "E":
            end_x, end_y = column, row


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

replacers = {
    "N": "^",
    "S": "v",
    "W": "<",
    "E": ">"
}

reverse_replacers = {
    "^": "N",
    "v": "S",
    "<": "W",
    ">": "E"
}


# def plug_dead_ends():
#     exit_code = False
#     for row in range(height):
#         for column in range(width):
#             entry = the_grid[row][column]
#             if entry == ".":
#                 neighbours = []
#                 for _, value in directions.items():
#                     new_x, new_y = column + value[0], row + value[1]
#                     neighbour_entry = the_grid[new_y][new_x]
#                     neighbours.append(neighbour_entry)
#                 pound_list =  [i for i, val in enumerate(neighbours) if val == "#"]
#                 if len(pound_list) == 3:
#                     exit_code = True
#                     the_grid[row][column] = "#"
#     return exit_code

# still_fixing = True
# while still_fixing:
#     still_fixing = plug_dead_ends()



def grid_traversal(the_grid):
    new_cells = [(start_x, start_y)]
    end_not_found = True
    depth = 0
    while end_not_found:
        fresh_cells = []
        depth += 1
        for cell in new_cells:
            if the_grid[cell[1]][cell[0]] in reverse_replacers.keys():
                offsets = directions[reverse_replacers[the_grid[cell[1]][cell[0]]]]
                new_x = offsets[0]+ cell[0]
                new_y = offsets[1]+ cell[1]
                if the_grid[new_y][new_x] in [".", "E"]:
                    fresh_cells.append((new_x, new_y))
                    the_grid[new_y][new_x] = depth
                    if (new_x, new_y) == (end_x, end_y):
                        end_not_found = False                
            else:
                for _, offsets in directions.items():
                    new_x = offsets[0]+ cell[0]
                    new_y = offsets[1]+ cell[1]
                    if the_grid[new_y][new_x] in [".", "E"]:
                        fresh_cells.append((new_x, new_y))
                        the_grid[new_y][new_x] = depth
                        if (new_x, new_y) == (end_x, end_y):
                            end_not_found = False
                    elif the_grid[new_y][new_x] in reverse_replacers.keys():
                        fresh_cells.append((new_x, new_y))
                        if (new_x, new_y) == (end_x, end_y):
                            end_not_found = False                  
        new_cells = fresh_cells
    default = the_grid[end_y][end_x]
    return default
default = grid_traversal(the_grid)
print(default)
accumulator = 0

def transform(entry):
    if type(entry) is int:
        return str(int(entry/1000))
    else:
        return entry

# for row in range(1,height-1):
#     for column in range(1,width-1):
#         entry = input_lines[row][column]
#         if entry == "#":
#             reachable_neighbours = []
#             for direction, offsets in directions.items():
#                 if input_lines[row + offsets[1]][column + offsets[0]] in [".", "S", "E"]:
#                     reachable_neighbours.append(direction)
#             if len(reachable_neighbours) > 1:
#                 for neighbour in reachable_neighbours:
#                     cheat_grid = [list(line) for line in input_lines]
#                     cheat_grid[row][column] = replacers[neighbour]
#                     result = grid_traversal(cheat_grid)
#                     if result < default - 99:
#                     # if result < default:

#                         print(default - result)
#                         accumulator +=1

# print(f"Accumulator: {accumulator}")

# 1453 is too low


# def test_outside_grid_strict(x_pos, y_pos):
#     return x_pos < 0 or x_pos > width-1 or y_pos<0 or y_pos > height-1

# Part 2:
# hitlist = []
# @cache
# def explore(x_pos, y_pos, cheat_steps, picoseconds, cheat_start = None, cheat_end = None):
#     if (x_pos, y_pos) == (end_x, end_y):
#         hitlist.append(picoseconds, cheat_start, cheat_end)
#         # TODO: Dict cheat_start -> cheat_end
#         return
#     options = []
#     for _, offsets in directions.items():
#         new_x = offsets[0]+ x_pos
#         new_y = offsets[1]+ y_pos
#         entry = input_lines[new_y][new_x]
#         if entry in [".", "E"]:
#             options.append((new_x, new_y, False))
#         if cheat_steps > 0:
#             if not test_outside_grid_strict(new_x, new_y):
#                 if entry == "#":
#                     options.append((new_x, new_y, True))              
#     for option in options:
#         new_x = option[0]
#         new_y = option[1]
#         # option[2]: stepping onto a cheat tile
#         if not option[2]:
#             if 0 < cheat_steps < 20:
#                 # continue cheating, despite stepping on a legal tile
#                 explore(new_x, new_y, cheat_steps - 1, picoseconds + 1, cheat_start, cheat_end)
#                 # stop cheating
#                 cheat_steps = 0
#             explore(new_x, new_y, cheat_steps, picoseconds + 1, cheat_start, cheat_end)
#         else:
#             if cheat_steps == 20:
#                 # start cheating
#                 cheat_start = (x_pos, y_pos)
#             elif cheat_steps == 1:
#                 # final cheating step
#                 cheat_end = (new_x, new_y)
#             # anyway, continue cheating
#             explore(new_x, new_y, cheat_steps -1, picoseconds + 1, cheat_start, cheat_end)
# doesn't work
# import sys
# sys.setrecursionlimit(7000)
# explore(start_x, start_y, 20, 0)
# print(hitlist)
def test_outside_grid_strict(x_pos, y_pos):
    return x_pos < 1 or x_pos > width-2 or y_pos<1 or y_pos > height-2

@cache
def get_options(x_pos, y_pos, cheatable):
    options = []
    for _, offsets in directions.items():
        new_x = offsets[0] + x_pos
        new_y = offsets[1] + y_pos
        if not test_outside_grid_strict(new_x, new_y) :
            entry = input_lines[new_y][new_x]
            if entry in [".", "E"]:
                options.append((new_x, new_y, False))
            if cheatable:
                # if not test_outside_grid_strict(new_x, new_y):
                if entry == "#":
                    options.append((new_x, new_y, True))
    return options      

# thread notation: x_pos, y_pos, cheat_steps, picoseconds, cheat_start = None, cheat_end = None, history):

def thread_is_new(new_threads, new_data):
    # new_x, new_y, cheat_steps, picoseconds, cheat_start, cheat_end = new_data
    for thread in new_threads:
        if thread[0:6] == new_data:
            return False
    return True


candidates = []
if filename == "input_small.txt":
    num_cheat_steps = 20
    time_limit = 90
    default = 84
    improvement = 0
elif filename == "input.txt":
    num_cheat_steps = 20
    time_limit = 10000
    default = 9420
    improvement = 99
threads = [(start_x, start_y, num_cheat_steps, 0, None, None, [])]
threads_running = True
while threads_running:
    new_threads = []
    for thread in threads:
        thread[6].append((thread[0], thread[1]))
        cur_x = thread[0]
        cur_y = thread[1]
        cheat_steps = thread[2]
        picoseconds = thread[3]
        cheat_start = thread[4]
        cheat_end = thread[5]
        history = thread[6]
        if (thread[0], thread[1]) == (end_x, end_y):
            if cheat_start and not cheat_end:
                cheat_end = (end_x, end_y)
            if all((cheat_start, cheat_end) != item[1:] for item in candidates):
                if picoseconds < default - improvement:
                    if (picoseconds, cheat_start) == (10, (1, 3)):
                        for cheat_end in [(3, 7),(4, 8),(5, 7)]:

                            print(cheat_end, history)
                    candidates.append((picoseconds, cheat_start, cheat_end))
        else:
            cheatable = thread[2]>0
            options = get_options(thread[0], thread[1], cheatable)
            for option in options:
                new_x = option[0]
                new_y = option[1]
                if (new_x, new_y) not in history and picoseconds<time_limit:
                    # option[2]: stepping onto a cheat tile
                    if not option[2]:
                        if 0 < cheat_steps < num_cheat_steps:
                            # continue cheating, despite stepping on a legal tile
                            if thread_is_new(new_threads,(new_x, new_y, cheat_steps - 1, picoseconds + 1, cheat_start, cheat_end)):
                                new_threads.append((new_x, new_y, cheat_steps - 1, picoseconds + 1, cheat_start, cheat_end, history[:] ))
                            # stop cheating
                            # cheat_steps = 0
                            # cheat_end = (new_x, new_y)
                            if thread_is_new(new_threads,(new_x, new_y, 0, picoseconds + 1, cheat_start, (new_x, new_y))):
                                new_threads.append((new_x, new_y, 0, picoseconds + 1, cheat_start, (new_x, new_y), history[:] ))
                        else:
                            if thread_is_new(new_threads,(new_x, new_y, cheat_steps, picoseconds + 1, cheat_start, cheat_end)):
                                new_threads.append((new_x, new_y, cheat_steps, picoseconds + 1, cheat_start, cheat_end, history[:] ))
                    else:
                        if cheat_steps == num_cheat_steps:
                            # start cheating
                            cheat_start = (thread[0], thread[1])
                        if cheat_steps == 1:
                            # final cheating step
                            cheat_end = (new_x, new_y)
                        # anyway, continue cheating
                        # explore(new_x, new_y, cheat_steps -1, picoseconds + 1, cheat_start, cheat_end)
                        if thread_is_new(new_threads, (new_x, new_y, cheat_steps -1, picoseconds + 1, cheat_start, cheat_end)):
                            new_threads.append((new_x, new_y, cheat_steps -1, picoseconds + 1, cheat_start, cheat_end, history[:] ))
    threads = new_threads
    if not new_threads:
        threads_running = False
    else:
        print(len(threads))
print(candidates)
savers:dict  = {}
for candidate in candidates:
    saved = default - candidate[0]
    if saved == 74:
        print(candidate)
    if saved not in savers.keys():
        savers[saved] = 1
    else:
        savers[saved] += 1
for key, value in savers.items():
    if key > 49:
        print(f"There are {value} cheats that save {key} picoseconds.")
print(len(candidates))
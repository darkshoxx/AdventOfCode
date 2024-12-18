
from collections import defaultdict
import os
import re
import math
HERE = os.path.dirname(__file__)
print(HERE)
DRAWFILES = os.path.join(HERE, "drawfiles")
filename = "input.txt"
INPUT_FILE = os.path.join(HERE, filename)

with open(INPUT_FILE) as my_file:
    input_data = my_file.read()
    input_lines = input_data.split("\n")
print(input_lines.pop())

the_grid = defaultdict(lambda:".")

for i, line in enumerate(input_lines):
    if i < 1024:
        x,y = line.split(",")
        the_grid[(int(x),int(y))] = "#"
for x in [-1, 71]:
    for y in range(-1,72):
        the_grid[(int(x),int(y))] = "#"
for y in [-1, 71]:
    for x in range(-1,72):
        the_grid[(int(x),int(y))] = "#"

directions = {
    "N": (0,-1),
    "S": (0,1),
    "W": (-1,0),
    "E": (1,0)
}
total_cells = [(0,0)]
new_cells = [(0,0)]
end_not_found = True
depth = 0
while end_not_found:
    fresh_cells = []
    depth += 1
    for cell in new_cells:
        for direction, offsets in directions.items():
            new_x = offsets[0]+ cell[0]
            new_y = offsets[1]+ cell[1]
            if the_grid[(new_x, new_y)] == ".":
                fresh_cells.append((new_x, new_y))
                the_grid[(new_x, new_y)] = depth
                if (new_x, new_y) == (70, 70):
                    end_not_found = False
    new_cells = fresh_cells
print(the_grid[(70, 70)])


## Part 2

the_grid = defaultdict(lambda:".")

for i, line in enumerate(input_lines):
    if i < 3038:
        x,y = line.split(",")
        the_grid[(int(x),int(y))] = "#"
        if i == 3037:
            print(x,y)
for x in [-1, 71]:
    for y in range(-1,72):
        the_grid[(int(x),int(y))] = "#"
for y in [-1, 71]:
    for x in range(-1,72):
        the_grid[(int(x),int(y))] = "#"

directions = {
    "N": (0,-1),
    "S": (0,1),
    "W": (-1,0),
    "E": (1,0)
}
total_cells = [(0,0)]
new_cells = [(0,0)]
end_not_found = True
depth = 0
while end_not_found:
    fresh_cells = []
    depth += 1
    for cell in new_cells:
        for direction, offsets in directions.items():
            new_x = offsets[0]+ cell[0]
            new_y = offsets[1]+ cell[1]
            if the_grid[(new_x, new_y)] == ".":
                fresh_cells.append((new_x, new_y))
                the_grid[(new_x, new_y)] = depth
                if (new_x, new_y) == (70, 70):
                    end_not_found = False
    new_cells = fresh_cells
print(the_grid[(70, 70)])

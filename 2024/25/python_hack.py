
from collections import defaultdict
import os
import re
import math

from time import sleep


from functools import cache
HERE = os.path.dirname(__file__)
print(HERE)
DRAWFILES = os.path.join(HERE, "drawfiles")
filename = "input.txt"
INPUT_FILE = os.path.join(HERE, filename)

with open(INPUT_FILE) as my_file:
    input_data = my_file.read()
    # input_lines = input_data.split("\n")
# print(input_lines.pop())

patterns = input_data.split("\n\n")
# print(patterns.pop())
lock_patterns = []
key_patterns = []
lock_biddings = []
key_biddings = []
for pattern in patterns:
    lines = pattern.split("\n")
    if lines[0][0] == "#":
        lock_patterns.append(lines)
    elif lines[0][0] == ".":
        key_patterns.append(lines)
    else:
        raise Exception("WHA?")

for key in key_patterns:
    bidding = [0, 0, 0, 0, 0]
    for row in range(5):
        for column in range(5):
            if not bidding[column] and key[row+1][column]=="#":
                bidding[column] = 5 - row
    key_biddings.append(bidding)

for lock in lock_patterns:
    bidding = [0, 0, 0, 0, 0]
    for row in range(5):
        for column in range(5):  
            if lock[row+1][column] == "#":
                bidding[column] = row + 1
    lock_biddings.append(bidding)

accumulator = 0
for key in key_biddings:
    for lock in lock_biddings:
        valid = True
        for index in range(5):
            valid = valid and ((key[index] + lock[index])<6)
        accumulator += valid
print(accumulator)
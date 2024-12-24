
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

inputs, gates = input_data.split("\n\n")
input_lines = inputs.split("\n")

gate_lines = gates.split("\n")
print(gate_lines.pop())
x_register = []
y_register = []
known_values = []
my_dict = {}
from copy import copy
for line in input_lines:
    var, val = line.split(": ")
    # index = int(var[1:])
    known_values.append(var)
    reg = var[:1]
    my_dict[var] = int(val)
    mt_other_dict = copy(my_dict)
    if reg == "x":
        x_register.append(int(val))
    if reg == "y":
        y_register.append(int(val))

# print(x_register)
list_of_instructions = []
for line in gate_lines:
    arg_1, op, arg_2, _, res = line.split(" ")
    list_of_instructions.append((arg_1, op, arg_2, res))

def testline(tuple):
    arg_1, op, arg_2, res = tuple
    if (arg_1 in my_dict.keys()) and (arg_2 in my_dict.keys()):
        arg_1_val = my_dict[arg_1]
        arg_2_val = my_dict[arg_2]

        if op == "OR":
            my_dict[res] = arg_1_val or arg_2_val
            return True
        elif op == "AND":
            my_dict[res] = arg_1_val and arg_2_val
            return True
        elif op == "XOR":
            my_dict[res] = arg_1_val ^ arg_2_val
            return True
        else:
            raise Exception("WHAT?")
    return False

while list_of_instructions:
    unfulfilled_instructions = []
    for instruction in list_of_instructions:
        resolved = testline(instruction)
        if not resolved:
            unfulfilled_instructions.append(instruction)
    list_of_instructions = unfulfilled_instructions

z_register = []
for key, value in my_dict.items():
    if key[0]=="z":
        z_register.append((key, value))
z_sorted = sorted(z_register, key=lambda x: x[0])
print(z_sorted)
z_value = "0b" + "".join([str(item[1]) for item in reversed(z_sorted)])
print(z_value)
print(int(z_value,2))


# part 2


# did it manually, see notes.txt

operator_table = {}

list_of_instructions = []
for i, line in enumerate(gate_lines):
    arg_1, op, arg_2, _, res = line.split(" ")
    if op not in operator_table.keys():
        operator_table[op] = 1
    else:
        operator_table[op] += 1
    if res in ["dnt","gdf","gwc","jst","mcm","z05","z15","z30"]:
        print(i, res)
    list_of_instructions.append([arg_1, op, arg_2, res])

print(operator_table)

# from itertools import combinations
# num_of_lines = len(gate_lines)
# counter = 0
# for combo in combinations(range(num_of_lines),8):
#     counter +=1
#     if counter %1000000 == 0:
#         print(combo)

my_list = list(range(8))
# generates all 4-sets of pairs from 8 candidates
combos = []
for i in range(1,8):
    fresh_list = my_list[:]
    pair_1 = (0, i)
    fresh_list.remove(0)
    fresh_list.remove(i)
    start = fresh_list[0]
    for j in fresh_list:
        if j != start:
            leftover_1 = fresh_list[:]
            pair_2 = (start, j)
            leftover_1.remove(start)
            leftover_1.remove(j)
            new_start = leftover_1[0]
            for k in leftover_1:
                if k != new_start:
                    leftover_2 = leftover_1[:]
                    pair_3 = (new_start, k)
                    leftover_2.remove(new_start)
                    leftover_2.remove(k)
                    pair_4 = tuple(leftover_2)
                    combos.append((pair_1, pair_2, pair_3, pair_4))

def swapper(instructions, tuple_8, pairs):
    for pair_1, pair_2 in pairs:
        swap_1 = tuple_8[pair_1]
        swap_2 = tuple_8[pair_2]
        carry = instructions[swap_1][3]
        instructions[swap_1][3] = instructions[swap_2][3]
        instructions[swap_2][3] = carry
    return instructions

list_of_instructions = swapper(list_of_instructions, (8,77,94,124,130,159,169,217), ((0, 5), (1, 4), (3, 6), (2, 7)))

def testline2(tuple):
    arg_1, op, arg_2, res = tuple
    if (arg_1 in mt_other_dict.keys()) and (arg_2 in mt_other_dict.keys()):
        arg_1_val = mt_other_dict[arg_1]
        arg_2_val = mt_other_dict[arg_2]

        if op == "OR":
            mt_other_dict[res] = arg_1_val or arg_2_val
            return True
        elif op == "AND":
            mt_other_dict[res] = arg_1_val and arg_2_val
            return True
        elif op == "XOR":
            mt_other_dict[res] = arg_1_val ^ arg_2_val
            return True
        else:
            raise Exception("WHAT?")
    return False

while list_of_instructions:
    unfulfilled_instructions = []
    for instruction in list_of_instructions:
        resolved = testline2(instruction)
        if not resolved:
            unfulfilled_instructions.append(instruction)
    list_of_instructions = unfulfilled_instructions

z_register = []
for key, value in my_dict.items():
    if key[0]=="z":
        z_register.append((key, value))
z_sorted = sorted(z_register, key=lambda x: x[0])
print(z_sorted)

z_value = "0b" + "".join([str(item[1]) for item in reversed(z_sorted)])
x_value = "0b0" + "".join([str(item) for item in reversed(x_register)])
y_value = "0b0" + "".join([str(item) for item in reversed(y_register)])
print(x_value)
print(y_value)
print(bin(int(x_value,2) + int(y_value,2)))
print(z_value)
    
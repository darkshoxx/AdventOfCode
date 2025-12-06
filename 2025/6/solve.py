import os
HERE = os.path.abspath(os.path.dirname(__file__))
INPUT = os.path.join(HERE, "input.txt")
INPUTTEST = os.path.join(HERE, "inputtest.txt")
# Part 1
with open(INPUT, "r") as f:
    content = f.readlines()
clean_lines = [line[:-1] for line in content]
import math
accumulator = 0
columns = len([item for item in clean_lines[0].split(" ") if item not in [""," ", "  ", "    "]])
op_dict = {"+":sum, "*":math.prod}
very_clean_lines = []
for line in clean_lines:
    very_clean_lines.append([item for item in line.split(" ") if item not in [""," ", "  ", "    "]])
for index in range(columns):
    my_col = []
    operator = very_clean_lines[4][index]
    for line in very_clean_lines:
        if line[0] != "*":
            my_col.append(int(line[index]))
    result = op_dict[operator](my_col)
    accumulator += result
print(accumulator)
    
# Part 2
lengths = []
for index in range(columns):
    current_max = 0
    for line in very_clean_lines:
        if line[0] != "*":
            if len(line[index]) > current_max:
                current_max = len(line[index])
    lengths.append(current_max)
print(lengths)


accumulator = 0 
pointer = 0
for number in lengths:
    my_col = []
    for line in clean_lines:
        my_col.append(line[pointer:pointer + number])
    operator = op_dict[my_col[4][0]]
    terms_list = []
    for line_index in range(number):
        terms_list.append(int("".join([item[line_index] for item in my_col if item[line_index] not in ["+", "*"]])))
    result = operator(terms_list)
    accumulator += result
    pointer += number + 1
print(accumulator)




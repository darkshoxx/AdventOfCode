import os
HERE = os.path.dirname(__file__)
print(HERE)
INPUT_FILE = os.path.join(HERE, "input.txt")
with open(INPUT_FILE) as my_file:
    input_data = my_file.read()
    input_lines = input_data.split("\n")
print(input_lines.pop())

height = len(input_lines)
width = len(input_lines[0])

accumulator = 0

def try_path(i, j, data):
    if 0 <= i < width:
        if 0 <= j < height:
            return data[i][j]
    return "0"

def test_for_xmas(row, column, input_lines):
    vertical_directions = [-1, 0, 1]
    horizontal_directions = [-1, 0, 1]
    mini_accumulator = 0
        

    for v_dir in vertical_directions:
        for h_dir in horizontal_directions:
            test_list = []
            for offset in range(1, 4):
                test_list.append(try_path(row + offset*v_dir, column + offset*h_dir, input_lines))
            if test_list == ["M","A","S"]:
                mini_accumulator += 1
    return mini_accumulator


for row in range(height):
    for column in range(width):
        if input_lines[row][column]=="X":
            accumulator += test_for_xmas(row, column, input_lines)

print(accumulator)

## Part 2

accumulator = 0
MS_LIST = [["M","S"],["S","M"]]
def test_for_x_mas(row, column, input_lines):
    mini_accumulator = 0
        


    test_list = []
    for h_offset in [-1,1]:
        for v_offset in [-1,1]:
            test_list.append(try_path(row + v_offset, column + h_offset, input_lines))
    diag_1 = [test_list[0],test_list[3]]
    diag_2 = [test_list[1],test_list[2]]
    if diag_1 in MS_LIST and diag_2 in MS_LIST:
        mini_accumulator += 1
    return mini_accumulator

for row in range(height):
    for column in range(width):
        if input_lines[row][column]=="A":
            accumulator += test_for_x_mas(row, column, input_lines)

print(accumulator)

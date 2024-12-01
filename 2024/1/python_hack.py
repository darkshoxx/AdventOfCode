import os
HERE = os.path.dirname(__file__)
print(HERE)
INPUT_FILE = os.path.join(HERE, "input.txt")
with open(INPUT_FILE) as my_file:
    input_data = my_file.read()
    input_lines = input_data.split("\n")
first_list = [int(line.split("  ")[0]) for line in input_lines if line]
second_list = [int(line.split("  ")[1]) for line in input_lines if line]
first_list.sort()
second_list.sort()
accumulator = 0
for first, second in zip(first_list, second_list):
    accumulator += abs(first-second)
print(accumulator)
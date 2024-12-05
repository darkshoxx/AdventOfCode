import os
from collections import defaultdict
HERE = os.path.dirname(__file__)
print(HERE)
INPUT_FILE = os.path.join(HERE, "input.txt")
with open(INPUT_FILE) as my_file:
    input_data = my_file.read()
    input_lines = input_data.split("\n")
print(input_lines.pop())

orderings, updates = input_data.split("\n\n")
ordering_lines = orderings.split("\n")
update_lines = updates.split("\n")
update_lines.pop()

lookup_dict = defaultdict(lambda: [])
for entry in ordering_lines:
    left, right = entry.split("|")
    if lookup_dict[left] == []:
        lookup_dict[left] = [right]
    else:
        lookup_dict[left].append(right)


def compare(start, end):
    end_list = lookup_dict[end]
    if end_list is not None:
        if start in end_list:
            return False
    return True
    
bad_lines = []
accumulator = 0
for line in update_lines:
    line_entries = line.split(",")
    line_length = len(line_entries)
    central_index = int((line_length-1)/2)
    currently_valid = True
    for first_index in range(line_length-1):
        for second_index in range(first_index+1, line_length):
            currently_valid = currently_valid and compare(line_entries[first_index], line_entries[second_index])
    if currently_valid:
        accumulator += int(line_entries[central_index])
    else:
        bad_lines.append(line)
print(accumulator)


## Part 2
accumulator = 0
for line in bad_lines:
    line = line.split(",")
    obstructions_dict = {}
    for entry in line:
        entry_list = lookup_dict[entry]
        obstructions = []
        other_entries = [other_entry for other_entry in line if other_entry != entry]
        for other_entry in other_entries:
            if other_entry in entry_list:
                obstructions.append(other_entry)
        # print(obstructions)
        obstructions_dict[len(obstructions)] = obstructions
    sorted_list = []
    line_length = len(line)
    for list_length in range(1, line_length):
        singleton = [entry for entry in obstructions_dict[list_length] if entry not in sorted_list]
        sorted_list.append(singleton[0])
    accumulator += (int(sorted_list[(int(line_length/2))]))
print(accumulator)


import os
HERE = os.path.dirname(__file__)
print(HERE)
INPUT_FILE = os.path.join(HERE, "input.txt")
with open(INPUT_FILE) as my_file:
    input_data = my_file.read()
    input_lines = input_data.split("\n")

def first_differences(my_list):
    length = len(my_list)
    result = []
    for index in range(length-1):
        result.append(int(my_list[index+1]) - int(my_list[index]))
    return result

print(input_lines.pop())
safe_observed = 0

def line_tester(levels):
    differences = first_differences(levels)
    if differences[0]<0:
        differences = [-item for item in differences]
    truth_vector = [(item>0 and item<4) for item in differences]
    if all(truth_vector):
        return True
    return False


safe_observed = 0
for line in input_lines:
    levels = line.split(" ")
    if(line_tester(levels)):
        safe_observed +=1
    
print(safe_observed)

# part 2

def skip_level_generator(levels:list):
    num_levels = len(levels)
    list_of_lists = []
    for index in range(num_levels):
        new_list = levels[:]
        new_list.pop(index)
        list_of_lists.append(new_list)
    return list_of_lists

safe_observed = 0
for line in input_lines:
    levels = line.split(" ")
    list_of_lists = skip_level_generator(levels)
    truth_of_truths = []
    for level_list in list_of_lists:
        truth_of_truths.append(line_tester(level_list))
    if any(truth_of_truths):
        safe_observed +=1


    # line_tester(levels)
    
print(safe_observed)







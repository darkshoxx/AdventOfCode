import os
HERE = os.path.dirname(__file__)
print(HERE)
INPUT_FILE = os.path.join(HERE, "input.txt")
with open(INPUT_FILE) as my_file:
    input_data = my_file.read()
    input_lines = input_data.split("\n")
print(input_lines.pop())

def adder(a,b):
    return a+b
def multiplier(a,b):
    return a*b
while False:
    candidate_accumulator = 0
    for line in input_lines:
        test_string, input_numbers = line.split(":")
        components = [int(item) for item in input_numbers.split(" ") if item]
        test_number = int(test_string)
        # print(components)
        # print(test_number)
        num_of_operators = len(components) - 1
        for bin_number in range(2**num_of_operators):
            flags = bin(bin_number)[2:]
            flags = (num_of_operators - len(flags))*"0" + flags
            mini_accumulator = components[0]
            for index in range(num_of_operators):

                if flags[index] == "0":
                    operator = adder
                else:
                    operator = multiplier
                mini_accumulator = operator(mini_accumulator,components[index+1])
            if mini_accumulator == test_number:
                candidate_accumulator += mini_accumulator
                print(candidate_accumulator)
                break
            # print(mini_accumulator)
    print(candidate_accumulator)

## Part 2
import math
import numpy as np
def concat(b, a):
    return b*(10**math.floor(math.log10(a)+1)) + a



candidate_accumulator = 0
for line in input_lines:
    test_string, input_numbers = line.split(":")
    components = [int(item) for item in input_numbers.split(" ") if item]
    test_number = int(test_string)
    # print(components)
    # print(test_number)
    num_of_operators = len(components) - 1
    for bin_number in range(3**num_of_operators):
        flags = np.base_repr(bin_number, base=3)
        flags = (num_of_operators - len(flags))*"0" + flags
        mini_accumulator = components[0]
        for index in range(num_of_operators):
            indicator = flags[index]
            if indicator == "0":
                operator = adder
            elif indicator == "1":
                operator = multiplier
            else:
                operator = concat
            mini_accumulator = operator(mini_accumulator,components[index+1])
        if mini_accumulator == test_number:
            candidate_accumulator += mini_accumulator
            print(candidate_accumulator)
            break
        # print(mini_accumulator)
print(f"result: {candidate_accumulator}")
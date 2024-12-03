import os
HERE = os.path.dirname(__file__)
print(HERE)
INPUT_FILE = os.path.join(HERE, "input.txt")
with open(INPUT_FILE) as my_file:
    input_data = my_file.read()
    input_lines = input_data.split("\n")
print(input_lines.pop())




# input_data = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

input_length = len(input_data)

# Attempt 2: regex

import re
accumulator = 0
re_comparison_left = []
re_comparison_right = []
matches = re.findall(pattern= "mul\(\d\d?\d?,\d\d?\d?\)", string = input_data)
for match in matches:
    splits = re.split(pattern = "\(|\)|,", string =match)
    re_comparison_left.append(splits[1])
    re_comparison_right.append(splits[2])
    accumulator += int(splits[1]) * int(splits[2])
# print(matches)
print(accumulator)


# Attempt 1: String Search
def chartest(sample, comparison):
    return sample == comparison




accumulator = 0
lagged_accumulator = 0
currently_valid = True
test_string_position = 0
digits_observed = 0
f_buffer = []
f_int = 0
e_buffer = []
e_int = 0
mul_string = "mul(f,e)"
numbers = "0123456789"
str_comparison_left = []
str_comparison_right = []
for position in range(input_length):
    if accumulator != lagged_accumulator:
        lagged_accumulator = accumulator
    if digits_observed > 3:
        currently_valid = False
    if not currently_valid:
        currently_valid = True
        test_string_position = 0
        digits_observed = 0
        f_buffer = []
        f_int = 0
        e_buffer = []
        e_int = 0
    if mul_string[test_string_position] not in ["f", "e"]:
        currently_valid = chartest(input_data[position], mul_string[test_string_position])
        if currently_valid:
            test_string_position += 1
    else:
        if input_data[position] in numbers:
            digits_observed += 1
            if mul_string[test_string_position] == "f":
                f_buffer.append(input_data[position])
                if input_data[position+1] == ",":
                    str_comparison_left.append("".join(f_buffer))
                    f_int = int("".join(f_buffer))
                    f_buffer = []
                    test_string_position += 1
                    digits_observed = 0
                elif input_data[position+1] not in numbers:
                    currently_valid = False
            if mul_string[test_string_position] == "e":
                e_buffer.append(input_data[position])
                if input_data[position+1] == ")":
                    str_comparison_right.append("".join(e_buffer))
                    e_int = int("".join(e_buffer))
                    e_buffer = []
                    test_string_position = 0
                    accumulator += e_int*f_int
                    digits_observed = 0
                elif input_data[position+1] not in numbers:
                    currently_valid = False
                    str_comparison_left.pop()

print(f"Part 1: {accumulator}")

## Part 2


enabled = True
accumulator = 0
lagged_accumulator = 0
currently_valid = True
test_string_position = 0
digits_observed = 0
f_buffer = []
f_int = 0
e_buffer = []
e_int = 0
str_enable = "do()"
str_disable = "don't()"
mul_string = "mul(f,e)"
numbers = "0123456789"
str_comparison_left = []
str_comparison_right = []
for position in range(input_length):
    if input_data[position] == "d":
        if input_data[position:position+4] == str_enable:
            enabled = True
        elif input_data[position:position+7] == str_disable:
            enabled = False
    if not enabled:
        currently_valid = False
    if accumulator != lagged_accumulator:
        lagged_accumulator = accumulator
    if digits_observed > 3:
        currently_valid = False
    if not currently_valid:
        currently_valid = True
        test_string_position = 0
        digits_observed = 0
        f_buffer = []
        f_int = 0
        e_buffer = []
        e_int = 0
    if mul_string[test_string_position] not in ["f", "e"]:
        currently_valid = chartest(input_data[position], mul_string[test_string_position])
        if currently_valid:
            test_string_position += 1
    else:
        if input_data[position] in numbers:
            digits_observed += 1
            if mul_string[test_string_position] == "f":
                f_buffer.append(input_data[position])
                if input_data[position+1] == ",":
                    str_comparison_left.append("".join(f_buffer))
                    f_int = int("".join(f_buffer))
                    f_buffer = []
                    test_string_position += 1
                    digits_observed = 0
                elif input_data[position+1] not in numbers:
                    currently_valid = False
            if mul_string[test_string_position] == "e":
                e_buffer.append(input_data[position])
                if input_data[position+1] == ")":
                    str_comparison_right.append("".join(e_buffer))
                    e_int = int("".join(e_buffer))
                    e_buffer = []
                    test_string_position = 0
                    accumulator += e_int*f_int
                    digits_observed = 0
                elif input_data[position+1] not in numbers:
                    currently_valid = False
                    str_comparison_left.pop()

print(f"Part 2: {accumulator}")




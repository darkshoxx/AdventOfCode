import os
HERE = os.path.abspath(os.path.dirname(__file__))
INPUT = os.path.join(HERE, "input.txt")
INPUTTEST = os.path.join(HERE, "inputtest.txt")
# Part 1
with open(INPUT, "r") as f:
    content = f.readlines()

accumulator = 0
for line in content:
    best_ten = line[0]
    best_one = line[1]
    for index in range(1, len(line)-2):
        if line[index] > best_ten:
            best_ten = line[index]
            best_one = line[index+1]
        elif line[index] > best_one:
            best_one = line[index]
    if line[index+1] > best_one:
        best_one = line[index+1]
    result = int(best_ten + best_one)            
    accumulator +=result
print(accumulator)

# Part 2

def go_deeper(digits_available, string, pointer):
    difference = len(string) - digits_available
    best = "0"
    best_index = - 1
    for index in range(pointer+1, difference+1):
        if string[index] > best:
            best_index = index
            best = string[index]
            if best == "9":
                break
    pointer = best_index
    if digits_available == 1:
        return best
    result_string = go_deeper(digits_available-1, string, pointer)
    return best + result_string

accumulator = 0
for line in content:
    result = go_deeper(digits_available=12, string=line[:-1], pointer=-1)
    print(int(result))
    accumulator += int(result)
print(accumulator)


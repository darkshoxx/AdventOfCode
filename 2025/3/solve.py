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
accumulator = 0
for line in content:
    digits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    length = len(line)
    difference = length - 12
    for index in range(difference):
        pass


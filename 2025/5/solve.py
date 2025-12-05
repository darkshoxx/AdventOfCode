import os
HERE = os.path.abspath(os.path.dirname(__file__))
INPUT = os.path.join(HERE, "input.txt")
INPUTTEST = os.path.join(HERE, "inputtest.txt")
# Part 1
with open(INPUT, "r") as f:
    content = f.readlines()
cleanlines = [line[:-1] for line in content]

ranger = True
ranges = []
candidates = []
for line in cleanlines:
    if ranger:
        if line=="":
            ranger = False
        else:
            first, last = line.split("-")
            ranges.append((int(first), int(last)))
    else:
        candidates.append(int(line))

print(ranges)
print(candidates)
accumulator = 0
for candidate in candidates:
    found = False
    for first, last in ranges:
        if not found:
            if first <= candidate <= last:
                accumulator +=1
                found = True
print(accumulator)
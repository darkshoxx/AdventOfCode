import os
HERE = os.path.abspath(os.path.dirname(__file__))
INPUT = os.path.join(HERE, "input.txt")
INPUTTEST = os.path.join(HERE, "inputtest.txt")


# Part 1
with open(INPUT, "r") as f:
    content = f.readline()[:-1]

ranges = content.split(",")
tuples = []
for item in ranges:
    odd = False
    first, last = item.split("-")
    if len(first)%2 == 1:
        first = '1' + '0'*(len(last)-1)
        odd = True
    else:
        attribute = int(len(first)/2)
    if len(last)%2 == 1:
        if odd:
            continue
        last = '9'*len(first)
    else:
        attribute = int(len(last)/2)
    tuples.append((first, last, attribute))
print(tuples)

accumulator = 0
for first, last, attribute in tuples:
    comparer = last[:(attribute)]
    comparee = first[:(attribute)]
    # if comparer == comparee:
    if int(first)<=int(comparer + comparer)<=int(last):
        accumulator += int(comparer + comparer)
    while comparer != comparee:
        compint = int(comparer) - 1 
        comparer = str(compint)
        if int(first)<=int(comparer + comparer)<=int(last):
            accumulator += int(comparer + comparer)

print(accumulator)

# Part 2
accumulator = 0
for first, last, attribute in tuples:
    comparer = last[:(attribute)]
    comparee = first[:(attribute)]
    # if comparer == comparee:
    for i in range(1, attribute+1):
        mini = comparer[:i]
        multiples = int(attribute/i)
    if int(first)<=int(mini*multiples)<=int(last):
        accumulator += int(comparer + comparer)
    while comparer != comparee:
        compint = int(comparer) - 1 
        comparer = str(compint)
        for i in range(1, attribute+1):
            mini = comparer[:i]
            multiples = int(attribute/i)
        if int(first)<=int(mini*multiples)<=int(last):
            accumulator += int(comparer + comparer)

print(accumulator)
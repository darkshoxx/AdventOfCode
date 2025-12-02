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

# WRONG START OVER
# accumulator = 0
# for first, last, attribute in tuples:
#     comparer = last[:(attribute)]
#     comparee = first[:(attribute)]
#     # if comparer == comparee:
#     for i in range(1, attribute+1):
#         mini = comparer[:i]
#         multiples = int(attribute/i)
#     if int(first)<=int(mini*multiples)<=int(last):
#         accumulator += int(comparer + comparer)
#     while comparer != comparee:
#         compint = int(comparer) - 1 
#         comparer = str(compint)
#         for i in range(1, attribute+1):
#             mini = comparer[:i]
#             multiples = int(attribute/i)
#         if int(first)<=int(mini*multiples)<=int(last):
#             accumulator += int(comparer + comparer)
tuples = []
for item in ranges:
    odd = False
    first, last = item.split("-")
    tuples.append((first, last))




# Either count them, or calculate them
import math
# count
accumulator = 0

def conglomerator(first, last, check):
    found = []
    digits = len(first)
    for i in range(1, math.floor(digits/2) + 1): # a 1 every ith place
        if digits % i == 0:
            quotient = int(digits/i) # number of repititions
            cell =  "0"*(i-1) + "1"
            pattern = cell * quotient
            low = first[:i]
            high = last[:i]
            for walker in range(int(low), int(high)+1):
                if check(walker*int(pattern)):
                    if walker*int(pattern) not in found:
                        found.append(walker*int(pattern))

    return sum(found)

for first, last in tuples:
    lower = int(first)
    upper = int(last)
    def check(candidate):
        return lower <= candidate <= upper
    # generate all pattern numbers of the type 11111 10101010 100100100 etc
    if len(first)==len(last):
        local_sum_1 = conglomerator(first, last, check)
        accumulator += local_sum_1
    else:
        digits = len(first)
        local_sum_2 = conglomerator(first, digits*"9", check)
        local_sum_3 = conglomerator("1" + digits*"0", last, check)
        accumulator += local_sum_2 + local_sum_3
print(accumulator)
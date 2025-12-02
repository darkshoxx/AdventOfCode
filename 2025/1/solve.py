import os
HERE = os.path.abspath(os.path.dirname(__file__))
INPUT = os.path.join(HERE, "input.txt")
INPUTDG = os.path.join(HERE, "inputdg.txt")
INPUTTEST = os.path.join(HERE, "test.txt")

with open(INPUT, "r") as f:
    content = f.readlines()

directions = []
distances = []

# Part 1
for line in content:
    if line:
        directions.append(line[0])
        distances.append(int(line[1:]))

# print(directions)
# print(distances)

start = 50
counter = 0
for dir, dist in zip(directions, distances):
    if dir == "L":
        start = (start + dist) % 100
    else:
        start = (start - dist) % 100
    if start == 0:
        counter += 1
print("Counter:",counter)

# # Part 2

start = 50
counter = 0
for dir, dist in zip(directions, distances):
    lagged_start = start
    if dir == "L":
        start = (start - dist) 
    else:
        start = (start + dist)
    if start >= 100:
        counter += start // 100
    elif start == 0:
        counter +=1
    elif start < 0 and lagged_start !=0:
        counter += abs(start // 100)
        if start % 100 == 0:
            counter += 1 # what an obscure edge case.
    elif start < 0 and lagged_start == 0:
        counter += abs(start // 100) - 1
    start = start % 100
print("Counter:", counter)

# Part 2 alt:
start = 50
counter = 0
for dir, dist in zip(directions, distances):
    while dist > 0:
        if dir == "L":
            start -= 1
        else:
            start += 1
        start = start % 100
        if start == 0:
            counter +=1
        dist -=1
print("Counter:", counter)

import copy
# Part 2 comparer:
start_check = 50
start_run = 50
counter_check = 0
counter_run = 0
for dir, dist in zip(directions, distances):
    # RUN
    dist_run = copy.copy(dist)

    while dist_run > 0:
        if dir == "L":
            start_run -= 1
        else:
            start_run += 1
        start_run = start_run % 100
        if start_run == 0:
            counter_run +=1
        dist_run -=1
    # CHECK
    lagged_start = start_check
    if dir == "L":
        start_check = (start_check - dist) 
    else:
        start_check = (start_check + dist)
    if start_check >= 100:
        counter_check += start_check // 100
    elif start_check == 0:
        counter_check +=1
    elif start_check < 0 and lagged_start !=0:
        counter_check += abs(start_check // 100)
        if start_check % 100 == 0:
            counter_check += 1
    elif start_check < 0 and lagged_start == 0:
        counter_check += abs(start_check // 100) - 1
    start_check = start_check % 100    

    if counter_check != counter_run:
        print("HERE")
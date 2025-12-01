import os
HERE = os.path.abspath(os.path.dirname(__file__))
INPUT = os.path.join(HERE, "input.txt")

with open(INPUT, "r") as f:
    content = f.readlines()

directions = []
distances = []

# Part 1
for line in content:
    if line:
        directions.append(line[0])
        distances.append(int(line[1:]))

print(directions)
print(distances)

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
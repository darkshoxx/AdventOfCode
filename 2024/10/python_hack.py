import os
import time
HERE = os.path.dirname(__file__)
print(HERE)
INPUT_FILE = os.path.join(HERE, "input.txt")
with open(INPUT_FILE) as my_file:
    input_data = my_file.read()
    input_lines = input_data.split("\n")
print(input_lines.pop())

width = len(input_lines[0])
height = len(input_lines)

trailheads = []
for row in range(height):
    for column in range(width):
        if input_lines[row][column] == "0":
            trailheads.append([row, column])

trailfeet = []
for row in range(height):
    for column in range(width):
        if input_lines[row][column] == "9":
            trailfeet.append([row, column])

print(width, height)

directions = {
    "N": (-1,0),
    "E": (0,1),
    "S": (1,0),
    "W": (0,-1),
}

def test_outside_grid(x_pos, y_pos):
    return x_pos < 0 or x_pos > width-1 or y_pos<0 or y_pos > height-1

def go_uphill(position, depth, path: list):
    partial_tracks = set()
    for cardinal, offsets in directions.items():
        new_x, new_y = position[0] + offsets[0], position[1] + offsets[1]
        if not test_outside_grid(new_x, new_y):
            entry = input_lines[new_x][new_y]
            if entry == ".":
                entry = 20
            if int(entry) == depth:
                if depth == 9:
                    partial_tracks = partial_tracks.union({(new_x, new_y)})
                else:
                    path.append(cardinal)
                    partial_tracks = partial_tracks.union(go_uphill([new_x, new_y], depth+1, path))
    return partial_tracks


def go_downhill(position, depth, path: list):
    partial_tracks = set()
    for cardinal, offsets in directions.items():
        new_x, new_y = position[0] + offsets[0], position[1] + offsets[1]
        if not test_outside_grid(new_x, new_y):
            entry = input_lines[new_x][new_y]
            if entry == ".":
                entry = -10
            if int(entry) == depth:
                if depth == 0:
                    partial_tracks = partial_tracks.union({(new_x, new_y)})
                else:
                    path.append(cardinal)
                    partial_tracks = partial_tracks.union(go_downhill([new_x, new_y], depth-1, path))
    return partial_tracks

t0 = time.time()
for _ in range(1):
    accumulator = []
    for head in trailheads:
        tracks = go_uphill(head, 1, path = [])
        accumulator.append(len(tracks))

print(sum(accumulator))
t1 = time.time()
for _ in range(1):
    accumulator = []
    for foot in trailfeet:
        tracks = go_downhill(foot, 8, path = [])
        accumulator.append(len(tracks))

print(sum(accumulator))
t2=time.time()
print(f"Time taken uphill:{t1-t0}\nTime taken dnhill:{t2-t1}")

# Part 2

def go_uphill(position, depth, path: list):
    partial_tracks = []
    for cardinal, offsets in directions.items():
        new_x, new_y = position[0] + offsets[0], position[1] + offsets[1]
        if not test_outside_grid(new_x, new_y):
            entry = input_lines[new_x][new_y]
            if entry == ".":
                entry = 20
            if int(entry) == depth:
                if depth == 9:
                    partial_tracks.append({(new_x, new_y)})
                else:
                    path.append(cardinal)
                    partial_tracks += go_uphill([new_x, new_y], depth+1, path)
    return partial_tracks


def go_downhill(position, depth, path: list):
    partial_tracks = []
    for cardinal, offsets in directions.items():
        new_x, new_y = position[0] + offsets[0], position[1] + offsets[1]
        if not test_outside_grid(new_x, new_y):
            entry = input_lines[new_x][new_y]
            if entry == ".":
                entry = -10
            if int(entry) == depth:
                if depth == 0:
                    partial_tracks.append({(new_x, new_y)})
                else:
                    path.append(cardinal)
                    partial_tracks += go_downhill([new_x, new_y], depth-1, path)
    return partial_tracks

t3 = time.time()

for _ in range(20):
    accumulator = []
    for head in trailheads:
        tracks = go_uphill(head, 1, path = [])
        accumulator.append(len(tracks))

print(sum(accumulator))
t4 = time.time()
for _ in range(20):
    accumulator = []
    for foot in trailfeet:
        tracks = go_downhill(foot, 8, path = [])
        accumulator.append(len(tracks))

print(sum(accumulator))
t5 = time.time()
print(f"Time taken uphill:{t4-t3}\nTime taken dnhill:{t5-t4}")
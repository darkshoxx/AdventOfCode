import os
HERE = os.path.dirname(__file__)
print(HERE)
INPUT_FILE = os.path.join(HERE, "input.txt")
with open(INPUT_FILE) as my_file:
    input_data = my_file.read()
    input_lines = input_data.split("\n")
print(input_lines.pop())

starting_directions = ["^","<",">","v"]

for i, row in enumerate(input_lines):
    for j, column in enumerate(row):
        if column in starting_directions:
            starting_position = [i,j]
position = starting_position[:]
print(position)

directions = {
    "N": (-1,0),
    "E": (0,1),
    "S": (1,0),
    "W": (0,-1),
}

new_directions = {
    "N": "E",
    "E": "S",
    "S": "W",
    "W": "N",
}

direction = "N"

dir_x, dir_y = directions[direction]

unique_positions = []
unique_positions.append(position)
on_the_field = True

while on_the_field:
    new_pos_x = position[0] + dir_x
    new_pos_y = position[1] + dir_y
    if new_pos_x < 0 or new_pos_x > len(input_lines[0])-1 or new_pos_y<0 or new_pos_y > len(input_lines)-1:
        on_the_field = False
    else:
        new_symbol = input_lines[new_pos_x][new_pos_y]
        if new_symbol == "#":
            direction = new_directions[direction]
            dir_x, dir_y = directions[direction]
        else:
            position = [new_pos_x, new_pos_y]
            if position not in unique_positions:
                unique_positions.append(position)
# print(unique_positions)
print(len(unique_positions))

## Part 2
accumulator = 0
unique_positions.pop(0)
for i, candidate in enumerate(unique_positions):
    on_the_field = True
    stuck_in_loop = False
    previosly_visited = []
    position = starting_position[:]
    direction = "N"
    dir_x, dir_y = directions[direction]
    previosly_visited.append([position[0], position[1], direction])
    while on_the_field and not stuck_in_loop:
        new_pos_x = position[0] + dir_x
        new_pos_y = position[1] + dir_y
        if new_pos_x < 0 or new_pos_x > len(input_lines[0])-1 or new_pos_y<0 or new_pos_y > len(input_lines)-1:
            on_the_field = False
        else:
            new_symbol = input_lines[new_pos_x][new_pos_y]
            if (new_symbol == "#") or [new_pos_x, new_pos_y] == candidate:
                direction = new_directions[direction]
                dir_x, dir_y = directions[direction]
            else:
                position = [new_pos_x, new_pos_y]
                # print([new_pos_x, new_pos_y, direction])
                # print(previosly_visited)
                if [new_pos_x, new_pos_y, direction] in previosly_visited:
                    stuck_in_loop = True
                else:
                    previosly_visited.append([position[0], position[1], direction])
    if stuck_in_loop:
        accumulator += 1

    print(f"Progress: accumulator:{accumulator}, stage {i} of {len(unique_positions)}")
print(accumulator)



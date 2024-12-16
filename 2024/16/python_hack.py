
import os
import re
import math
HERE = os.path.dirname(__file__)
print(HERE)
DRAWFILES = os.path.join(HERE, "drawfiles")
filename = "input.txt"
INPUT_FILE = os.path.join(HERE, filename)
with open(INPUT_FILE) as my_file:
    input_data = my_file.read()
    input_lines = input_data.split("\n")
print(input_lines.pop())

new_grid = [list(line) for line in input_lines]
width = len(input_lines[0])
height = len(input_lines)

for row in range(height):
    for column in range(width):
        entry = input_lines[row][column]
        if entry == "S":
            start_x, start_y = column, row
        elif entry == "E":
            end_x, end_y = column, row

def test_outside_grid(x_pos, y_pos):
    return x_pos < 0 or x_pos > width-1 or y_pos<0 or y_pos > height-1

# removing dead ens
directions = {
    "N": (0,-1),
    "S": (0,1),
    "W": (-1,0),
    "E": (1,0)
}

opposite = {
    "N": "S",
    "S": "N",
    "W": "E",
    "E": "W"
}


def plug_dead_ends():
    exit_code = False
    for row in range(height):
        for column in range(width):
            entry = new_grid[row][column]
            if entry == ".":
                neighbours = []
                for _, value in directions.items():
                    new_x, new_y = column + value[0], row + value[1]
                    neighbour_entry = new_grid[new_y][new_x]
                    neighbours.append(neighbour_entry)
                pound_list =  [i for i, val in enumerate(neighbours) if val == "#"]
                if len(pound_list) == 3:
                    exit_code = True
                    new_grid[row][column] = "#"
    return exit_code

still_fixing = True
while still_fixing:
    still_fixing = plug_dead_ends()


print_grid = ["".join(line) for line in new_grid]
drawfile_path = os.path.join(HERE, f"plugged_maze.txt")
with open(drawfile_path, "w") as drawfile:
    drawfile.write("".join("\n".join(print_grid)))                   

def available_directions(pos_x, pos_y, direction):
    neighbours = []
    for cardinal, value in directions.items():
        if cardinal != opposite[direction]:
            new_x, new_y = pos_x + value[0], pos_y + value[1]
            neighbour_entry = new_grid[new_y][new_x]
            if neighbour_entry == ".":
                neighbours.append(((new_x, new_y), cardinal))
    return neighbours

def go_to_next_node(init_x, init_y, cardinal):
    score = 0
    next_node_found = False
    movement = directions[cardinal]
    current_cardinal = cardinal
    cur_x, cur_y = init_x + movement[0], init_y + movement[1]
    score += 1
    while not next_node_found:
        possible = available_directions(cur_x, cur_y, current_cardinal)
        if len(possible) == 1:
            if possible[0][1] == current_cardinal:
                score += 1
            else: 
                score += 1001
            current_cardinal = possible[0][1]
            cur_x, cur_y = possible[0][0]
        elif possible == []:
            # E/S reached
            final_direction = directions[current_cardinal]
            next_x, next_y = (cur_x + final_direction[0], cur_y + final_direction[1])
            if not (next_x, next_y) in [(end_x, end_y), (start_x, start_y)]:
                raise Exception("YOU NO GO HERE!!!")
            score += 1
            return next_x, next_y, current_cardinal, score
        else:
            next_node_found = True
    return cur_x, cur_y, current_cardinal, score

print(start_x, start_y)
print(go_to_next_node(start_x, start_y, "E"))

# dict
# key: node_coordinates
# value: dict
#        key: direction
#        value: cheapest observed cost of direction
node_costs:dict[tuple[int,int],dict[str,int]] = {}

def explore(pos_x, pos_y, cardinal, score):
    node_x, node_y, node_card, node_score = go_to_next_node(pos_x, pos_y, cardinal)
    if (node_x, node_y) not in node_costs.keys():
        node_costs[(node_x, node_y)] = {}
    possible = available_directions(node_x, node_y, node_card)
    for possibility in possible:
        _, next_card = possibility
        potential_score = score + node_score
        if next_card != node_card:
            potential_score += 1000
        if next_card in node_costs[(node_x, node_y)].keys():
            if potential_score < node_costs[(node_x, node_y)][next_card]:
                node_costs[(node_x, node_y)][next_card] = potential_score
                explore(node_x, node_y, next_card, potential_score)
        else: 
            node_costs[(node_x, node_y)][next_card] = potential_score
            explore(node_x, node_y, next_card, potential_score)
# unexplored nodes have infinite cost
# spawn at branch of a node, if path is cheaper
# save cheapest way to move on from node
# if our path is more expesive than all the options: die
# continue_exploring = True
# while continue_exploring:
#     pass

# commented out for part 2 performance
# explore(start_x, start_y, "N", 1000)
# if filename == "input.txt":
#     explore(start_x, start_y, "E", 0)

# print(min(node_costs[(end_x, end_y)].values())-1000)


# {'S': 85444, 'W': 84444}

## Part 2

def go_to_next_node_2(init_x, init_y, cardinal, path:list):
    score = 0
    next_node_found = False
    movement = directions[cardinal]
    current_cardinal = cardinal
    cur_x, cur_y = init_x + movement[0], init_y + movement[1]
    score += 1
    path.append((cur_x, cur_y))
    while not next_node_found:
        possible = available_directions(cur_x, cur_y, current_cardinal)
        if len(possible) == 1:
            if possible[0][1] == current_cardinal:
                score += 1
            else: 
                score += 1001
            current_cardinal = possible[0][1]
            cur_x, cur_y = possible[0][0]
            path.append((cur_x, cur_y))
        elif possible == []:
            # E/S reached
            final_direction = directions[current_cardinal]
            next_x, next_y = (cur_x + final_direction[0], cur_y + final_direction[1])
            if not (next_x, next_y) in [(end_x, end_y), (start_x, start_y)]:
                raise Exception("YOU NO GO HERE!!!")
            score += 1
            return next_x, next_y, current_cardinal, score, path
        else:
            next_node_found = True
    return cur_x, cur_y, current_cardinal, score, path

node_costs:dict[tuple[int,int],dict[str,int]] = {}

def explore_2(pos_x, pos_y, cardinal, score, path:list):
    node_x, node_y, node_card, node_score, path = go_to_next_node_2(pos_x, pos_y, cardinal, path)
    if (node_x, node_y) == (end_x, end_y):
        paths_reaching_end.append((score + node_score, path))
    if (node_x, node_y) not in node_costs.keys():
        node_costs[(node_x, node_y)] = {}
    possible = available_directions(node_x, node_y, node_card)
    for possibility in possible:
        _, next_card = possibility
        potential_score = score + node_score
        if next_card != node_card:
            potential_score += 1000
        if next_card in node_costs[(node_x, node_y)].keys():
            if potential_score <= node_costs[(node_x, node_y)][next_card]:
                node_costs[(node_x, node_y)][next_card] = potential_score
                path.append((node_x, node_y))
                explore_2(node_x, node_y, next_card, potential_score, path[:])
        else: 
            node_costs[(node_x, node_y)][next_card] = potential_score
            path.append((node_x, node_y))
            explore_2(node_x, node_y, next_card, potential_score, path[:])
# unexplored nodes have infinite cost
# spawn at branch of a node, if path is cheaper
# save cheapest way to move on from node
# if our path is more expesive than all the options: die
# continue_exploring = True
# while continue_exploring:
#     pass

paths_reaching_end = []

explore_2(start_x, start_y, "N", 1000, [(start_x, start_y)])
if filename == "input.txt":
    explore_2(start_x, start_y, "E", 0, [(start_x, start_y)])

min_score = min(node_costs[(end_x, end_y)].values())-1000

candidate_tiles = []
for score, path in paths_reaching_end:
    if score == min_score:
        for i, tile in enumerate(path):
            # if i+1<len(path):
                # if tile[0] == path[i+1][0]:
                #     min_val = min(tile[1],path[i+1][1])
                #     max_val = max(tile[1],path[i+1][1])
                #     for j in range(min_val, max_val):
                #         if (tile[0], j) not in candidate_tiles:
                #             candidate_tiles.append((tile[0], j))
                # elif tile[1] == path[i+1][1]:
                #     min_val = min(tile[0],path[i+1][0])
                #     max_val = max(tile[0],path[i+1][0])
                #     for j in range(min_val, max_val):
                #         if (j, tile[1]) not in candidate_tiles:
                #             candidate_tiles.append((j, tile[1]))
                # else:
                #     raise Exception("WHAT YOU DO HERE!?!??!?!")

            if tile not in candidate_tiles:
                candidate_tiles.append(tile)
print(len(candidate_tiles))
# probably add 1, not counting final tile.
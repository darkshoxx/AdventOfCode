from functools import cache
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


def test_outside_grid(x_pos, y_pos):
    return x_pos < 0 or x_pos > width-1 or y_pos<0 or y_pos > height-1

def add_to_dict(entry, dict):
    if entry not in dict.keys():
        dict[entry] = 1
    else:
        dict[entry] +=1
    return dict



def explore_region(row, column):
    entry = input_lines[row][column]
    belonging = [(column , row)]
    new_plots = [(column , row)]
    new_plots_found = True
    while new_plots_found:
        newer_plots = []
        for plot in new_plots:
            x_pos, y_pos = plot
            # north
            if y_pos != 0:
                if input_lines[y_pos-1][x_pos] == entry:
                    north_plot = (x_pos,y_pos-1) 
                    if north_plot not in belonging:
                        belonging.append(north_plot)
                        newer_plots.append(north_plot)
            # east
            if x_pos != width - 1:
                if input_lines[y_pos][x_pos+1] == entry:
                    east_plot = (x_pos+1,y_pos) 
                    if east_plot not in belonging:
                        belonging.append(east_plot)
                        newer_plots.append(east_plot)                        
            # south
            if y_pos != height - 1:
                if input_lines[y_pos+1][x_pos] == entry:
                    south_plot =  (x_pos,y_pos+1) 
                    if south_plot not in belonging:
                        belonging.append(south_plot)
                        newer_plots.append(south_plot)                          
            # west
            if x_pos != 0:
                if input_lines[y_pos][x_pos-1] == entry:
                    west_plot = (x_pos-1,y_pos) 
                    if west_plot not in belonging:
                        belonging.append(west_plot)
                        newer_plots.append(west_plot) 
        if newer_plots == []:
            new_plots_found = False
        new_plots = newer_plots
    return belonging

# print(explore_region(0,0))
# print(len(explore_region(0,0)))

belonging_region = {}

for row in range(height):
    for column in range(width):
        if (column , row) not in belonging_region.keys():
            current_new_region = explore_region(row, column)
            region_value = current_new_region[0]
            for region in current_new_region:
                belonging_region[region] = region_value


plants_area = {}
plants_perimeter= {}


for row in range(height):
    for column in range(width):
        entry = belonging_region[(column, row)]
        add_to_dict(entry, plants_area)
        if row == 0:
            add_to_dict(entry, plants_perimeter)
        if column == 0:
            add_to_dict(entry, plants_perimeter)
        if row == height - 1:
            add_to_dict(entry, plants_perimeter)
        else:
            south_neighbour = belonging_region[(column, row+1)]
            if entry != south_neighbour:
                add_to_dict(entry, plants_perimeter)
                add_to_dict(south_neighbour, plants_perimeter)
        if column == width - 1:
            add_to_dict(entry, plants_perimeter)
        else:
            east_neighbour = belonging_region[(column+1, row)]
            if entry != east_neighbour:
                add_to_dict(entry, plants_perimeter)
                add_to_dict(east_neighbour, plants_perimeter)
print(plants_area)
# print(plants_perimeter)
# accumulator = 0
# for plant in plants_area.keys():
#     accumulator += plants_perimeter[plant] * plants_area[plant]
# print(accumulator)

## Part 2

belonging_region = {}

edges_dict: dict[tuple, dict[tuple,tuple]] = {}
# key= unique identifier of region
# value = dict
        # key: fencepiece between region and outside ((in_x, in_y),(out_x, out_y))
        # value: unique identifier of current side


def test_outside(plot):
    return test_outside_grid(plot[0], plot[1])

def explore_current_edge(in_plot, out_plot, entry, indentifier, edges_dict):
    dx = in_plot[0] - out_plot[0]
    dy = in_plot[1] - out_plot[1]
    if dy != 0:
        if dy>0:
            direction = "N"
        else:
            direction = "S"
        edges_dict[indentifier][(in_plot, out_plot)] = (in_plot[0], in_plot[1], direction)
        # go west
        continue_west = True
        west_offset = 1
        while continue_west:
            west_in = (in_plot[0] - west_offset, in_plot[1]) 
            west_out = (out_plot[0] - west_offset, out_plot[1]) 
            if not (test_outside(west_in) or test_outside(west_out)):
                if input_lines[west_in[1]][west_in[0]] == entry and input_lines[west_out[1]][west_out[0]] != entry:
                    edges_dict[indentifier][(west_in, west_out)] = (in_plot[0], in_plot[1], direction)
                    west_offset += 1
                else:
                    continue_west = False
            else:
                continue_west = False
        # go east
        continue_east = True
        east_offset = 1
        while continue_east:
            east_in = (in_plot[0]+ east_offset, in_plot[1])
            east_out = (out_plot[0]+ east_offset, out_plot[1])
            if not (test_outside(east_in) or test_outside(east_out)):
                if input_lines[east_in[1]][east_in[0]] == entry and input_lines[east_out[1]][east_out[0]] != entry:
                    edges_dict[indentifier][(east_in, east_out)] = (in_plot[0], in_plot[1], direction)
                    east_offset += 1
                else:
                    continue_east = False
            else:
                continue_east = False
    if dx != 0:
        if dx>0:
            direction = "W"
        else:
            direction = "E"
        edges_dict[indentifier][(in_plot, out_plot)] = (in_plot[0], in_plot[1], direction)
        # go north
        continue_north = True
        north_offset = 1
        while continue_north:
            north_in = (in_plot[0], in_plot[1] - north_offset)
            north_out = (out_plot[0], out_plot[1] - north_offset)
            if not (test_outside(north_in) or test_outside(north_out)):
                if input_lines[north_in[1]][north_in[0]] == entry and input_lines[north_out[1]][north_out[0]] != entry:
                    edges_dict[indentifier][(north_in, north_out)] = (in_plot[0], in_plot[1], direction)
                    north_offset += 1
                else:
                    continue_north = False
            else:
                continue_north = False                    
        # go south
        continue_south = True
        south_offset = 1
        while continue_south:
            south_in = (in_plot[0], in_plot[1] + south_offset)
            south_out = (out_plot[0], out_plot[1] + south_offset)
            if not (test_outside(south_in) or test_outside(south_out)):
                if input_lines[south_in[1]][south_in[0]] == entry and input_lines[south_out[1]][south_out[0]] != entry:
                    edges_dict[indentifier][(south_in, south_out)] = (in_plot[0], in_plot[1], direction)
                    south_offset += 1
                else:
                    continue_south = False
            else:
                continue_south = False 
    return edges_dict

def explore_region_with_edges(row, column, edges_dict):
    if (column, row) not in edges_dict.keys():
        edges_dict[(column, row)] = {}
    entry = input_lines[row][column]
    belonging = [(column , row)]
    new_plots = [(column , row)]
    new_plots_found = True
    while new_plots_found:
        newer_plots = []
        for plot in new_plots:
            x_pos, y_pos = plot
            # north
            if y_pos != 0:
                north_plot = (x_pos,y_pos-1) 
                if input_lines[y_pos-1][x_pos] == entry:
                    if north_plot not in belonging:
                        belonging.append(north_plot)
                        newer_plots.append(north_plot)
                else:
                    if (plot, north_plot) not in edges_dict[(column, row)].keys():
                        edges_dict = explore_current_edge(plot, north_plot, entry, (column, row), edges_dict)
            # east
            if x_pos != width - 1:
                east_plot = (x_pos+1,y_pos) 
                if input_lines[y_pos][x_pos+1] == entry:
                    if east_plot not in belonging:
                        belonging.append(east_plot)
                        newer_plots.append(east_plot)
                else:
                    if (plot, east_plot) not in edges_dict[(column, row)].keys():
                        edges_dict = explore_current_edge(plot, east_plot, entry, (column, row), edges_dict)                                            
            # south
            if y_pos != height - 1:
                south_plot =  (x_pos,y_pos+1) 
                if input_lines[y_pos+1][x_pos] == entry:
                    if south_plot not in belonging:
                        belonging.append(south_plot)
                        newer_plots.append(south_plot)  
                else:                        
                    if (plot, south_plot) not in edges_dict[(column, row)].keys():
                        edges_dict = explore_current_edge(plot, south_plot, entry, (column, row), edges_dict)
            # west
            if x_pos != 0:
                west_plot = (x_pos-1,y_pos) 
                if input_lines[y_pos][x_pos-1] == entry:
                    if west_plot not in belonging:
                        belonging.append(west_plot)
                        newer_plots.append(west_plot) 
                else:
                    if (plot, west_plot) not in edges_dict[(column, row)].keys():
                        edges_dict = explore_current_edge(plot, west_plot, entry, (column, row), edges_dict)
        if newer_plots == []:
            new_plots_found = False
        new_plots = newer_plots
    return edges_dict, belonging

# all on the inside
for row in range(height):
    for column in range(width):
        if (column , row) not in belonging_region.keys():
            edges_dict , current_new_region = explore_region_with_edges(row, column, edges_dict)
            region_value = current_new_region[0]
            for region in current_new_region:
                belonging_region[region] = region_value


# Reminder: 
# key= unique identifier of region
# value = dict
        # key: fencepiece between region and outside ((in_x, in_y),(out_x, out_y))
        # value: unique identifier of current side

print("HERE")
# north and south border
for row in [0, height - 1]:
    if row == 0:
        direction = "N"
    else:
        direction = "S"
    for column in range(width):
        identifier = belonging_region[(column, row)]
        if ((column, row), direction) not in edges_dict[identifier].keys():
            edges_dict[identifier][((column, row), direction)] = (column, row, direction)
            continue_east = True
            east_offset = 1
            while continue_east:
                east_plot = (column + east_offset, row)
                if column + east_offset != width:
                    if identifier == belonging_region[east_plot]:
                        edges_dict[identifier][((column+east_offset, row), direction)] = (column, row, direction)
                        east_offset +=1
                    else:
                        continue_east = False
                else:
                    continue_east = False
                    


# west and east border
for column in [0, width - 1]:
    if column == 0:
        direction = "W"
    else:
        direction = "E"
    for row in range(height):
        identifier = belonging_region[(column, row)]
        if ((column, row), direction) not in edges_dict[identifier].keys():
            edges_dict[identifier][((column, row), direction)] = (column, row, direction)
            continue_south = True
            south_offset = 1
            while continue_south:
                south_plot = (column , row+south_offset)
                if row + south_offset != height:
                    if identifier == belonging_region[south_plot]:
                        edges_dict[identifier][((column, row+south_offset), direction)] = (column, row, direction)
                        south_offset +=1
                    else:
                        continue_south = False
                else:
                    continue_south = False
print(len(edges_dict[(0,0)].keys()))
print(plants_area)
print("EDGES")
accumulator = 0
for region, regional_edges in edges_dict.items():
    # print(regional_edges)
    print(region)
    print(set(regional_edges.values()))
    print(plants_area[region])
    accumulator += plants_area[region]* len(set(regional_edges.values()))
print(accumulator)

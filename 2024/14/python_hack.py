
import os
import re
import math
HERE = os.path.dirname(__file__)
print(HERE)
INPUT_FILE = os.path.join(HERE, "input.txt")
with open(INPUT_FILE) as my_file:
    input_data = my_file.read()
    input_lines = input_data.split("\n")
print(input_lines.pop())

width = 101 #len(input_lines[0])
height = 103 #len(input_lines)

w_mid = int((width-1)/2)
h_mid = int((height-1)/2)
# width = 11 #len(input_lines[0])
# height = 7 #len(input_lines)

quadrants = [0,0,0,0]

for line in input_lines:
    line_strings = re.findall("\-?[0-9]+", line)
    line_values =  [int(item) for item in line_strings]
    x_pos, y_pos, x_vel, y_vel = line_values
    x_final = (x_pos + x_vel*100) % width
    y_final = (y_pos + y_vel*100) % height
    if x_final < w_mid:
        if y_final < h_mid:
            quadrants[0] += 1
        elif y_final > h_mid:
            quadrants[2] += 1
    elif x_final > w_mid:
        if y_final < h_mid:
            quadrants[1] += 1
        elif y_final > h_mid:
            quadrants[3] += 1
print(quadrants)
print(math.prod(quadrants))

from itertools import combinations

# Part 2
robots = []
for line in input_lines:
    line_strings = re.findall("\-?[0-9]+", line)
    line_values =  [int(item) for item in line_strings]
    x_pos, y_pos, x_vel, y_vel = line_values
    robots.append((x_pos, y_pos, x_vel, y_vel))

def conditional_draw(seconds, positions):
    if seconds not in [6668, 5226, 7799, 6255, 5431, 4814, 3681, 3989, 1003, 797, 2958, 5527, 9540, 5014, 7891, 9435, 385, 3779, 1412, 3573, 5112, 5623, 7371, 1513, 9171, 3228, 2440, 6134, 3876, 4903, 204, 7466, 7055, 2823, 4078, 3157, 8798, 486, 9660, 3463, 9924, 2746, 2232, 3522, 8278, 6327, 4380, 3051, 6018, 588, 5914, 5827, 4623, 7031, 9193, 7550, 8473, 6125, 5524, 9291, 8032, 7630, 4321, 6419, 7328, 2919, 2641, 8874, 1203, 8427, 179, 7122, 4578, 3416, 7946, 4474, 1611, 1919, 7229, 7416, 7915, 9678, 6717, 3912, 6818, 8346, 4111, 2111, 1106, 403, 8107, 4808, 4208, 9565, 1711, 893, 9805, 5204, 5004, 5685]:
        return
    draw_list = []
    for row in range(height):
        for column in range(width+1):
            if column == width:
                draw_list.append("\n")
            else:
                if (column, row) in positions:
                    draw_list.append("R")
                else:
                    draw_list.append(".")
    drawfile_path = os.path.join(HERE, f"drawing_{seconds}.txt")
    with  open(drawfile_path, "w") as drawfile:
        drawfile.write("".join(draw_list))    


observed_distances = []
for seconds in range(10000):
    positions = []
    for x_pos, y_pos, x_vel, y_vel in robots:
        x_final = (x_pos + x_vel*seconds) % width
        y_final = (y_pos + y_vel*seconds) % height
        positions.append((x_final, y_final))
    # largest_distance_of_second = 0
    conditional_draw(seconds, positions)
    distances_observed = []
    for a,b in combinations(positions,2):
        x_dist = abs(a[0] - b[0])
        y_dist = abs(a[1] - b[1])
        dist_total = (x_dist + y_dist)**2
        distances_observed.append(dist_total)
        # if dist_total > largest_distance_of_second:
        #     largest_distance_of_second = dist_total
    average_distance_of_second = sum(distances_observed)/len(distances_observed)
    # observed_distances.append(largest_distance_of_second)
    observed_distances.append(average_distance_of_second)
print(observed_distances)
smallest_distances = []
indices = []
for _ in range(100):
    my_min = min(observed_distances)
    min_index = observed_distances.index(my_min)
    indices.append(min_index)
    smallest_distances.append(observed_distances.pop(min_index))
print(indices)
print(smallest_distances)


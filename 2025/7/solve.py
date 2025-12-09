import os
HERE = os.path.abspath(os.path.dirname(__file__))
INPUT = os.path.join(HERE, "input.txt")
INPUTTEST = os.path.join(HERE, "inputtestmini.txt")
OUTPUT = os.path.join(HERE, "output.txt")
OUTPUTTEST = os.path.join(HERE, "outputtest.txt")
# Part 1
with open(INPUT, "r") as f:
    content = f.readlines()
clean_lines = [line[:-1] for line in content]

splitters_hit = 0
start_position = None
for index in range(len(clean_lines[0])):
    if clean_lines[0][index]=="S":
        start_position = index
print(start_position)
last_line = len(clean_lines)-1
current_row = 2
current_rays = [start_position]
next_rays = []
with open(OUTPUT, "w") as f:
    while current_row<=last_line:
        draw_line_1 = list(clean_lines[current_row])
        draw_line_2 = list(clean_lines[current_row+1])
        for ray in current_rays:
            if clean_lines[current_row][ray]=="^":
                splitters_hit +=1
                if ray-1 not in next_rays:
                    next_rays.append(ray-1)
                next_rays.append(ray+1)
                draw_line_1[ray-1] = "|"
                draw_line_1[ray+1] = "|"
                draw_line_2[ray-1] = "|"
                draw_line_2[ray+1] = "|"
            else:
                if ray not in next_rays:
                    next_rays.append(ray)
        current_rays = next_rays
        next_rays = []
        current_row +=2
        f.write("".join(draw_line_1))
        f.write("\n")
        f.write("".join(draw_line_2))
        f.write("\n")
print(splitters_hit)


# Part 2

def update_dict(my_dict, entry, value):
    if entry in my_dict:
        my_dict[entry] += value
    else: my_dict[entry] = value

splitters_hit = 0
start_position = None
for index in range(len(clean_lines[0])):
    if clean_lines[0][index]=="S":
        start_position = index
print("Start:", start_position)
last_line = len(clean_lines)-1
rays_per_position = {start_position:1}
next_rays_per_position = {}
current_row = 2
current_rays = [start_position]
next_rays = []
while current_row<=last_line:
    for ray in rays_per_position:
        if clean_lines[current_row][ray]=="^":
            # splitters_hit +=1
            update_dict(next_rays_per_position,ray+1,rays_per_position[ray])
            update_dict(next_rays_per_position,ray-1,rays_per_position[ray])
            next_rays_per_position[ray] = 0
        else:
            update_dict(next_rays_per_position,ray,rays_per_position[ray])
    rays_per_position = next_rays_per_position
    next_rays_per_position = {}
    current_row +=2

accumulator = 0
for value in rays_per_position.values():
    accumulator += value
print("Total:", accumulator)


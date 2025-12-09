import os
HERE = os.path.abspath(os.path.dirname(__file__))
INPUT = os.path.join(HERE, "input.txt")
INPUTTEST = os.path.join(HERE, "inputtestmini.txt")
# Part 1
with open(INPUT, "r") as f:
    content = f.readlines()
clean_lines = [line[:-1] for line in content]

points = [tuple(map(int, item.split(","))) for item in clean_lines]
print(points)
def dist(p1,p2):
    return sum([(p1[index] - p2[index])**2 for index in range(3)])

print(dist([1,2,3],[4,5,6]))
from itertools import combinations

def update_list(my_big_list, entry): # biglist:[curr_max_index, [dist_0, dist_1,..]] # entry: newdist
    max_index = my_big_list[0]
    my_list = my_big_list[1]
    if len(my_list)<500:
        my_list.append(entry)
        if entry>my_list[max_index]:
            my_big_list = [len(my_list)-1, my_list]
        else:
            my_big_list = [max_index, my_list]
    else:
        if entry>my_list[max_index]:
            pass
        else:
            my_list[max_index] = entry
            my_big_list = [max_index, my_list]



total = len(points)
list_dict = {}
for combo in combinations(list(range(total)), 2):
    dis = dist(points[combo[0]], points[combo[1]])
    if combo[0] not in list_dict:
        list_dict[combo[0]] = [0, [dis]]
    else:
        update_list(list_dict[combo[0]], dis)
    if combo[1] not in list_dict:
        list_dict[combo[1]] = [0, [dis]]
    else:
        update_list(list_dict[combo[1]], dis)

print(list_dict)

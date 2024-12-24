
from collections import defaultdict
import os
import re
import math

from time import sleep


from functools import cache
HERE = os.path.dirname(__file__)
print(HERE)
DRAWFILES = os.path.join(HERE, "drawfiles")
filename = "input.txt"
INPUT_FILE = os.path.join(HERE, filename)

with open(INPUT_FILE) as my_file:
    input_data = my_file.read()
    input_lines = input_data.split("\n")
print(input_lines.pop())

connections = []
t_connections:dict[str, list] = {}
for line in input_lines:
    left, right = line.split("-")
    connections.append({left, right})
    if left[0] == "t":
        if left in t_connections.keys():
            t_connections[left].append(right)
        else:
            t_connections[left] = [right]
    if right[0] == "t":
        if right in t_connections.keys():
            t_connections[right].append(left)
        else:
            t_connections[right] = [left]

from itertools import combinations

triplets = set()
for key, value in t_connections.items():
    for pair in combinations(value, 2):
        if {pair[0], pair[1]} in connections:
            triplets.add(frozenset({key, pair[0], pair[1]}))


# Part 2

connections = []
g_connections:dict[str,list] = {}
for line in input_lines:
    left, right = line.split("-")
    connections.append({left, right})
    if left in g_connections.keys():
        g_connections[left].append(right)
    else:
        g_connections[left] = [right]

    if right in g_connections.keys():
        g_connections[right].append(left)
    else:
        g_connections[right] = [left]



triplets = set()
for key, value in g_connections.items():
    for pair in combinations(value, 2):
        if {pair[0], pair[1]} in connections:
            triplets.add(frozenset({key, pair[0], pair[1]}))


def increase_sets(n_set, ruled_out:set):
    addition_candidates = set(key for key in g_connections.keys()) - ruled_out
    for item in n_set:
        addition_candidates = addition_candidates.intersection(set(g_connections[item]))
    return addition_candidates

from copy import copy
def find_group_max(n_set:set, group_max, ruled_out:set=set()):
    candidates = increase_sets(n_set, ruled_out)
    group_max = max(group_max, len(n_set))
    if not candidates:
        if group_max == 13:
            global best
            best = n_set
        return group_max
    # ruled_out = set()
    values = []
    for candidate in candidates:
        copied_set = copy(n_set)
        copied_set.add(candidate)
        copied_rule_out = copy(ruled_out)
        value = find_group_max(copied_set, group_max+1, copied_rule_out)
        values.append(value)
        ruled_out.add(candidate)
    return max(values)
best = set()
values = []
# for triplet in triplets:
ruled_out = set()
for entry in g_connections.keys():
    triplet = {entry}
    group_max = 1
    new_val = find_group_max(set(triplet), group_max, copy(ruled_out))
    ruled_out.add(entry)
    values.append(new_val)
    print(new_val)
print("MAX GROUP:", max(values))
print(values)
print(best)
print(",".join(sorted(list(best))))
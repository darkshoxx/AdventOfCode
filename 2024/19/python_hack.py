
from collections import defaultdict
import os
import re
import math

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

first, last = input_data.split("\n\n")
towels = first.split(", ")
patterns = last.split("\n")
patterns.pop()
def list_to_regex(my_list):
    stringlist = []
    stringlist.append("^(")
    for i, string in enumerate(my_list):
        if i != 0:
            stringlist.append("|")
        stringlist.append(f"({string})")
    stringlist.append(")*$")
    regex = "".join(stringlist)
    return regex
regex = list_to_regex(towels)
print(regex)
sorted_towels = sorted(towels, key=len)
print(sorted_towels)
atomic_towels = []
for towel in sorted_towels:
    atomic_regex = list_to_regex(atomic_towels)
    towel_molecule = bool(re.match(atomic_regex, towel))
    if not towel_molecule:
        atomic_towels.append(towel)
print(atomic_towels)
atomic_towel_regex = list_to_regex(atomic_towels)
accumulator = 0
for line in patterns:
    val = re.match(atomic_towel_regex ,line)
    if val:
        accumulator += 1

print(accumulator)

# part 2
possible_patterns = []
for line in patterns:
    val = re.match(atomic_towel_regex ,line)
    if val:
        possible_patterns.append(line)

my_dict = {
    'g':[],
    'u':[],
    'b':[],
    'r':[],
    'w':[],
           }
for towel in sorted_towels:
    first_letter = towel[0]
    my_dict[first_letter].append(towel)
print(my_dict)

@cache
def find_decompositions(search_string):
    if search_string == '':
        return 1
    total_found = 0
    for word in my_dict[search_string[0]]:
        if search_string[:len(word)] == word:
            total_found += find_decompositions(search_string[len(word):])
    return total_found

accumulator = 0
for pattern in possible_patterns:
    accumulator += find_decompositions(pattern)
print(accumulator)

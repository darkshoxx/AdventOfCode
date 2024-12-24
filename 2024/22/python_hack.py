
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

def prune(number):
    return number % 16777216

def mix(value, secret_number):
    return value ^ secret_number

def step(secret_number, factor):
    value = int(secret_number * factor)
    secret_number = mix(value, secret_number)
    secret_number = prune(secret_number)
    return secret_number

def advance(secret_number):
    secret_number = step(secret_number, 64)
    secret_number = step(secret_number, 1/32)
    secret_number = step(secret_number, 2048)
    return secret_number

# accumulator = 0
# for line in input_lines:
#     secret_number = int(line)
#     for _ in range(2000):
#         secret_number = advance(secret_number)
#     print(secret_number)
#     accumulator += secret_number
# print("ACCUMULATOR:", accumulator)

# print(advance(123))

## Part 2
banana_dict = {}
# dict key:line index
#      value: dict: key: 4-tuple of changes
#                   value: resulting price

from queue import Queue
from collections import defaultdict

for i, line in enumerate(input_lines):
    secret_number = int(line)
    my_queue = Queue(maxsize=4)
    current_banana_dict = defaultdict(lambda: 0)
    previous_remainder = None
    for _ in range(2000):
        secret_number = advance(secret_number)
        remainder = secret_number % 10
        if previous_remainder is not None:
            diff = remainder - previous_remainder
            my_queue.put_nowait(diff)
            if my_queue.full():
                queue_tuple = tuple(my_queue.queue)
                if queue_tuple not in current_banana_dict.keys():
                    current_banana_dict[queue_tuple] = remainder
                my_queue.get_nowait()
        previous_remainder = remainder
    print(i)
    banana_dict[i] = current_banana_dict
all_keys = {key for cur_dict in banana_dict.values()
            for key in cur_dict
            }
current_best = 0
for key in all_keys:
    accumulator = 0
    for _, value in banana_dict.items():
        accumulator += value[key]
    if accumulator > current_best:
        current_best = accumulator
        print("CURRENT_BEST:", current_best)
        print("CURRENT_KEY:", key)
print("OPTIMUM:",current_best)




        
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
import math

starting_stones = [int(item) for item in input_lines[0].split(" ")]
print(starting_stones)

def num_of_digits(num):
    return math.floor(math.log10(num)+1)

t0 = time.time()

def stones_after_n_blinks(stone, blinks):
    if blinks == 0:
        return 1
    if stone == 0:
        return stones_after_n_blinks(1, blinks - 1)
    else:
        digits = num_of_digits(stone)
        if not (digits % 2):
            right = int(stone % 10**(digits/2))
            left = int((stone - right)/(10**(digits/2)))
            return stones_after_n_blinks(left, blinks - 1) + stones_after_n_blinks(right, blinks - 1)
        else:
            return stones_after_n_blinks(stone*2024, blinks - 1)
            
accumulator = 0
for stone in starting_stones:
    accumulator += stones_after_n_blinks(stone, 25)

print(accumulator)

t1 = time.time()
## part 2 with manual cache

from collections import defaultdict
starting_stones = [int(item) for item in input_lines[0].split(" ")]
print(starting_stones)
known_solutions = defaultdict(lambda: defaultdict(lambda: None))

t2 = time.time()

def add_to_double_default(stone, blinks, result):
    if stone in known_solutions.keys():
        known_solutions[stone][blinks] = result
    else:
        known_solutions[stone] = defaultdict(lambda: None)

def stones_after_n_blinks(stone, blinks):
    if blinks == 0:
        return 1
    if stone == 0:
        return stones_after_n_blinks(1, blinks - 1)
    else:
        digits = num_of_digits(stone)
        if not (digits % 2):
            right = int(stone % 10**(digits/2))
            left = int((stone - right)/(10**(digits/2)))
            left_result = known_solutions[left][blinks-1]
            if left_result is None:
                left_result = stones_after_n_blinks(left, blinks - 1)
                add_to_double_default(left, blinks-1, left_result)
            right_result = known_solutions[right][blinks-1]
            if right_result is None:
                right_result = stones_after_n_blinks(right, blinks - 1)
                add_to_double_default(right, blinks-1, right_result)
            return left_result + right_result
        else:
            product = stone*2024
            result = known_solutions[product][blinks-1]
            if result is None:
                result = stones_after_n_blinks(product, blinks - 1)
                add_to_double_default(product, blinks-1, result)
            return result
            
accumulator = 0
for stone in starting_stones:
    print(stone)
    accumulator += stones_after_n_blinks(stone, 75)
print(accumulator)
t3 = time.time()

## Part 2 with functools cache

t4 = time.time()

@cache
def stones_after_n_blinks(stone, blinks):
    if blinks == 0:
        return 1
    if stone == 0:
        return stones_after_n_blinks(1, blinks - 1)
    else:
        digits = num_of_digits(stone)
        if not (digits % 2):
            right = int(stone % 10**(digits/2))
            left = int((stone - right)/(10**(digits/2)))
            return stones_after_n_blinks(left, blinks - 1) + stones_after_n_blinks(right, blinks - 1)
        else:
            return stones_after_n_blinks(stone*2024, blinks - 1)
            
accumulator = 0
for stone in starting_stones:
    accumulator += stones_after_n_blinks(stone, 75)

print(accumulator)
t5=time.time()

print(f"Part 1 Uncached:{t1-t0}\nPart 2 Mncached:{t3-t2}\nPart 2 Pycached:{t5-t4}")
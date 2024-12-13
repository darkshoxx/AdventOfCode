
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

width = len(input_lines[0])
height = len(input_lines)

token_accumulator = 0
machines=input_data.split("\n\n")
singularities = []
for machine in machines:

    machine_lines = [lines for lines in machine.split("\n") if lines]
    machine_numbers = []
    for line in machine_lines:
        machine_numbers += re.findall("[0-9]+", line)
    numbers = [int(number) for number in machine_numbers]


    # find n_a, n_b such that
    # n_a* a_x + n_b*b_x = X
    # n_a* a_y + n_b*b_y = Y 
    #     (a_x a_y)      (X)    (n_a)
    # A = (b_x b_y)  G = (Y) N= (n_b)
    # solve N*A = G for N
    # N = G*A^-1
    import numpy as np

    A = np.array([[numbers[0], numbers[1]],[numbers[2], numbers[3]]])
    G = np.array([numbers[4], numbers[5]])

    def sizetest(n):
        return abs(n)<1e-10

    def n_test(N):
        return (0 < N[0] < 100 
            and 0 < N[1] < 100 
            and sizetest(N[0] - round(N[0]))
            and sizetest(N[1] - round(N[1]))
            )

    if sizetest(np.linalg.det(A)):
        singularities.append(machine)
        tokens = 0
    else:
        A_inv = np.linalg.inv(A)
        N = np.matmul(G,A_inv)
        # print(N)
        if n_test(N):
            tokens = 3*N[0] + N[1]
        else:
            tokens = 0
    # print(tokens)
    token_accumulator += round(tokens)
print(token_accumulator)
# print(singularities)



# Part 2
def sizetest(n):
    return abs(n)<1e-10

def n_test(N):
    return (0 < N[0]
        and 0 < N[1]
        and sizetest(N[0] - round(N[0]))
        and sizetest(N[1] - round(N[1]))
        )
import mpmath as mp
mp.mp.dps = 30
token_accumulator = 0
for machine in machines:

    machine_lines = [lines for lines in machine.split("\n") if lines]
    machine_numbers = []
    for line in machine_lines:
        machine_numbers += re.findall("[0-9]+", line)
    numbers = [int(number) for number in machine_numbers]

    numbers[4] +=10000000000000
    numbers[5] +=10000000000000


    A = mp.mp.matrix([[numbers[0], numbers[1]],[numbers[2], numbers[3]]])
    G = mp.mp.matrix([numbers[4], numbers[5]])


    if sizetest(mp.mp.det(A)):
        singularities.append(machine)
        tokens = 0
    else:
        A_inv = A**-1
        N = G.T*A_inv
        # print(N)
        if n_test(N):
            tokens = 3*N[0] + N[1]
        else:
            tokens = 0
    # print(tokens)
    token_accumulator += round(tokens)
print(token_accumulator)

# dps 15: 83551068361379
# dps 20: 83551068361379

if False:
    b_ratio_x = numbers[4]/numbers[2]
    b_ratio_y = numbers[5]/numbers[3]
    print(b_ratio_x, b_ratio_y)
    if(b_ratio_x>b_ratio_y):
        smaller = b_ratio_y
        # larger = b_ratio_y
    else:
        smaller = b_ratio_x
        # larger = b_ratio_x
    print(smaller)
    max_b = math.floor(smaller)
    print(max_b)

    def calculate(cur_a, cur_b, numbers):
        prize = True
        prize = prize and (cal_x(cur_a, cur_b, numbers)==numbers[4])
        prize = prize and (cal_y(cur_a, cur_b, numbers)==numbers[5])
        return prize

    def cal_x(cur_a, cur_b, numbers):
        return cur_a*numbers[0] + cur_b*numbers[2]

    def cal_y(cur_a, cur_b, numbers):
        return cur_a*numbers[1] + cur_b*numbers[3]

    current_b = max_b
    current_a = 0
    tokens = 0
    keep_going = True
    while keep_going:
        if calculate(current_a, current_b, numbers):
            tokens = current_a + current_b
            break
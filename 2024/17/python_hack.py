
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

numbers = []
for line in input_lines:

    line_strings = re.findall("\-?[0-9]+", line)
    numbers.append(line_strings)

reg_a = int(numbers[0][0])
reg_b = int(numbers[1][0])
reg_c = int(numbers[2][0])
program = [int(item) for item in numbers[4]]



class Computer:

    def __init__(self, reg_a, reg_b, reg_c, program):
        self.sigfig = 16
        self.init_a = reg_a
        self.reg_a = reg_a
        self.reg_b = reg_b
        self.reg_c = reg_c
        self.program = program
        self.output = []
        self.pointer = 0
        self.opcodes = {
            0:self.adv,
            1:self.bxl,
            2:self.bst,
            3:self.jnz,
            4:self.bxc,
            5:self.out,
            6:self.bdv,
            7:self.cdv,
        }
    
    def combo(self, operand):
        if 0 <= operand < 4:
            return operand
        elif operand == 4:
            return self.reg_a 
        elif operand == 5:
            return self.reg_b 
        elif operand == 6:
            return self.reg_c 
        else:
            raise Exception("HOW YOU GET HERE? ILLEGAL!")
             

    def adv(self, operand):
        self.reg_a = math.floor(self.reg_a / (2**self.combo(operand)))
        self.pointer += 2 
    
    def bxl(self, operand):
        self.reg_b = self.reg_b ^ operand
        self.pointer += 2 

    def bst(self, operand):
        self.reg_b = self.combo(operand)%8
        self.pointer += 2 
    
    def jnz(self, operand):
        if self.reg_a != 0:
            self.pointer = operand
        else:
            self.pointer += 2 

    def bxc(self, operand):
        self.reg_b = self.reg_b ^ self.reg_c
        self.pointer += 2 

    def out(self, operand):
        self.output.append(self.combo(operand)%8)
        self.pointer += 2 

    def bdv(self, operand):
        self.reg_b = math.floor(self.reg_a / (2**self.combo(operand)))
        self.pointer += 2 

    def cdv(self, operand):
        self.reg_c = math.floor(self.reg_a / (2**self.combo(operand)))
        self.pointer += 2 

    def run(self):
        while True:
            if self.pointer >= len(self.program):
                return self.output
            else:
                opcode = self.program[self.pointer]
                operand = self.program[self.pointer + 1]
                self.opcodes[opcode](operand)
# reg_a = 2503159374167055
#2503159374167055
#251359560481807
# "0b1000111001001001110000110101010100000011110000001111"
# for a in [0, 1]:
#     for b in [0, 1]:
#         for c in [0, 1]:
#             reg_a = int(f"0b{a}{b}{c}01001001110000110101010100000011110000001111", 2)
#             part_1 = Computer(reg_a, reg_b, reg_c, program)
#             output = [str(item) for item in part_1.run()]
#             print(",".join(output))

reg_a = 251359560481807
part_1 = Computer(reg_a, reg_b, reg_c, program)
output = [str(item) for item in part_1.run()]
print(",".join(output))
# part 2



class Computer2(Computer):

    def compare(self):
        if len(self.output) == self.sigfig:
            if self.program[:len(self.output)] == self.output:
                return True

    def run(self):
        while True:
            if self.pointer >= len(self.program):
                # print(self.output)
                # print(self.program)
                # print(self.init_a)
                return self.output == self.program
            else:
                if self.pointer == 0:
                    # if self.compare():
                    #     print(self.init_a)
                    #     return self.output
                    pass
                opcode = self.program[self.pointer]
                operand = self.program[self.pointer + 1]
                self.opcodes[opcode](operand)

    def reset(self, init_a, reg_b, reg_c):
        self.init_a = init_a
        self.reg_a = init_a
        self.reg_b = reg_b
        self.reg_c = reg_c
        self.output = []
        self.pointer = 0

    def set_sigfig(self, number):
        self.sigfig = number
value_found = False


# starting_bits = bin(0)
# figures = len(starting_bits) - 2
# chunks = math.floor(figures / 3)
# starter = "0o"
# carry_string = ""
# number_found = False
# while not number_found:
#     next_found = False
#     runner = 0
#     while not next_found:
#         test_number = int(starter +  carry_string + bin(runner)[2:] ,2)
#         part_2 = Computer(test_number, 0, 0, program)
#         output = part_2.run()
#         if output == program:
#             print(f"HERE:{test_number}\n{output}\n{program}")
#         if chunks < 13:
#             if output[-(chunks+1):] == program[-(chunks+1):]:
#                 next_found = True
#                 lead_zeroes = 8- (len(bin(runner))-2) +16
#                 carry_string =  carry_string + ("0"*lead_zeroes +bin(runner)[2:])[-3:]
#                 figures = len(carry_string)
#                 chunks = math.floor(figures / 3)
#                 if chunks == 16:
#                     number_found = True
#             else:
#                 runner += 1
#         else:
#             # print(f"CURRENT:{test_number}\n{output}\n{program}")
#             print(bin(test_number))
#             runner += 1
#             if runner == 1024:
#                 raise Exception
# print(int(starter + bin(runner)[2:] + carry_string ,2))
test_number = 190384615275535
argh= Computer(test_number, 0, 0, program)
print(argh.run())



# starting_bits = bin(0)
# figures = len(starting_bits) - 2
# chunks = math.floor(figures / 3)
# starter = "0b"
# carry_string = ""
# number_found = False
# while not number_found:
#     next_found = False
#     runner = 0
#     while not next_found:
#         test_number = int(starter +  carry_string + bin(runner)[2:] ,2)
#         part_2 = Computer(test_number, 0, 0, program)
#         output = part_2.run()
#         if output == program:
#             print(f"HERE:{test_number}\n{output}\n{program}")
#         if chunks < 13:
#             if output[-(chunks+1):] == program[-(chunks+1):]:
#                 next_found = True
#                 lead_zeroes = 8- (len(bin(runner))-2) +16
#                 carry_string =  carry_string + ("0"*lead_zeroes +bin(runner)[2:])[-3:]
#                 figures = len(carry_string)
#                 chunks = math.floor(figures / 3)
#                 if chunks == 16:
#                     number_found = True
#             else:
#                 runner += 1
#         else:
#             # print(f"CURRENT:{test_number}\n{output}\n{program}")
#             print(bin(test_number))
#             runner += 1
#             if runner == 1024:
#                 raise Exception
# print(int(starter + bin(runner)[2:] + carry_string ,2))
# test_number = 15119566326021135
# argh= Computer(test_number, 0, 0, program)
# print(argh.run())

# starting_bits = bin(0)
# figures = len(starting_bits) - 2
# chunks = math.floor(figures / 3)
# starter = "0b"
# carry_string = ""
# number_found = False
# while not number_found:
#     next_found = False
#     runner = 0
#     while not next_found:
#         test_number = int(starter + bin(runner)[2:] + carry_string ,2)
#         part_2 = Computer(test_number, 0, 0, program)
#         output = part_2.run()
#         if output == program:
#             print(f"HERE:{test_number}\n{output}\n{program}")
#         if chunks < 13:
#             if output[:chunks+1] == program[:chunks+1]:
#                 next_found = True
#                 lead_zeroes = 8- (len(bin(runner))-2) +16
#                 carry_string = ("0"*lead_zeroes +bin(runner)[2:])[-3:] + carry_string
#                 figures = len(carry_string)
#                 chunks = math.floor(figures / 3)
#                 if chunks == 16:
#                     number_found = True
#             else:
#                 runner += 1
#         else:
#             # print(f"CURRENT:{test_number}\n{output}\n{program}")
#             print(bin(test_number))
#             runner += 1
#             if runner == 1024:
#                 raise Exception
# print(int(starter + bin(runner)[2:] + carry_string ,2))
# test_number = 15119566326021135
# argh= Computer(test_number, 0, 0, program)
# print(argh.run())

# starting_bits = bin(0)
# figures = len(starting_bits) - 2
# chunks = math.floor(figures / 3)
# starter = "0b"
# carry_string = ""
# number_found = False
# while not number_found:
#     next_found = False
#     for runner in range(1024):
#         if not next_found:
#             test_number = int(starter + bin(runner)[2:] + carry_string ,2)
#             part_2 = Computer(test_number, 0, 0, program)
#             output = part_2.run()
#             if output == program[:chunks+1]:
#                 next_found = True
#                 lead_zeroes = 8- (len(bin(runner))-2)
#                 carry_string = ("0"*lead_zeroes +bin(runner)[2:])[5:] + carry_string
#                 figures = len(carry_string)
#                 chunks = math.floor(figures / 3)
#                 if chunks == 16:
#                     number_found = True
# print(int(starter + bin(runner)[2:] + carry_string ,2))


# init_val = 281474976710657
# starting_bits =                      0b011110000001111
# starting_bits =                   0b000011110000001111
# starting_bits =                0b011000011110000001111
# starting_bits =           0b010000100101010011000011110000001111
# starting_bits =              0b000100101010011000011110000001111
# starting_bits = 0b0
# starting_bits =                    0b101010100000011110000001111
# starting_bits =           0b110000101101010100000011110000001111
# starting_bits = 251359560481807
# solution     "0b101011010010011101011111010111010011110000001111"
# init_val = starting_bits
# part_2 = Computer2(init_val, reg_b, reg_c, program)
# sigfig = 15
# part_2.set_sigfig(16)
# while not value_found:
#     output = part_2.run()
#     if output:
#         print(output)
#         value_found = True
#     else:
#         init_val += 2**(3*sigfig)
#         # print(bin(2**(3*sigfig)))
#         part_2.reset(init_val, reg_b, reg_c)

# while not value_found:
#     if (init_val%1000000 == 0):
#         print(init_val)
#     if part_2.run():
#         value_found = True
#     else:
#         init_val += 1
#         part_2.reset(init_val, reg_b, reg_c)
# print("RESULT:", init_val)

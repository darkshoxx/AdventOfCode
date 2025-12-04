import os
HERE = os.path.abspath(os.path.dirname(__file__))
INPUT = os.path.join(HERE, "input.txt")
INPUTTEST = os.path.join(HERE, "inputtest.txt")
# Part 1
with open(INPUT, "r") as f:
    content = f.readlines()
cleanlines = [line[:-1] for line in content]

def safe_get(x,y,content):
    if 0 <= x < len(content[0]):
        if 0 <= y < len(content):
            return content[y][x]
    return ""
# Part 1
print(cleanlines)
lines = cleanlines[:]
accumulator = 0
for y, row in enumerate(cleanlines):
    for x, entry in enumerate(row):
        if entry == "@":
            neighbours = 0
            for dx in [-1,0,1]:
                for dy in [-1, 0, 1]:
                    if dx or dy: # not both zero
                        if safe_get(x+dx,y+dy,cleanlines) in ["@", "x"]:
                            neighbours +=1
            if neighbours < 4:
                accumulator +=1
                my_list = list(cleanlines[y])
                my_list[x] = "x"
                cleanlines[y] = "".join(my_list)

print(accumulator)

# Part 2
removing = True
accumulator = 0
while removing:
    removing = False
    for y, row in enumerate(lines):
        for x, entry in enumerate(row):
            if entry == "@":
                neighbours = 0
                for dx in [-1,0,1]:
                    for dy in [-1, 0, 1]:
                        if dx or dy: # not both zero
                            if safe_get(x+dx,y+dy,lines) == "@":
                                neighbours +=1
                if neighbours < 4:
                    accumulator +=1
                    my_list = list(lines[y])
                    my_list[x] = "."
                    lines[y] = "".join(my_list)
                    removing = True

print(accumulator)
print()
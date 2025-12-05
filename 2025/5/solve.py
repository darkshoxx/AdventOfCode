import os
HERE = os.path.abspath(os.path.dirname(__file__))
INPUT = os.path.join(HERE, "input.txt")
INPUTTEST = os.path.join(HERE, "inputtest.txt")
# Part 1
with open(INPUT, "r") as f:
    content = f.readlines()
cleanlines = [line[:-1] for line in content]

# Part 1

ranger = True
ranges = []
candidates = []
for line in cleanlines:
    if ranger:
        if line=="":
            ranger = False
        else:
            first, last = line.split("-")
            ranges.append((int(first), int(last)))
    else:
        candidates.append(int(line))

print(ranges)
print(candidates)
accumulator = 0
for candidate in candidates:
    found = False
    for first, last in ranges:
        if not found:
            if first <= candidate <= last:
                accumulator +=1
                found = True
print(accumulator)

# Part 2
total = len(ranges)
index_sets_dict = {index:set() for index in range(len(ranges))}
for base_index, (base_first, base_last) in enumerate(ranges):
    for test_index, (test_first, test_last) in enumerate(ranges):
        if base_first<=test_first<=base_last or base_first<=test_last<=base_last:
            index_sets_dict[base_index].add(test_index)
            # for index in index_sets_dict[test_index]:
            #     index_sets_dict[index].add(base_index)

# I comment out the brute force of shame, but
# it shall be on display as a memorial 
# for _ in range(300): 
for index, value_set in index_sets_dict.items():
    processing_set = set([index])
    processing = True
    while processing:
        processing = False
        for item in value_set.difference(processing_set):
            processing_set.add(item)
            processing = True
            for value in index_sets_dict[item]:
                processing_set.add(value)
    for item in value_set:
        index_sets_dict[item] = processing_set


# Test that for every index, for every item in it's value set has the value set as value set
trues = 0
falses = 0
for index, value_set in index_sets_dict.items():
    for item in value_set:
        if index_sets_dict[item] == value_set:
            trues +=1
        else:
            falses +=1

print("Trues:  ", trues)
print("Falses: ", falses)

# print(index_sets_dict)
indices_used = []
final_ranges = []
for key, value in index_sets_dict.items():
    if key not in indices_used:
        indices_used += list(value)
        lower = min([ranges[item][0] for item in value])
        upper = max([ranges[item][1] for item in value])
        final_ranges.append((lower, upper))
# print(final_ranges)
# print(len(final_ranges))

accumulator = 0
for first, last in final_ranges:
    accumulator += last - first +1

print("current:  ", accumulator)
print("previous: ", 342018167474526)
import os
HERE = os.path.dirname(__file__)
print(HERE)
INPUT_FILE = os.path.join(HERE, "input.txt")
with open(INPUT_FILE) as my_file:
    input_data = my_file.read()
    input_lines = input_data.split("\n")
print(input_lines.pop())

def get_id(index):
    if (index%2==1):
        raise Exception("Invalid Parity for ID")
    return int(index/2)

def get_next_backwalker_skips(backwalker):
    if (backwalker%2==0):
        return int(input_lines[0][backwalker-1])
    raise Exception("Invalid Parity for backwalker")

def get_next_backwalker(backwalker):
    if (backwalker%2==0):
        return int(input_lines[0][backwalker])*[get_id(backwalker)]
    raise Exception("Invalid Parity for backwalker")
    return int(input_lines[0][backwalker-1])*get_id(backwalker-1)
    
    
def get_next_block_length(index):
      return int(input_lines[0][index])

total_length = len(input_lines[0])
print(total_length)
checksum = 0
backwalker = total_length-1
backwalker_buffer = []
map_position = -1
current_block_length = 0
block_position = 0
pre_checksum_list = []
backwalker_block = -1
for index, entry in enumerate(input_lines[0]):
    backwalker_block += int(entry)
while map_position < backwalker:
    if abs(map_position- backwalker)<5:
        print(block_position, backwalker_block, current_id)
    if backwalker_buffer == []:
        backwalker_buffer = get_next_backwalker(backwalker)
        backwalker_block -= get_next_backwalker_skips(backwalker)
        backwalker = backwalker - 2
    if current_block_length == 0:
        map_position += 1
        current_block_length = get_next_block_length(map_position)
        if current_block_length == 0:
            map_position += 1
            # block_position += 1
            current_block_length = get_next_block_length(map_position)
    if (map_position %2==0):
        current_id = get_id(map_position)
        checksum += current_id*block_position
        pre_checksum_list.append(str(current_id))
        block_position +=1
        current_block_length -=1
    else:
        current_id = backwalker_buffer.pop()
        backwalker_block -= 1
        checksum += current_id*block_position
        pre_checksum_list.append(str(current_id))
        block_position +=1
        current_block_length -=1
if (map_position % 2 ==0):
    while current_block_length != 0:
        current_id = get_id(map_position)
        checksum += current_id*block_position
        pre_checksum_list.append(str(current_id))
        block_position +=1
        current_block_length -=1

while backwalker_buffer != []:
    current_id = backwalker_buffer.pop()
    backwalker_block -= 1
    checksum += current_id*block_position
    pre_checksum_list.append(str(current_id))
    block_position +=1
    current_block_length -=1    
# print(map_position, backwalker, current_id)
# print(block_position, backwalker_block, current_id)
# check_string = "".join(pre_checksum_list)
# print(checksum)

## Part 2
checksum = 0
backwalker = total_length-1
backwalker_buffer = []
map_position = -1
current_block_length = 0
block_position = 0
backwalker_block = -1
for index, entry in enumerate(input_lines[0]):
    backwalker_block += int(entry)


id_list_2 = []
# populate the id_lists
for index, entry in enumerate(input_lines[0]):
    block_lenght = int(entry)
    if (index %2 == 0):
        block_id = get_id(index)
        for offset in range(block_lenght):
            id_list_2.append(block_id)
    else:
        for offset in range(block_lenght):
            id_list_2.append(".")

def find_first_dot_streak_before(my_list, length, before):
    current_streak = 0
    for index, entry in enumerate(my_list):
        if index > before:
            return None
        if entry == ".":
            current_streak += 1
            if current_streak == length:
                return index - length + 1
        else:
            current_streak = 0
    return None

def replace_id_with_dot(my_list, id):
    for index in range(len(my_list)):
        if my_list[index] == id:
            my_list[index] = "."
    return my_list

print("Check :No None's", None not in id_list_2)
print(id_list_2)
print(input_lines[0])
while backwalker > 0:
    if backwalker % 2 == 0:
        current_id = get_id(backwalker)
        backwalker_length = int(input_lines[0][backwalker])
        streak = find_first_dot_streak_before(id_list_2, backwalker_length, backwalker_block)
        if streak is not None:
            id_list_2 = replace_id_with_dot(id_list_2, current_id)
            for index in range(backwalker_length):
                id_list_2[streak + index] = current_id
        backwalker_block -= backwalker_length
    else:
        backwalker_length = int(input_lines[0][backwalker])
        backwalker_block -= backwalker_length

    backwalker -= 1
id_list_2_strings = [str(item) for item in id_list_2]
# print("".join(id_list_2_strings))
checksum = 0 
for index in range(len(id_list_2)):
    entry = id_list_2[index] 
    if entry == ".":
        entry = 0
    checksum += index*entry
print("Checksum is")
print(checksum)







# while map_position < backwalker:
#     pass
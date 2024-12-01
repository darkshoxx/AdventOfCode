# To load:
# source("C:/code/AdventOfCode/2024/1/r_hack.r")
path_to_dir = "C:/code/AdventOfCode/2024/1/"
input_file = "input.txt"
filename = paste(path_to_dir, input_file, sep="")
input = read.table(file=filename)
row_length = nrow(input)
left = sort(input[,1])
right = sort(input[,2])
result = sum(abs(left-right))
print(result)
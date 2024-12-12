print("Hello, World!")

function readAll(file)
    local f = assert(io.open(file, "rb"))
    local content = f:read("*all")
    f:close()
    return content
end

function num_of_digits(num)
    return math.floor(math.log10(num)+1)
end

function get_right(num)
    local num_dig = num_of_digits(num)
    local right  = math.floor(num % 10^(num_dig/2))
    local left = math.floor((num - right)/(10^(num_dig/2)))
    return left
end



print(get_right(123456))

function stones_after_n_blinks(stone, blinks)
    if blinks == 0 then
        return 1
    end
    if stone == 0 then
        return stones_after_n_blinks(1, blinks - 1)
    else
        digits = num_of_digits(stone)
        if digits % 2 == 0 then
            local right  = math.floor(stone % 10^(digits/2))
            local left = math.floor((stone - right)/(10^(digits/2)))            
            return stones_after_n_blinks(left, blinks - 1) + stones_after_n_blinks(right, blinks - 1)
        else
            return stones_after_n_blinks(stone*2024, blinks - 1)
        end
    end
end

local my_string = readAll("input.txt")
print(my_string)

local t = {}
local sep = " "
for str in string.gmatch(my_string, "([^"..sep.."]+)") do
    table.insert(t, tonumber(str))
end

local accumulator = 0
for index=1,8 do
    print(t[index])
    accumulator = accumulator + stones_after_n_blinks(t[index], 25)
end
print(accumulator)
print("Goodbye")
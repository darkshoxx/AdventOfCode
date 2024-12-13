lines = readlines('input.txt');
token_accumulator = int32(0);
function [my_bool] = ntest(number)
    my_bool = true;
    my_bool = true & (number > 0);
    my_bool = true & (number < 100);
    my_bool = true & (abs(number - round(number))< 1e-5);
end

for line_index =1:length(lines)
    text_index = mod(line_index,4);
    if text_index == 1
        test_text = lines(line_index,1);
        my_match = regexp(test_text,"[0-9]+",'match');
    elseif text_index == 2
        test_text_2 = lines(line_index,1);
        my_match_2 = regexp(test_text_2,"[0-9]+",'match');
    elseif text_index == 3
        test_text_3 = lines(line_index,1);
        my_match_3 = regexp(test_text_3,"[0-9]+",'match');
    else
        A = [str2double(my_match(1)), str2double(my_match(2));str2double(my_match_2(1)), str2double(my_match_2(2))];
        G = [str2double(my_match_3(1)), str2double(my_match_3(2))];
        N = G/A;

        if ntest(N(1,1)) && ntest(N(1,2))
            N
            token_accumulator = token_accumulator + 3*N(1,1) + N(1,2);
        end
    end
end
token_accumulator
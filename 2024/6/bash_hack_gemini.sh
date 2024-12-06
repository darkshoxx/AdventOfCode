my_string='Hello, World!'
declare -a lines=()
# echo ${my_string:2:4}
while read p; do
    lines+=("$p")
    # echo $p
done < C:\\Code\\GithubRepos\\AdventOfCode\\2024\\6\\input.txt
line_1_string=${lines[1]}
width=${#line_1_string}
height=${#lines}
# echo "$height"
caretstring="^"
rows=($(seq 0 1 $height))
for row in "${rows[@]}"
do
    line=${lines[row]}
    cols=($(seq 0 1 $width))
    for col in "${cols[@]}"
    do
    teststring="${line:col:1}"
    if [[ "$caretstring" == "$teststring" ]];then
        echo ${line:col:1}
        start_x=$row
        start_y=$col
    fi
    # echo ${line:col:1}
    done
done
# echo "$start_x"
# echo "$start_y"

pos_x=$start_x
pos_y=$start_y

declare -A new_directions=( ["N"]="E" ["E"]="S" ["S"]="W" ["W"]="N")
# echo "${new_directions[N]}"
north_x=-1
east_x=0
south_x=1
west_x=0
declare -A directions_x=( ["N"]=$north_x ["E"]=$east_x ["S"]=$south_x ["W"]=$west_x)
north_y=0
east_y=1
south_y=0
west_y=-1
declare -A directions_y=( ["N"]=$north_y ["E"]=$east_y ["S"]=$south_y ["W"]=$west_y)
# echo "${directions_x[N]}"
# echo "${directions_y[N]}"

direction="N"

dir_x=${directions_x[$direction]}
dir_y=${directions_y[$direction]}
# echo "X:"
# echo $dir_x
# echo "Y:"
# echo $dir_y


declare -a unique_positions=()
declare -a current_positions=()
current_positions+=($pos_x)
current_positions+=($pos_y)
new_pos="${current_positions[*]},"
new_pos="${new_pos%,}"
# echo $new_pos
unique_positions+=("$new_pos")
# echo Uni
# echo $unique_positions
# test_string="-1 0"
# for item in "${unique_positions[@]}"
# do
#     if [[ "$item" == "$test_string" ]]
#     then
#        [:]
#     fi
# done

on_the_field=1
pound_symbol="#"
while [ $on_the_field -eq 1 ]
do
    echo $on_the_field
    new_pos_x=$((pos_x + dir_x))
    new_pos_y=$((pos_y + dir_y))
    echo "X: $new_pos_x Y: $new_pos_y"
    if (($new_pos_x < 0)) || (($new_pos_x > $width)) ||  (($new_pos_y < 0)) || (($new_pos_y > $height))
    then
        on_the_field=0
    else
        line=${lines[$new_pos_x]}
        new_symbol=${line:$new_pos_y:1}
        if [[ "$new_symbol" == "$pound_symbol" ]]
        then
            echo "THEN"
            direction=${new_directions[$direction]}
            dir_x=${directions_x[$direction]}
            dir_y=${directions_y[$direction]}
        else
            echo "ELSE"
            pos_x=$new_pos_x
            pos_y=$new_pos_y
            declare -a current_positions=("R" "$new_pos_x" "$new_pos_y")
            test_string="${current_positions[*]}"
            if [[ ! " ${unique_positions[*]} " =~ " $test_string " ]]; then
                unique_positions+=("$test_string")
            fi
        fi
    fi

done
echo "RESULT:"
echo ${#unique_positions[@]}

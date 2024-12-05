$text = Get-Content C:\Code\GithubRepos\AdventOfCode\2024\5\input_small.txt -Raw
# $text = "a b"
$textArray = $text -Split "`r`n`r`n"
$orderings = $textArray[0]
$updates = $textArray[1]


$string1 = "S1"
$string2 = "S2"

$lookup_dict = @{}
$orderings_array = $orderings -Split "`r`n"
foreach ($pair in $orderings_array){
    $pair_array = $pair.Split("|")
    $key = $pair_array[0]
    $value = $pair_array[1]
    if ($lookup_dict.$key -ne $null){
        $temp_list = $lookup_dict[$key]
        # Write-Output "Here"
        # Write-Output "Value: $value"
        # Write-Output "TempList before: $temp_list"
        $temp_list = $temp_list + @($value)
        # Write-Output "TempList after: $temp_list"
        # Write-Output "Here END"
        $lookup_dict[$key] = $temp_list        
    } else {
        
        
        $lookup_dict.Add($key, @($value))
    }
    
}

function comparison{
    param(
        $start,
        $end
    )

    if ($lookup_dict.$end -ne $null){
        $end_list = $lookup_dict[$end]
        if($end_list -contains $start){
            Write-Output "Returning False"
            return $false
        }
        Write-Output "Returning True"
        return $true
    }
}
$result = comparison  "75" "29"
Write-Output $result
$accumulator = 0

$update_lines = $updates -Split "`n"
# Write-Output $update_lines[0]
foreach ($line in $update_lines){
    Write-Output $line.Substring(0,4)
    if ($line.Substring(0,5) -eq "75,47"){
        $line_entries = $line -Split ","
        $currently_valid = $true
        $line_length = $line_entries.length
        if($line_length -ne 1){
            $central_index = ($line_length-1)/2
            $range_1 = 0..($line_length-2)
            # Write-Output $line_entries[$central_index]
            foreach ($first in $range_1){
                
                $range_2 = ($first+1)..($line_length-1)
                Write-Output "range_2: $range_2"
                foreach ($second in $range_2){
                    $my_start = $line_entries[$first]
                    $my_end = $line_entries[$second]
                    Write-Output "Start: $my_start"
                    Write-Output "End: $my_end"
                    $my_start_length = $my_start.length
                    if($my_start_length -eq 3){
                        $my_start = $my_start[0] + $my_start[1]
                    }
                    $my_end_length = $my_end.length
                    if($my_end_length -eq 3){
                        $my_end = $my_end[0] + $my_end[1]
                    }
                    Write-Output "EndLength: $my_end_length"


                    $compared_value = comparison $my_start $my_end
                    $currently_valid = $currently_valid -and $compared_value
                    Write-Output "Comp: $compared_value"
                }
                
            }
        }
        
        Write-Output "EOL VALID: $currently_valid"
        if($currently_valid){
            $new_term = [int]$line_entries[$central_index]
            Write-Output "NEW TERM: $new_term"

            $accumulator = $accumulator + $new_term
            Write-Output "MidAcc: $accumulator"
        }
    }
}
Write-Output "Acc: $accumulator"
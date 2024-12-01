// to compile:
// gcc c_hack.c -o c_hack
// to run: ./c_hack.exe
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main() {

    // writing print statement to print hello world
    FILE* fptr;
    fptr = fopen("C:/code/AdventOfCode/2024/1/input.txt", "r"); 
    if (fptr == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
    // option: load file into buffer line by line
    char buffer[14];
    int left_array[100];
    int right_array[100];
    int index = 0;


    while(fgets(buffer, 14, fptr) != NULL){
        buffer[strcspn(buffer, "\n")] = '\0';
        int left = atoi(buffer);
        int right = atoi(buffer + 8);
        printf("Left: %d, Right: %d\n", left, right);
        if (left != 0){
            left_array[index] = left;
            right_array[index] = right;
            index = index + 1;
        }
    }
    int min = 0
    int min_index = 0
    for(int search_index = 0; search_index < 100; search_index++){
        if(left_array[print_index]> min){
            min = left_array[print_index]
            min_index = print_index
        }
    }
    for (int print_index=0; print_index<100; print_index++){
        printf("Leftarray entry %d is %d\n", print_index, left_array[print_index]);

    }
    // option: load entire file into buffer

    // char* buffer = NULL;
    // size_t len;
    // ssize_t bytes_read = getdelim(&buffer, &len, '\0', fptr);
    // if (bytes_read != -1){
    //     printf(buffer);
    // }
    return 0;
}
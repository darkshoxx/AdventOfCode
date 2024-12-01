// to compile:
// gcc c_hack.c -o c_hack
// to run: ./c_hack.exe
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int smallest_difference(int left_array[1000], int right_array[1000] ){
    int min_left = 100000;
    int min_index_left = 0;
    int min_right = 100000;
    int min_index_right = 0;
    for(int search_index = 0; search_index < 1000; search_index++){
        if(left_array[search_index]< min_left){
            min_left = left_array[search_index];
            min_index_left = search_index;
        }
        if(right_array[search_index]< min_right){
            min_right = right_array[search_index];
            min_index_right = search_index;
        }
    }
    left_array[min_index_left] = 100000;
    right_array[min_index_right] = 100000;
        if (min_left > min_right){
        return min_left - min_right;
    } else {
        return min_right - min_left;
    }
}

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
    int left_array[1000];
    int right_array[1000];
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
    int accumulator = 0;
    for(int i=0; i<1000; i++){
    accumulator += smallest_difference(left_array, right_array);
    }

    for (int print_index=0; print_index<1000; print_index++){
        printf("Leftarray entry %d is %d\n", print_index, left_array[print_index]);

    }

    //printf("Left min is %d, right min is %d\n", min_left, min_right);
    printf("Solution is %d\n", accumulator);
    // option: load entire file into buffer

    // char* buffer = NULL;
    // size_t len;
    // ssize_t bytes_read = getdelim(&buffer, &len, '\0', fptr);
    // if (bytes_read != -1){
    //     printf(buffer);
    // }
    return 0;
}
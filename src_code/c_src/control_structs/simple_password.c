#include <stdio.h>

void main(int argc, char *argv[]) {
    
    if (strcmp("cybertron", argv[1]) == 0){
        puts("You win!");
    } else {
        puts("Try again :(");
    }
}

#include <stdio.h>

int main() {
    int v = 10;
    int w = 20;
    int x = 30;
    int y = 40;
    int z = 50;

    if (v < w) {
        printf("v is less than w\n");
    } else {
        printf("v is not less than w\n");
    }

    if (x > y) {
        printf("x is greater than y\n");
    } else {
        printf("x is not greater than y\n");
    }

    if (z == 50) {
        printf("z is equal to 50\n");
    } else {
        printf("z is not equal to 50\n");
    }

    return 0;
}

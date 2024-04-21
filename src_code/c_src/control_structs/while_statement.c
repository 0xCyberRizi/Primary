#include <stdio.h>

int main() {
    int a = 1;
    int b = 10;
    int c = 3;

    printf("Printing numbers from %d to %d with step %d:\n", a, b, c);

    while (a <= b) {
        printf("%d ", a);
        a += c; // Increment 'a' by 'c' in each iteration
    }

    printf("\n");

    return 0;
}

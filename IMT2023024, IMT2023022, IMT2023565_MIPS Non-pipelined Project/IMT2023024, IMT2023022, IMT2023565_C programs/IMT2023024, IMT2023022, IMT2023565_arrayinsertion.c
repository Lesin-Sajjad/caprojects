#include <stdio.h>
#include <stdlib.h>

int main() {
    int source[] = {1, 2, 3, 4, 5};
    int size = 5;
    int target[5][4]; // 5x4 target array

    // Copy elements from source to target
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < 4; j++) {
            target[i][j] = source[i];
        }
    }

    // Output the target array
    printf("Target array:\n");
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < 4; j++) {
            printf("%d ", target[i][j]);
        }
        printf("\n");
    }

    return 0;
}
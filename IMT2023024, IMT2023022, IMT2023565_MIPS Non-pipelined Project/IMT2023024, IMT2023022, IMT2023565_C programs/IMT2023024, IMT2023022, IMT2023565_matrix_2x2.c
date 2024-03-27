#include <stdio.h>

int main() {
    int matrix_X[2][2] = {{1, 2}, {3, 4}};
    int matrix_Y[2][2] = {{5, 6}, {7, 8}};
    int result[2][2];

    // Perform matrix multiplication
    result[0][0] = matrix_X[0][0] * matrix_Y[0][0] + matrix_X[0][1] * matrix_Y[1][0];
    result[0][1] = matrix_X[0][0] * matrix_Y[0][1] + matrix_X[0][1] * matrix_Y[1][1];
    result[1][0] = matrix_X[1][0] * matrix_Y[0][0] + matrix_X[1][1] * matrix_Y[1][0];
    result[1][1] = matrix_X[1][0] * matrix_Y[0][1] + matrix_X[1][1] * matrix_Y[1][1];

    // Display the result
    printf("Result:\n");
    printf("%d %d\n", result[0][0], result[0][1]);
    printf("%d %d\n", result[1][0], result[1][1]);

    return 0;
}
#include <stdio.h>

int main() {
    int n = 8; // Number of Fibonacci numbers to generate
    int x = 0, y = 1, t4, counter = 0;

    // Output the first Fibonacci number (0)
    printf("%d ", x);

    // Output the second Fibonacci number (1)
    printf("%d ", y);
    
    counter += 2; // Count the first two Fibonacci numbers

    // Calculate and output the remaining Fibonacci numbers
    while (counter < n) {
        t4 = x + y;
        x = y;
        y = t4;
        printf("%d ", y);
        counter++;
    }

    return 0;
}

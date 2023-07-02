#include <stdio.h>
#include "math_operations.h"

int main() {
    int a = 10, b = 5;
    
    int sum = add(a, b);
    printf("Sum: %d\n", sum);

    int difference = subtract(a, b);
    printf("Difference: %d\n", difference);

    int product = multiply(a, b);
    printf("Product: %d\n", product);

    int quotient = divide(a, b);
    printf("Quotient: %d\n", quotient);

    return 0;
}

// Swap 2 numbers by using call by value and call by reference

#include <stdio.h>

void cv_swap (int a, int b) {
    int temp;
    printf ("Values before swap in call by value function: a = %d, b = %d\n", a, b);
    temp = a;
    a = b;
    b = temp;
    printf ("Values after swap in call by value function: a = %d, b = %d\n", a, b);
}

void cr_swap (int *a, int *b) {
    int temp;
    printf ("Values before swap in call by reference function: a = %d, b = %d\n", *a, *b);
    temp = *a;
    *a = *b;
    *b = temp;
    printf ("Values after swap in call by reference function: a = %d, b = %d\n", *a, *b);
}

void main () {
    int a = 10, b = 20;
     printf ("Values in main: a = %d, b = %d\n\n", a, b);
     cv_swap (a, b);
     printf ("Values after swap in main: a = %d, b = %d\n\n", a, b);
     cr_swap (&a, &b);
    printf ("Values after swap in main: a = %d, b = %d\n\n", a, b);
    
}
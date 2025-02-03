// C program to find Factorial by using recursion.

#include <stdio.h>

long factorial(int n) {
    if (n==0) return 1;
    else return n*factorial(n-1);
}

void main () {
    int num;
    long fact;
    
    printf ("Enter a number for its factorial: ");
    scanf ("%d", &num);
    
    fact = factorial (num);
    
    printf ("Factorial of %d is %d", num, fact);
}
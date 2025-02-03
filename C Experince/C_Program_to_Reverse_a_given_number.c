// Write a C program to display Reverse of a given number
#include <stdio.h>

int main() {
    int n, reverse = 0, remainder;
    
    printf ("Enter an integer number: ");
    scanf ("%d", &n);
    
    while (n != 0) {
        remainder = n % 10;
        reverse = reverse * 10 + remainder;
        n = n / 10;        
        
    }
        printf ("Reversed Number = %d", reverse);

    return 0;
}
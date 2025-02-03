// C Program to Convert Decimal Numbers to Binary Numbers

#include <stdio.h>

void main () {
    int decimal, bin = 0, i = 1, remainder;
    
    printf ("Enter a decimal nmber to convert it into binary number: ");
    scanf ("%d", &decimal);
    
    
    while (decimal != 0) {
        remainder = decimal % 2;
        decimal = decimal /2;
        bin = bin + remainder * i;
        i = i*10;
    }
    
    printf ("The binary number is %d", bin);
}
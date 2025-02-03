//Q: Write a C program to check whether given number is divisible by 5 and 7.

#include <stdio.h>

int main() {
 
 int num;
 
 printf ("Enter a number to check whether it is divisible by 5 and 7: ");
 scanf ("%d", &num);
 
 if ((num%5==0)&&(num%7==0)) {
     printf ("The number is divisible by 5 and 7");
     
 }
 
 else {
     
     printf ("The number is not divisble by 5 and 7");
 }
    return 0;
}
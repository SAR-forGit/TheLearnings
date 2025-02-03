//Q: Write a C program to check whether given number is divisible by 5 and 7 or either one of them.

#include <stdio.h>

int main() {
 
 int num;
 
 printf ("Enter a number to check whether it is divisible by 5 and 7: ");
 scanf ("%d", &num);
 
 if ((num%5==0)&&(num%7==0)) {
     printf ("The number is divisible by 5 and 7 \n");
     
 }
 else if (num%5==0) {
     printf ("Number is only divisible by 5 \n");
 }
 
 else if (num%7==0) {
     printf ("Number is only divisible by 7 \n");
 }
 
 else {
     
     printf ("The number is not divisble by 5 and 7");
 }
    return 0;
}
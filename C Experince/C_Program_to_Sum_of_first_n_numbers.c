//Q: Write a C program to display the sum of first N natural numbers.

#include <stdio.h>

int main() {
   
   int num, sum=0;
   
   printf ("enter a number: ");
   scanf ("%d", &num);
   
   for (int i=0; i<=num; i++) {
       sum =sum + i;
   }
   
   printf ("The sum of the first %d number is: %d", num, sum);
   
    return 0;
}
//Q: Write a C program to display the sum of first N natural numbers do-while loop.

#include <stdio.h>

int main() {
   
   int num, sum=0;
   
   printf ("enter a number: ");
   scanf ("%d", &num);
   
   int i=0;
   
   do {
       sum = sum + i;
       i++;
      
   } while (i<=num);
   
   printf ("The sum of the first %d number is: %d", num, sum);
   
    return 0;
}
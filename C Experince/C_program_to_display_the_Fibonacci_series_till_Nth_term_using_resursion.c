// Q: Write a C program to display the Fibonacci series till Nth term using resursion.

#include <stdio.h>

int fib (int n) {
   static int n1 = 0, n2 = 1, n3;
   
   if (n>0) {
       n3 = n1 + n2;
       n1 = n2;
       n2 = n3;
       printf ("%d\t", n3);
       fib (n-1);
   }
   
    }
 
void main () {
    int n;
    printf ("Enter the number of elements: ");
    scanf ("%d", &n);
    printf ("0\t1\t");
    fib (n-2);
}
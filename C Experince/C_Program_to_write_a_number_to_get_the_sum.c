#include <stdio.h>

int main() {
   
int j, sum=0;

printf ("write a number to get the sum: \n");
scanf ("%d", &j);


for (int i=1; i<=j; i++) {
    sum = sum + i;
}
    printf ("Your answer is %d", sum);
    
    return 0;
}
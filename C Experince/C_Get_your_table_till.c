#include <stdio.h>

int main() {
 
 int users_number;
 
 printf ("write a number for it's table: ");
 scanf ("%d", &users_number);
 
 int table_completion;
 printf ("table complete till?: ");
scanf ("%d", &table_completion);

 for (int i=0; i<=table_completion; i++) {
printf ("%d x ", users_number);
printf ("%d = ", i);
printf ("%d \n", i*users_number);

 }
 

    return 0;
}
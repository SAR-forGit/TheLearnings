// smallest among 2 numbers
#include <stdio.h>

void main () {
    int a, b;
    
    printf ("Enter values of a, b : ");
    scanf ("%d%d", &a, &b);
    
    if (a>b) {
        printf ("b is smallest");
    }
    
    else {
        printf ("a is smallest");
    }
}
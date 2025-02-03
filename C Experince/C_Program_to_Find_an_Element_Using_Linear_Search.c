// C Program to Find an Element Using Linear Search

#include <stdio.h>

void main () {
    int i, search, m, arr[1000];
    
    printf ("Enter size of array: ");
    scanf ("%d", &m);
    
    printf ("\nEnter %d numbers: ", m);
    
    for (i=0; i<m; i++) {
        scanf ("%d", &arr[i]);
    }
    
    printf ("\nEnter number to search: ");
    scanf ("%d", &search);
    
    for (i=0; i<m; i++) {
        if (arr[i] == search) {
        printf ("\nNumber %d is present at %d position", search, i+1);
        break;
        }
    }
    
    if (i == m )
        printf("%d is not present in array.\n", search);
    
}
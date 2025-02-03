//Bubble sort program in C

#include <stdio.h>

void bubble_sort (int arr[], int n) {
 int i, j;
 for (i=0; i<n-1; i++) {
     for (j=0; j<n-i-1; j++) {
         if (arr[j] > arr[j+1]) {
         int temp = arr[j];
         arr[j] = arr[j+1];
         arr[j+1] = temp;
         }
     }
 }
}

void main () {
    int i, m, n;
    
    int arr[] = { 5, 1, 4, 2, 8 };
    
    n = sizeof(arr) / sizeof(arr[0]);
    
    bubble_sort (arr, n);
    
    printf("Sorted array: ");
    
    for (int i = 0; i < n; i++) {  
    printf("%d ", arr[i]);  
  }
    
}














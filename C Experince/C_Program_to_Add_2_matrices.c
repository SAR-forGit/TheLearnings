// Q: Write a C program to add two matrices

#include <stdio.h>

int main() {
int rows, columns;
int matrix1[rows][columns], matrix2[rows][columns], result[rows][columns];

//number for matrix's row and columns
printf ("Enter the number for rows and columns for the matrices: ");
scanf ("%d%d", &rows, &columns);

//matrix 1
printf ("Enter elements for first matrix: \n");

for (int i=0; i<rows; i++) {
    for (int j=0; j<columns; j++) {
     
     scanf ("%d", &matrix1[i][j]);   

    }
}

//matrix2
printf ("Enter elements for second matrix: \n");

for (int i=0; i<rows; i++) {
    for (int j=0; j<columns;j++) {
    
    scanf ("%d", &matrix2[i][j]);
    }
}

//result

for (int i=0; i<rows; i++) {
    for (int j=0; j<columns; j++) {
        result[i][j] = matrix1[i][j] + matrix2[i][j];
    }
}

//printing the result

printf ("The sum of the two matrices is: \n");

for (int i=0; i<rows; i++) {
    for (int j=0; j<columns; j++) {
        printf ("%d \t", result[i][j]);
    }
    
    printf ("\n");
}
    return 0;
}
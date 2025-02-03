// Demonstrate student structure

#include <stdio.h>

struct student {
    char name[50];
    int roll_number;
    char section;
}s;

void main () {
    printf ("Enter student's info: \n\n");
    
    printf ("Enter student's name: ");
    scanf ("%s", &s.name);
    
    printf ("\nEnter student's roll number: ");
    scanf ("%d", &s.roll_number);
    
    printf ("\nEnter student's section: ");
    scanf ("%s", &s.section);
    
    printf ("\n\nName: %s\nRoll Number: %d\nSection: %c\n", s.name, s.roll_number, s.section);
    
}

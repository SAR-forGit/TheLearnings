// C Program to Make a Simple Calculator Using switch...case

#include <stdio.h>

void main () {
    
    char op;
    int a, b;
    
    printf ("Enter an operand +, -, *, /, %: ");
    scanf ("%c", &op);
    
    printf ("Enter two number to %c : ", op);
    scanf ("%d%d", &a, &b);
    
    switch (op) {
        case '+':
        printf ("%d + %d = %d", a, b, a+b);
        break;
        
        case '-':
        printf ("%d - %d = %d", a, b, a-b);
        break;
        
        case '*':
        printf ("%d x %d = %d", a, b, a*b);
        break;
        
        case '/':
        printf ("%d / %d = %d", a, b, a/b);
        break;
        
        case '%':
        printf ("%d % %d = %d", a, b, a%b);
        break;
        
        default:
        printf ("Error! nothing to match");
    }
    
}
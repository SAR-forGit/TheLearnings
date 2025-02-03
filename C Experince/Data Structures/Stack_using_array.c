//Stack using array
#include<stdio.h>
#include <stdlib.h>

#define MAX_SIZE 100

int top;
int s[MAX_SIZE];
int item;
int stack_size;

void push(){
    if (top == stack_size-1){
        printf ("Stack overflow");
    }
    
    top++;
    s[top] = item;
}

int pop(){

    if (top == -1){
        printf ("stack underflow\n");
    }
    
    int item_deleted = s[top--];
    return item_deleted;
}

void display() {
      if (top == -1){
        printf ("stack underflow");
    }
    
    printf ("Contents of the stack: \n");
    for (int i = 0; i <= top; i++) {
        printf ("%d\n", s[i]);
    }
    
}

void main(){
    int choice;
    
    printf("Enter the size of the stack (up to %d): ", MAX_SIZE);
    scanf("%d", &stack_size);
    
    if (stack_size > MAX_SIZE || stack_size <= 0){
        printf ("Invalid stack size. Please enter a size between 1 and %d\n", MAX_SIZE);
        exit(1);
    }
    
    top = -1;
    
    for (;;){
        printf("1: Push 2: Pop\n");
        printf("3: Display 4: Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);
    
    
        switch (choice){
            case 1:
            printf ("Enter the item to be inserted: ");
            scanf ("%d", &item);
            push();
            break;
            
            case 2:
            item = pop();
            if (item != 0){
            printf ("Item deleted = %d\n", item);
            }
            break;
            
            case 3:
            display();
            break;
            
            case 4:
            exit(0);
            break;
            
            default:
            printf ("Invalid choice, try again. \n");
            break;
        }
    
    }
    
}



// Creating a single linked list
#include <stdio.h>
#include <stdlib.h>

struct node{
    int data;
    struct node *link;
};

int main(){
    struct node *head = malloc (sizeof(struct node));
    head -> data = 70;
    head -> link = NULL;
    
    struct node *current = malloc(sizeof(struct node));
    current -> data = 100;
    current -> link = NULL;
    head -> link = current;
    
    current = malloc(sizeof(struct node));
    current -> data = 121;
    current -> link = NULL;
    head -> link -> link = current;
    
    printf ("%d", current -> data);
    
    return 0;
}
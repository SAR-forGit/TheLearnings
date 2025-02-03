// Traversing a Single Linked List (Counting the Nodes)
#include <stdio.h>
#include <stdlib.h>

struct node{
    int data;
    struct node *link;
};


void count_of_nodes(struct node *head){
    int count = 0;
    if (head == NULL)
        printf ("Linked List is empty");
    
    struct node *ptr = NULL;
    ptr = head;
    
    while (ptr != NULL){
        count ++;
        ptr = ptr -> link;
    }
    printf ("And the number of nodes are: %d", count);
    
}

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
    
    count_of_nodes(head);
    
    return 0;
}




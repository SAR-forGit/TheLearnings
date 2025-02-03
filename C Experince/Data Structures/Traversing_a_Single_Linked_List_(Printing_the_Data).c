// Traversing a Single Linked List (Printing the Data)
#include <stdio.h>
#include <stdlib.h>

struct node{
    int data;
    struct node *link;
};


void count_of_nodes(struct node *head){
    
    if (head == NULL)
        printf ("Linked List is empty");
    
    struct node *ptr;           //or can write ( struct node *ptr = NULL; )
    ptr = head;
    
    while (ptr != NULL){
        printf ("%d\t", ptr -> data);
        ptr = ptr -> link;
    }

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




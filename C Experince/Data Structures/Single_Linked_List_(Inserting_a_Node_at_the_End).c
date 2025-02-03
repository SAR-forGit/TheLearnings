// Single Linked List (Inserting a Node at the End)

#include <stdio.h>
#include <stdlib.h>

//////////////////////////////Node////////////////////////////
struct node{
    int data;
    struct node *link;
};

////////////////// To insert a node at end ////////////////////
void add_at_end(struct node *head, int data){
    struct node *ptr, *temp;
    ptr = head;
    
    temp = (struct node *) malloc(sizeof(struct node));
    temp -> data = data;
    temp -> link = NULL;
    
    while (ptr->link != NULL){
        ptr = ptr -> link;
    }
    ptr -> link = temp;
}

/////////////////// To traverse a node ///////////////////////
void count_of_nodes(struct node *head){
    
    if (head == NULL)
        printf ("Linked List is empty");
    
    struct node *ptr = NULL;
    ptr = head;
    
    while (ptr != NULL){
        printf ("%d ", ptr -> data);
        ptr = ptr -> link;
    }

}

/////////////////////// Main Function //////////////////////////
void main(){
    struct node *head = malloc(sizeof(struct node)); //1st node
    head -> data = 70;
    head -> link = NULL;
    
    struct node *current = malloc(sizeof(struct node)); //2nd node
    current -> data = 800;
    current -> link = NULL;
    head -> link = current;
    
    current = malloc(sizeof(struct node)); //3rd node
    current -> data = 9000;
    current -> link = NULL;
    head -> link -> link = current;
    
    current = malloc(sizeof(struct node)); //4th node
    current -> data = 6969;
    current -> link = NULL;
    head -> link -> link -> link = current;
    
    add_at_end(head, 67); // To insert a node at end function
    count_of_nodes(head); // To count nodes and printing
}




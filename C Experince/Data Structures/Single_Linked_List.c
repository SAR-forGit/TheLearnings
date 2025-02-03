//Single Linked List

#include <stdio.h>
#include <stdlib.h>

////////////////// To create a single linked list ///////////////////////
struct node{
    int data;
    struct node *link;
};

/////////////// Function to allocate a new node /////////////////
struct node *getnode(){
    struct node *head = malloc(sizeof(struct node));
    
    if (head == NULL){
        printf("Out of memory");
        exit(0);
    }
    return head;
};

////// Function to insert a node at the front of the list //////
struct node *insert_front (int item, struct node *first){
    struct node *temp = getnode();
    temp -> data = item;
    temp -> link = first;
    
    return temp;
};

/////// Function to insert a node at the end of the list ///////
struct node *insert_end (int item, struct node *end){
    
    struct node *temp = getnode(), *current;
    temp -> data = item;
    temp -> link = NULL;
    
    if (end == NULL){
        return temp;
    }
   
   current = end;
   
   while (current->link != NULL){
       current = current -> link;
   }
   
   current -> link = temp;
   return end;
};

/////////////////////// to delete the front node //////////////////////////
struct node *delete_front (struct node *first){
    struct node *temp;
    temp = first;
    temp = temp -> link;
    
    if (first == NULL){
        printf ("List is empty, cannot delete\n");
    }
    
    printf ("Item deleted = %d,\n", first -> data);
    free(first);
    return temp;
};

/////////////////////// to delete the last node ///////////////////////////
struct node *delete_end (struct node *end){
    struct node *current, *prev = NULL;
    
    if (end == NULL){
        printf ("List is empty, cannot delete\n");
    }
    
    if (end -> link == NULL){
        printf ("Item deleted = %d\n", end -> data);
        free(end);
    }
    
    current = end;
    
    while (current->link != NULL){
        prev = current;
        current = current -> link;
    }
    
    printf ("Item deleted = %d\n", current -> data);
    free (current);
    prev -> link = NULL;
    
    return end;
}

///////////////////// To display Contents of Node /////////////////////////
void display (struct node *first){
    struct node *current;
    
    if (first == NULL){
        printf ("The Linked list is empty\n");
    }
    
    printf ("The contents of the linked list are: ");
    current = first;
    
    while (current != NULL){
        printf ("%d ", current -> data);
        current = current -> link;
    }
    printf ("\n");
}


//////////////////////////// Main Function ////////////////////////////////
void main(){
    struct node *first = NULL, *head;
    int choice, item;
    
    while (1){
        printf("\n1: Insert Front\n");
        printf("2: Insert End\n");
        printf("3: Delete Front\n");
        printf("4: Delete End\n");
        printf("5: Display\n");
        printf("6: Exit\n");
    
        printf ("Enter your choice: ");
        scanf ("%d", &choice);
        
        switch (choice) {
            case 1:
            printf ("Enter the item to be inserted at the front: ");
            scanf ("%d", &item);
            first = insert_front (item, first);
            break;
            
            case 2:
            printf ("Enter the item to bo inserted at the end: ");
            scanf ("%d", &item);
            first = insert_end (item, first);
            break;
            
            case 3:
            first = delete_front (first);
            break;
            
            case 4:
            first = delete_end (first);
            break;
            
            case 5:
            display(first);
            break;
            
            case 6:
            exit(0);
            
            default:
            printf ("Invalid choice\n");
        }

    }
    
}





#include <bits/stdc++.h>
using namespace std;

struct Node {
    int data;
    Node* next;
};

// Function to delete a node from the linked list
void del(Node*& start, Node*& avail, Node* loc, Node* locp) {
    // Step 1: If LOCP is NULL, delete the first node
    if (locp == NULL) {
        start = loc->next;  // Update START to point to the second node
    } else {
        locp->next = loc->next;  // Link the previous node to the next of the node to be deleted
    }

    // Step 2: Return the deleted node to the AVAIL list
    loc->next = avail;  // Set the next of the deleted node to the current AVAIL
    avail = loc;        // Update AVAIL to point to the deleted node
}

// Function to traverse and print the linked list
void linkedListTraversal(Node* ptr) {
    while (ptr != NULL) {
        cout << ptr->data << " ";
        ptr = ptr->next;
    }
    cout << endl;
}

int main() {
    // Create a linked list
    Node* head = new Node{7, nullptr};
    Node* second = new Node{11, nullptr};
    Node* third = new Node{41, nullptr};
    Node* fourth = new Node{66, nullptr};
                                                                                                                                                                                                                                                                                                                                                                                                
    // Link nodes
    head->next = second;
    second->next = third;
    third->next = fourth;

    // Initialize available nodes list (AVAIL)
    Node* avail = nullptr;

    // Print the original linked list
    cout << "Original linked list: ";
    linkedListTraversal(head);

    // Assume we want to delete the second node (11)
    Node* loc = second;   // Node to delete
    Node* locp = head;    // Previous node (7)

    // Delete the node
    del(head, avail, loc, locp);

    // Print the linked list after deletion
    cout << "Linked list after deletion: ";
    linkedListTraversal(head);

    // Print the available nodes
    cout << "Available nodes after deletion: ";
    linkedListTraversal(avail);

    return 0;
}

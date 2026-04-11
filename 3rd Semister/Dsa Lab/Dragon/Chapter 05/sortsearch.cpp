#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
};

// Function to search for an item in a sorted linked list
Node* searchSorted(Node* start, int item) {
    Node* ptr = start;

    // Traverse the linked list
    while (ptr != NULL) {
        if (item < ptr->data) {
            // Since the list is sorted, if ITEM < ptr->data, ITEM is not in the list
            return NULL;
        } else if (item == ptr->data) {
            // Item found, return the node's address
            return ptr;
        }
        ptr = ptr->next;  // Move to the next node
    }

    // If the item is not found
    return NULL;
}

// Function to print the linked list
void linkedListTraversal(Node* ptr) {
    while (ptr != NULL) {
        cout << ptr->data << " ";
        ptr = ptr->next;
    }
    cout << endl;
}

int main() {
    // Create a sorted linked list
    Node* head = new Node{7, nullptr};
    Node* second = new Node{11, nullptr};
    Node* third = new Node{41, nullptr};
    Node* fourth = new Node{66, nullptr};

    // Link nodes
    head->next = second;
    second->next = third;
    third->next = fourth;

    // Print the linked list
    cout << "Sorted linked list: ";
    linkedListTraversal(head);

    // Search for an item in the sorted linked list
    int item = 41;
    Node* loc = searchSorted(head, item);

    // Display the result
    if (loc != NULL) {
        cout << "Item " << item << " found at node with address: " << loc << endl;
    } else {
        cout << "Item " << item << " not found in the list." << endl;
    }

    return 0;
}

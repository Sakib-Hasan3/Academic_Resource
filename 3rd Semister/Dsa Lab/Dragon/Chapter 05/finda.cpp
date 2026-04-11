#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
};

// Function to find the last node with INFO[LOC] < ITEM in a sorted linked list
Node* findA(Node* start, int item) {
    // Step 1: Check if the list is empty
    if (start == NULL) {
        return NULL; // Set LOC = NULL
    }

    // Step 2: Special case for the first node
    if (item < start->data) {
        return NULL; // Set LOC = NULL
    }

    // Step 3: Initialize pointers
    Node* save = start;
    Node* ptr = start->next;

    // Step 4: Traverse the list
    while (ptr != NULL) {
        // Step 5: Check if the current node's data is greater than or equal to ITEM
        if (item < ptr->data) {
            return save; // Set LOC = SAVE and return
        }
        
        // Step 6: Update pointers
        save = ptr;
        ptr = ptr->next;
    }

    // Step 7: Set LOC to the last valid save
    return save; // Return the last node where INFO[LOC] < ITEM
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
    // Create a sorted linked list
    Node* head = new Node{7, nullptr};
    Node* second = new Node{11, nullptr};
    Node* third = new Node{41, nullptr};
    Node* fourth = new Node{66, nullptr};

    // Link nodes
    head->next = second;
    second->next = third;
    third->next = fourth;

    // Print the sorted linked list
    cout << "Sorted linked list: ";
    linkedListTraversal(head);

    // Search for an item in the sorted linked list
    int item = 40;
    Node* loc = findA(head, item);

    // Display the result
    if (loc != NULL) {
        cout << "The last node where INFO[LOC] < " << item << " is: " << loc->data << endl;
    } else {
        cout << "No node found where INFO[LOC] < " << item << "." << endl;
    }

    return 0;
}

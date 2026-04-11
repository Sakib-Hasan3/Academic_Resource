#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
};

// Function to insert a new item as the first node in the list
void insertFirst(Node*& start, Node*& avail, int item) {
    // Step 1: Check for overflow (no available nodes)
    if (avail == NULL) {
        cout << "OVERFLOW: No available nodes to insert." << endl;
        return;
    }

    // Step 2: Remove first node from AVAIL list
    Node* newNode = avail;
    avail = avail->next;  // Update AVAIL to point to the next available node

    // Step 3: Copy item into new node
    newNode->data = item;

    // Step 4: Set new node's link to the current START
    newNode->next = start;

    // Step 5: Update START to point to the new node
    start = newNode;
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
    // Initialize an available nodes list (AVAIL) with some nodes
    Node* avail = new Node{0, nullptr};
    avail->next = new Node{0, nullptr};
    avail->next->next = new Node{0, nullptr};

    // Initialize an empty linked list (START)
    Node* start = NULL;

    // Insert items at the beginning of the list
    insertFirst(start, avail, 10);
    insertFirst(start, avail, 20);
    insertFirst(start, avail, 30);

    // Display the linked list after insertions
    cout << "Linked list after insertions: ";
    linkedListTraversal(start);

    // Display remaining nodes in AVAIL
    cout << "Remaining nodes in AVAIL: ";
    linkedListTraversal(avail);

    return 0;
}

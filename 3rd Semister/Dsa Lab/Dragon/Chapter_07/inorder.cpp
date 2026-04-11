// C++ program for inorder traversals
#include<bits/stdc++.h>
using namespace std;

struct Node
{
    int data;
    struct Node *left,*right;
    Node(int v)
    {
        data = v;
        left = right =nullptr;
    }
};

void printInorder(struct Node* node){
    if(node==nullptr)
    return;

    printInorder(node->left);
    cout<<node->data<<" ";
    printInorder(node->right);
}

int main(){
    struct Node* root = new Node(1);
    root->left= new Node(2);
    root->right= new Node(3);
    root->left-> left = new Node(4);
    root->left->right = new Node(5);
    root->right->right = new Node(6);

    // Function call
    cout << "Inorder traversal of binary tree is: \n";

    printInorder(root);

    return 0;
}

#include<bits/stdc++.h>
using namespace std;
struct Node{
    int data;
    struct Node *left,*right;
    Node(int val){
        data=val;
        left=right=nullptr;
    }
};

void printPre(struct Node* root){
    if (root==nullptr)
    {
        return;
    }
    printPre(root->left);
    cout<<root->data<<endl;
    printPre(root->right);
    
}
int main(){
    struct Node* root = new Node(10);
    root->left=new Node(20);
    root->right=new Node(30);
    root->left->left=new Node(40);
    root->left->right=new Node(50);
    root->right->right=new Node(60);

    printPre(root);
}
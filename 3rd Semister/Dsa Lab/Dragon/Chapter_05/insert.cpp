#include<bits/stdc++.h>
using namespace std;
class Node{
    public:
    int val;
    Node* next;
    Node(int val){//constractor 
        this->val=val;
        this->next=NULL;
    }
};

void printTra(Node* head){
    Node* temp=head;
    while (temp!=NULL)
    {
        cout<<temp->val<<" ";
        temp=temp->next;
    }
    cout<<endl;
    
}

void insert(Node* head,int p,int vall){
    Node* newN= new Node(vall);
    Node* temp=head;
    for (int i = 0; i < p-1; i++)
    {
        temp=temp->next;
    }
    newN->next=temp->next;
    temp->next=newN;

    
    
}
int main()
{
    Node* head = new Node(10);
    Node* a = new Node(20);
    Node* b = new Node(30);
    Node* c = new Node(40);
    Node* d = new Node(50);


    head->next=a;
    a->next=b;
    b->next=c;
    c->next=d;

    cout << "Given list: " << endl;
    printTra(head);

    int p;
    cin>>p;

    int vall;
    cin>>vall;

    insert(head,p,vall);

    cout << "After insert list: " << endl;
    printTra(head);
}
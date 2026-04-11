#include <bits/stdc++.h>
using namespace std;
class Node
{
public:
    int val;
    Node *next;
    Node(int val)
    {
        this->val = val;
        this->next = NULL;
    }
};
void printTra(Node *head)
{
    Node *temp = head;
    while (temp != NULL)
    {
        cout << temp->val << " ";
        temp = temp->next;
    }
    cout<<endl;
}

void DeleteN(Node*& head,int pos){
    if (head==NULL)
    {
        cout<<"Empty list"<<endl;
        return;
    }
    if (pos==1)
    {
        Node* toDelete = head;
        head=head->next;
        delete toDelete;
        return;
    }

    Node* temp=head;
    for (int i = 1; i < pos-1 && temp->next!=NULL; i++)
    {
        temp=temp->next;
    }

    if (temp->next==NULL)
    {
        cout<<"Position is out of bound"<<endl;
        return;
    }

    Node* toDelete = temp->next;
    temp->next = toDelete->next;
    delete toDelete;
    
    
    
}

int main()
{
    Node *head = new Node(10);
    Node *a = new Node(20);
    Node *b = new Node(30);
    Node *c = new Node(40);
    Node *d = new Node(50);

    head->next = a;
    a->next = b;
    b->next = c;
    c->next = d;
    cout << "Given list: " << endl;
    printTra(head);

    int pos;
    cout << "Given position: " << endl;
    cin >> pos;


    DeleteN(head, pos);

    cout << "New list: " << endl;
    printTra(head);
}
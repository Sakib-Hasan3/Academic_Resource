#include<bits/stdc++.h>
using namespace std;

int insertD(int arr[],int n,int pos,int item){
    for (int i = n-1; i >=pos ; i--)
    {
        arr[i+1]=arr[i];
    }

    arr[pos]=item;

    return n+1;
    
}


int main(){
    int n;
    cin>>n;
    int arr[n];
    for (int i = 0; i < n; i++)
    {
        cin>>arr[i];
    }

    int pos;
    cout<<"Enter position: "<<endl;
    cin>>pos;

    int item;
    cout<<"Enter item: "<<endl;
    cin>>item;

    n = insertD(arr,n,pos-1,item);
    

    for (int i = 0; i < n; i++)
    {
        cout<<arr[i]<<" ";
    }
    
}
#include<bits/stdc++.h>
using namespace std;

int del(int arr[],int n,int k){
    
    for (int i = k; i <=n-1; i++)
    {
        arr[i]=arr[i+1];
    }
    
    
    return n-1;
    
}



int main(){
    int n;
    cin>>n;

    int arr[n];
    for (int i = 0; i < n; i++)
    {
        cin>>arr[i];
    }

    
    int k;
    cout<<"Input the position: "<<endl;
    cin>>k;

    del(arr,n,k-1);
    for (int i = 0; i < n; i++)
    {
        cout<<arr[i]<<" ";
    }
    cout<<endl;
    
}
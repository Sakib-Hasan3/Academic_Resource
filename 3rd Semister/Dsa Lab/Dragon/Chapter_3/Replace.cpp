#include<bits/stdc++.h>
using namespace std;

int main(){
    string str = "To be or not 2B, that is the ? that is 2B decided for future!";
    string pattern = "2B";
    string placeholder = "to be";
    cout<<str<<endl;

    int index = str.find(pattern);
    while (index!= -1)
    {
        str.replace(index,pattern.length(),placeholder);
        index = str.find(pattern);
    }

    cout<<str<<endl;
    
}
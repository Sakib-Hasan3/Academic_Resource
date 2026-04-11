#include <bits/stdc++.h>
using namespace std;

int insert(int arr[], int n, int k, int item)
{

    for (int i = n - 1; i >= k; i--)
    {
        arr[i + 1] = arr[i];
    }

    arr[k] = item;
    return n + 1;
}

int main()
{
    int n;
    cin >> n;

    int arr[n];
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    int item;
    cout << "Input the item: " << endl;
    cin >> item;

    int k;
    cout << "Input the position: " << endl;
    cin >> k;

    n = insert(arr, n, k - 1, item);//notice

    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
}
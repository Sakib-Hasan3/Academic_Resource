#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int T;
    cin >> T; 

    while (T--) 
    {
       long long  int a, b, c;
        cin >> a >> b >> c;
        long long s = (a + b + c) / 2;
        
        long long area = s * (s - a) * (s - b) * (s - c);
        
    
        if (area <= 0) 
        {
            cout << "Error: invalid triangle dimensions\n";
            continue;
        }
        
        long long n = 4 * area;
        long long d =4*(s * s);

        int g = gcd(n, d);
        n /= g;
        d/= g;

        cout << n << "/" << d << endl;
    }

    return 0;
}

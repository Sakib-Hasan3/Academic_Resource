/*#include <iostream>
using namespace std;

int main() 
{
    int T;
    cin >> T;  

    for (int i = 1; i <= T; i++) 
    {
        int N, D;
        cin >> N >> D;  
        
        int k = 0; 

        for (int j = 0; j < N; j++) 
        {
            int X, Y;
            cin >> X >> Y;  
    
            int count = 0;  

            int next_possible = X + Y;

      
            while (next_possible <= D) 
            {
                count++;  
                next_possible += X;  
            }

       
            k += count;
        }

        cout << "Case " << i << ": " << k << endl;
    }

}*/
#include <iostream>
using namespace std;

int main() 

{
    long long int t;
    long long int n, k;
    long long int x,y,z=0;
    long long int sum=0;
    cin>>t;
    while(t>0)
    {

        cin>>n>>k;
        for(int i=0;i<n;i++)
        {
          
          cin>>x>>y;

          long long int a=(k/x);
          //cout<<a<<endl;
         sum = sum+a;
        }
        z++;

        cout<<"Case "<<z<<":"<<" "<<sum<<endl;
        sum = 0;

        t--;


    }
}
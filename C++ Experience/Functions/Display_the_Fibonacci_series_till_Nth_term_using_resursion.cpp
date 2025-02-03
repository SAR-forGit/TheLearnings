// Q: Display the Fibonacci series till Nth term using resursion.

#include <iostream>
using namespace std;

int fib (int n) {
   static int n1 = 0, n2 = 1, n3;
   
   if (n>0) {
       n3 = n1 + n2;
       n1 = n2;
       n2 = n3;
       cout << n3 << "\t";
       fib (n-1);
   }
   
   return 0;
}
 
int main () {
    int n;
    cout << "Enter the number of elements: ";
    cin >> n;
    cout << "0\t1\t";
    fib (n-2);
    
    return 0;
}
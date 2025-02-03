// Q: Program To Print Prime Numbers From 1 To n Using Function

#include <iostream>
using namespace std;

bool isPrime(int n)
{
  
      if (n==1 || n==0) 
      return false;
  
      for (int i=2; i<n; i++)
      {
        if(n%i==0) 
        return false;
      }
      return true;

}

int printPrime (int n) {

    for (int i=2; i<=n; i++) {
        if (isPrime(i)) {
            cout << i << " ";
        }
    }    
    return 0;
}

int main () {
    int givenNum;
    
    cout << "Enter a number to print numbers from 2 to: ";
    cin >> givenNum;
    cout << endl;
    
    cout << "Prime number till " << givenNum << " is ";
    cout << printPrime (givenNum);
    
    return 0;
}
// Q: Print Factorial of Number

#include <iostream> 
using namespace std;

int main() {
    
    int givenNum, Number=1;
    
    cout <<"Enter the number to print its Factorial: ";
    cin >> givenNum;
    cout << "\n";
    
    for (int n=1; n<=givenNum; n++) {
            Number *= n;
        }
    
    
cout << "Ans: The Factorial of " << givenNum << " is " << Number;
    
    return 0;
}
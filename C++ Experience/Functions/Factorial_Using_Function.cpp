// Q: Factorial Using Function

#include <iostream>
using namespace std;

int Factorial (int givenNum) {
    int num=1;
    for (int i=1; i<=givenNum; i++) {
        num *= i;
    }
    
    return num;
}

int main() {
    int theNumber;
    
    cout << "Write a number to know it's Factorial; ";
    cin >> theNumber;
    
    cout << endl;
    cout << "Your Factorial for a number " << theNumber << " is " << Factorial(theNumber);

    return 0;
}
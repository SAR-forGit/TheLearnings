// Q: Sum of Digits

#include <iostream>
using namespace std;

int SumOfDigits (int num) {
    
    int digSum =0;
    
    while (num > 0) {
        int lastDig = num % 10;
        
        num /= 10;
        digSum += lastDig;
    }
    return digSum;
}

int main() {
    int givenNum;
    
    cout << "Enter a number to calculate sum of its all digits: ";
    cin >> givenNum;
    cout << endl << "Sum of " << givenNum << " is " << SumOfDigits(givenNum);
    
    return 0;
}
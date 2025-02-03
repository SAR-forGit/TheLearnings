// Q: Sum of all numbers from 1 to n which are divisible by 3

#include <iostream> 
using namespace std;

int main() {
    
    int givenNum, Number=0;
    
    cout <<"Enter the number to check wether it's divisible by 3 and add till it: ";
    cin >> givenNum;
    cout << "\n";
    
    for (int n=1; n<=givenNum; n++) {
        if (n%3 == 0) {
            Number += n;
        }
    }
    
cout << "Ans: The  Sum of all numbers from 1 to " << givenNum << " which are divisible by 3 is " << Number;
    
    return 0;
}
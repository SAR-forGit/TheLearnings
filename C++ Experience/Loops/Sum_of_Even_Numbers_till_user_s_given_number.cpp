// Q: Sum of Even-Numbers till user's given number

#include <iostream>
using namespace std;

int main () {
    int n, givenNum, evensum=0;
    
    cout << "Enter the number to check till is even or not: \n";
    cin >> givenNum;
    
    for (n=1; n<=givenNum; n++) {
        if (n%2==0) {
            evensum = evensum + n;
        }
    }

cout <<"Ans: The sum of even numbers from " << givenNum << " is " << evensum;

    return 0;
}
// Q: Reverse Triangle Pattern

#include <iostream>
using namespace std;

int main() {
    
    int givenNum, n;
    
    cout << "Enter a number to print a reverse traingle pattern: ";
    cin >> givenNum;
    cout << endl;
    
    for (int i=0; i<=givenNum-1; i++) {
        for (int j=i+1; j>0; j--) {
            cout << j << " ";
        }
        cout << endl;
    }
    
    cout << endl << "Is the given pattern";
    
    return 0;
}
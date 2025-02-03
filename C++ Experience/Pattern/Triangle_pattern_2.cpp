// Q: Triangle Pattern

#include <iostream>
using namespace std;

int main() {
    int givenNum, num=1;

    cout << "Give a num to print pattern accordingly: ";
    cin >> givenNum;
    cout << "\n";
    
    for (int i=1; i<givenNum+1; i++) {
        for (int j=1; j<=i; j++) {
            cout << i << " ";
        }
        cout << endl;
    }
    
    cout << endl << "Your Triangle Pattern is printed!!!";
    
    return 0;
}
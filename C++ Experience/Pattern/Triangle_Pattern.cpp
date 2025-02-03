// Q: Triangle Pattern

#include <iostream>
using namespace std;

int main() {
    int givenNum, num=1;

    cout << "Give a num to print pattern accordingly: ";
    cin >> givenNum;
    cout << "\n";
    
    for (int i=0; i<givenNum; i++) {
        for (int j=0; j<i+1; j++) {
            cout << "* ";
        }
        cout << endl;
    }
    
    cout << endl << "Your Triangle Pattern is printed!!!";
    
    return 0;
}
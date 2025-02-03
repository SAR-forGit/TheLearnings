// Q: Square Pattern

#include <iostream>
using namespace std;

int main() {
    int givenNum, num=1;

    cout << "Give a num to print pattern accordingly: ";
    cin >> givenNum;
    cout << "\n";
    
    for (int i=0; i<givenNum; i++) {
        for (int j=0; j<givenNum; j++) {
            cout << num << " ";
            num++;
        }
        cout << endl;
    }
    
    cout << endl << "Next number will be: " << num;
    
    return 0;
}
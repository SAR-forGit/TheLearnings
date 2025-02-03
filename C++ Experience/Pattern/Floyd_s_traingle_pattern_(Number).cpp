// Q: Floyd's traingle pattern (Number)

#include <iostream>
using namespace std;

int main() {
    
    int givenNum, num=1;
    
    cout << "Enter a number to print a Floyd's traingle pattern: ";
    cin >> givenNum;
    cout << endl;
    
    for (int i=0; i<=givenNum; i++) {
        for (int j=i+1; j>0; j--) {
            cout << num << " ";
            num++;
        }
        cout << endl;
    }
    
    cout << endl << "Is the given pattern";
    
    return 0;
}
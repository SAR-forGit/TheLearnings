// Q: Floyd's traingle pattern (Alphabets)

#include <iostream>
using namespace std;

int main() {
    
    int givenNum;
    char num= 65;
    
    cout << "Enter a number to print a Floyd's traingle pattern: ";
    cin >> givenNum;
    
    for (int i=0; i<=givenNum; i++) {
        for (int j=0; j<i; j++) {
            cout << num << " ";
            num++;
        }
        cout << endl;
    }
    
    cout << endl << "Is the given pattern";
    
    return 0;
}
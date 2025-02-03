// Q: Inverted traingle pattern 

#include <iostream>
using namespace std;

int main() {
    
    int givenNum;
    char num= 65;
    
    cout << "Enter a number to print a inverted traingle pattern: ";
    cin >> givenNum;
    cout << endl;
    
    for (int i=0; i<=givenNum; i++) {
        for (int j=0; j<i; j++) {
            cout << " ";
        }
        
        for (int j=0; j<givenNum-i; j++) {
            cout << (i+1);
        }
        
        cout << endl;
    }
    
    cout << endl << "Is the given pattern";
    
    return 0;
}
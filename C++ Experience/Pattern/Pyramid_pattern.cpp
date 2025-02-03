// Q: Pyramid pattern

#include <iostream>
using namespace std;

int main() {
    int givenNum, num;
    
    cout << "Enter the number to print and pyramid pattern: ";
    cin >> givenNum;
    cout << endl;
    
    for (int i=0; i<givenNum; i++) {
      
        // To print spaces
        for (int j=0; j<givenNum-i-1; j++) {
            cout << " ";
        }
        
        // To print first set of numbers
        for (int j=1; j<=i+1; j++) {
            cout << j;
        }
        
        // To print second set of numbers
        for (int j=i; j>0; j--) {
            cout << (j);
        }
        
        cout << endl;
    }
    
    cout << endl << "Is the given pattern";
    
    return 0;
}
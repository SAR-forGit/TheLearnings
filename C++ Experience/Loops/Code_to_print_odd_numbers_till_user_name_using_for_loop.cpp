// Q: Code to print odd-numbers till user name using for loop

#include <iostream> 
using namespace std;

int main () {
    int  number, input;
    cout << "Enter a number to count till: " << "\n";
    cin >> input;
    
    for (number=1; number<=input; number++) {
        if (number%2 != 0) {
            cout << number << " ";
        }
    }
    
    cout << endl;
    
    return 0;
}
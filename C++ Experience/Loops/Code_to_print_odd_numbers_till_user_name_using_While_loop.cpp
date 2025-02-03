// Q: Code to print odd-numbers till user name using While loop

#include <iostream> 
using namespace std;

int main () {
    int  number=1 , input;
    cout << "Enter a number to count till: " << "\n";
    cin >> input;

    while (number<=input) {
        if (number%2 !=0) {
            cout << number << " ";
        }
        number++;
    }
    
    cout << endl;
    
    return 0;
}
// Q: To Print numbers till the user given number using while loop

#include <iostream> 
using namespace std;

int main () {
    int  number, input;
    cout << "Enter a number to count till: " << "\n";
    cin >> input;
    
    while (number<=input) {
        cout << number << " ";
        number++;
    }

    cout << endl;
    
    return 0;

}
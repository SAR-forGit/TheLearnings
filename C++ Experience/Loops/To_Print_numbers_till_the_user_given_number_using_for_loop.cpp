// Q: To Print numbers till the user given number using for loop

#include <iostream> 
using namespace std;

int main() {
    int  number, input;
    cout << "Enter a number to count till: " << "\n";
    cin >> input;
    
    for (number=1; number<=input; number++) {
        cout << number << " ";
    }
    
    cout << endl;
    
    return 0;
}
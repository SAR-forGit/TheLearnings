// Q: Code to add odd-numbers till user name's number using While loop

#include <iostream> 
using namespace std;

int main () {
    int  number=1 , input;
    int oddsum = 0;
    
    cout << "Enter a number to count till: " << "\n";
    cin >> input;

    while (number<=input) {
        if (number%2 !=0) {
        oddsum += number; 
        }
        number++;
    }
    
cout <<"odd sum= " << oddsum << " ";
    
    return 0;
}
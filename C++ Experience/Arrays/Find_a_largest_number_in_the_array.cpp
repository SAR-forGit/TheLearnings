// Q: Find a largest number in the array

#include <iostream>
// INT_MAX and INT_MIN are available in <climits> library in programmiz
#include <climits>
using namespace std;

int main() {
    int largest = INT_MIN, sz;
    
    cout << "Enter size of an array: ";
    cin >> sz;
    
    int numbers[sz];
    
    cout << "Enter "<< sz << " numbers: "<< endl;
    
    // We can iterate until size of arra divided by size of datatype or we can just make a variable and store size of array in it
    
    for (int i=0; i< sizeof(numbers) / sizeof(int); i++) {
        cin >> numbers[i];
    }

    for (int i=0; i<sz; i++) {
        if (numbers[i] > largest) {
            largest = numbers[i];
        }
    }
    
    cout << "The largest number from the given array is: " << largest;
    
    return 0;
}
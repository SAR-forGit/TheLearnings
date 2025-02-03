// Q: Find a largest and smallest number in the array

#include <iostream>
// INT_MAX and INT_MIN are available in <climits> library in programmiz
#include <climits>
using namespace std;

int main() {
    int largest = INT_MIN, smallest = INT_MAX, sz;
    
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
    
    
    for (int i=0; i<sz; i++) {
        if (numbers[i] < smallest) {
            smallest = numbers[i];
        }
    }
    

    cout << endl << "The largest number from the given array is " << largest << endl << endl << "And" << endl << endl << "the smallest number from the given array is " << smallest;
    
    return 0;
}
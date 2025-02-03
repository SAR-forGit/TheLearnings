// Q: Print Pattern of Number till it

#include <iostream> 
using namespace std;

int main() {
    
    int givenNum, Number=1;
    
    cout <<"Enter the number to print its pattern of same number of row and same number of colmumn: ";
    cin >> givenNum;
    cout << "\n";
    
    cout << "Ans: \n";
    
    for (int n=1; n<=givenNum; n++) {
        for (int m=1; m<=givenNum; m++) {
            cout << m << " ";
        }
        cout << "\n";
        }
    
    return 0;
}
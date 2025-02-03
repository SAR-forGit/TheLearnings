// Q: Binomial Coefficient (nCr) using Function

#include <iostream>
using namespace std;

int Factorial (int a){
    int fact=1;
    for (int i=1; i<=a; i++) {
        fact *= i;
    }
    return fact;
}

int nCr (int n, int r) {
    int fact_n = Factorial(n);
    int fact_r = Factorial(r);
    int fact_nr = Factorial(n-r);
    
    return (fact_n / (fact_r * fact_nr));
}

int main() {
    
    int given_n, given_r;
    
    cout << "Enter a two numbers to calculate to find its binomial coefficient (nCr): "<< endl << "n= ";
    cin >> given_n;
    cout <<"r= ";
    cin >> given_r;
    
    cout << "Your Binomial factorial of " << given_n << "C" << given_r << " is " << nCr(given_n, given_r);
    
    return 0;
}
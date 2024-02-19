#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int main() {
    cout << "Write a function (example: y=x^2): " << endl;
    string function;
    cin >> function;
    cout << "Upper bound :" << endl;
    double upper;
    cin >> upper;
    cout << "Lower bound :" << endl;
    double lower;
    cin >> lower;
    cout << "Number of subintervals : n" << endl;
    double n;
    cin >> n;
    double x = (upper-lower)/n;
    cout << "delta x = " << abs(x);
    

}
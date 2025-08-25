#include <iostream>
using namespace std;

// Program to print Fibonacci series up to n terms
int main() {
    int n;

    cout<< "Enter the number of terms: ";
    cin >> n;

    int t1 = 0, t2 = 1;

    cout << "Fibonacci Series: ";

    for (int i = 1; i <= n; i++) {
        cout << t1 << " ";
        int nextTerm= t1 + t2;
        t1 = t2;
        t2 = nextTerm;
    }

    cout << endl;
    return 0;
}

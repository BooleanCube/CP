#include <iostream>
using namespace std;

int main() {
    int c; cin >> c;
    string a = c%2==0 && c>2 ? "YES" : "NO";
    cout << a;
    return 0;
}

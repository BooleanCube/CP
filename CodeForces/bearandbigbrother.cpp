#include <iostream>
using namespace std;

int main() {
    int l, b; cin >> l >> b;
    int s = 0;
    while(l<=b) {
        ++s;
        l*=3; b*=2;
    }
    cout << s;
    return 0;
}

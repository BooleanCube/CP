#include <iostream>
using namespace std;

int main() {
    int r, b; cin >> r >> b;
    int t = r+b; int d = 2;
    while(true) {
        int q = t/d; int re = t%d;
        if(re==0 && r==2*q+2*d-4) {
            cout << q << " " << d;
            break;
        } else ++d;
    }
    return 0;
}

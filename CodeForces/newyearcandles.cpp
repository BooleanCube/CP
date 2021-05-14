#include <iostream>
using namespace std;

int main() {
    int a, b; cin >> a >> b; int r=0; int total=0;
    while(a>0) {
        total += a; r += a;
        a=r/b; r-=(int)(r/b)*b;
    }
    cout << total;
    return 0;
}

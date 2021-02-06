#include <iostream>
using namespace std;

int main() {
    int x;
    int n;
    cin >> x >> n;
    int a = x*(n+1);
    for(int i=0; i<n; i++) {int c; cin >> c; a-=c;}
    cout << a;
    return 0;
}

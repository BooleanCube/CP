#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int l[n];
    for(int i=1; i<=n; i++) {
        cin >> l[n-i];
    }
    for(int a : l) {
        cout << a << "\n";
    }
}

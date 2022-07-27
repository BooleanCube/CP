#include <iostream>
using namespace std;

int main() {
    int n; cin >> n;
    for(int i=0; i<n; i++) {
        string a; cin >> a;
        int l = a.size();
        if(l>10) cout << a.substr(0,1) << l-2 << a.substr(l-1, 1) << "\n";
        else cout << a << "\n";
    }
    return 0;
}

#include <iostream>
using namespace std;

int main() {
    int n; cin >> n;
    int c=0;
    string p = "+";
    for(int i=0; i<n; i++) {
        string op; cin >> op;
        if(op.find(p) != string::npos) ++c;
        else --c;
    }
    cout << c;
}

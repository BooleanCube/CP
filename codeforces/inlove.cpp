#include <bits/stdc++.h>
using namespace std;

int main() {
    int q; cin >> q;
    multiset<int> a, b;
    for(int z=0; z<q; z++) {
        char op; int l, r; cin >> op >> l >> r;
        // cout << op << " " << l << " " << r << endl;
        if(op == '+') a.insert(l), b.insert(r);
        else a.erase(a.find(l)), b.erase(b.find(r));
        // for(int bruh : a) cout << bruh << " "; cout << endl;
        // for(int bruh : b) cout << bruh << " ";
        // cout << endl;
        if(a.size() == 0) {
            cout << "NO\n";
            continue;
        }
        int mxL = *(--a.end()), mnR = *(b.begin());
        if(mxL > mnR) cout << "YES\n";
        else cout << "NO\n";
    }
    return 0;
}
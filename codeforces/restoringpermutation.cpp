#include <algorithm>
#include <bits/stdc++.h>
using namespace std;

int main() {
    int t; cin >> t;
    while(t--) {
        int n; cin >> n;
        vector<int> b(n);
        int m = 0;
        for(int i=0; i<n; i++) {
            cin >> b[i];
            m = max(m, b[i]);
        }
        if(m >= 2*n) {
            cout << -1 << endl;
            continue;
        }
        multiset<int> unused;
        for(int i=1; i<=2*n; i++) {
            if(count(b.begin(), b.end(), i) == 0) {
                unused.insert(i);
            }
        }
        vector<int> a(2*n);
        bool flag = 1;
        for(int i=0; i<n; i++) {
            a[2*i] = b[i];
            auto it = unused.upper_bound(b[i]);
            if(it == unused.end()) {
                flag = 0;
                cout << -1;
                break;
            }
            a[2*i+1] = *it;
            unused.erase(it);
        }
        if(flag) for(int i : a) cout << i << " ";
        cout << endl;
    }
}

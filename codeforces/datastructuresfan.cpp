#include <bits/stdc++.h>
using namespace std;

#define endl "\n"

int main() {
    int tc; cin >> tc;
    while(tc--) {
        int n; cin >> n;
        vector<int> a(n);
        for(int i=0; i<n; i++) cin >> a[i];
        vector<int> px; px.push_back(0);
        for(int i=0; i<n; i++) px.push_back(px[i]^a[i]);
        string s; cin >> s;
        int onXor = 0, offXor = 0;
        for(int i=0; i<n; i++) {
            if(s[i]-'0') onXor ^= a[i];
            else offXor ^= a[i];
        }
        int m; cin >> m;
        for(int i=0; i<m; i++) {
            int op; cin >> op;
            if(op-1) {
                int g; cin >> g;
                cout << (g ? onXor : offXor) << " ";
            } else {
                int l, r; cin >> l >> r;
                int pXor = px[r]^px[l-1];
                onXor ^= pXor;
                offXor ^= pXor;
            }
        }
        cout << endl;
    }
}

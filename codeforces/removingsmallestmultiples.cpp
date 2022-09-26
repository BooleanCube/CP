#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int main() {
    int t; cin >> t;
    while(t--) {
        int n; cin >> n;
        string s; cin >> s;
        unordered_set<ll> *r = new unordered_set<ll>;
        vector<ll> *e = new vector<ll>;
        for(int i=1; i<=n; i++) {
            if(s[i-1] == '0') {
                r->insert(i);
                e->push_back(i);
            }
        }
        int rs = r->size();
        if(rs == 0) {
            cout << 0 << endl;
            continue;
        }
        if(rs == n) {
            cout << n << endl;
            continue;
        }
        vector<bool> vis(n+1, 0);
        ll sum = 0;
        for(ll i : *e) {
            ll j=1;
            while(1) {
                if(r->count(j*i)) {
                    if(!vis[j*i]) sum += i; 
                } else break;
                vis[j*i] = true;
                ++j;
            }
        }
        cout << sum << "\n";
    }
    return 0;
}

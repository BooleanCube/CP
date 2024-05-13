#include <bits/stdc++.h>
using namespace std;

#define ll long long

const int MOD = 1e9+7;

int main() {
    int n; cin >> n;
    vector<ll> a(n);
    for(ll &i : a) cin >> i;
    sort(a.begin(), a.end());

    for(int i=1; i<n-1; i++) {
        int cs = n-i+1;
        vector<ll> b(cs-1), nr(cs-1);
        multiset<array<ll, 3>> q;
        q.insert({a[0]+a[1], 0, 1}); nr[0] = 1;
        if(cs > 2) q.insert({a[1]+a[2], 1, 2});
        for(int i=0; i<cs-1; i++) {
            auto [v, l, r] = *q.begin(); q.erase(q.begin());
            if(nr[l] == 0 && l < cs-1) {
                q.insert({a[l+1]+a[l+2], l+1, l+2});
                nr[l] = r+1;
            }
            nr[l] = ++r;
            if(r < cs) q.insert({a[l]+a[r], l, r});
            b[i] = v;
        }
        a = b;
        ll rm = a[0] / MOD;
        for(ll &i : a) i -= rm*MOD;
    }

    cout << (a[0] + a[1]) % MOD << endl;

    return 0;
}
#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int main() {
    freopen("lifeguards.in", "r", stdin);
    freopen("lifeguards.out", "w", stdout);

    int n; cin >> n;
    vector<pair<ll, ll>> shifts(n);
    for(int i=0; i<n; i++) cin >> shifts[i].second >> shifts[i].first;
    sort(shifts.begin(), shifts.end());
    ll prev = 0;
    ll sum = 0;
    ll m = 1000000001;
    for(int i=0; i<n; i++) {
        ll s = shifts[i].second, e = shifts[i].first;
        ll g = max(0ll, min(e-prev, e-s));
        ll lp = m;
        if(i>0) lp = min(prev-shifts[i-1].second, s-shifts[i-1].second);
        if(i>1) lp = min(lp, s-shifts[i-2].first);
        m = min(m, lp);
        sum += g;
        prev = e;
    }
    cout << sum-m << endl;
}

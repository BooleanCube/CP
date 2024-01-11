#include <bits/stdc++.h>
using namespace std;

#define int long long

signed main() {
    int n, m; cin >> n >> m;
    vector<int> cities(n), towers(m);
    for(int i=0; i<n; i++) cin >> cities[i];
    for(int i=0; i<m; i++) cin >> towers[i];
    int ans = 0;
    for(int i=0; i<n; i++) {
        auto it = lower_bound(towers.begin(), towers.end(), cities[i]);
        int d = INT32_MAX;
        if(it != towers.end()) d = *it - cities[i];
        if(it != towers.begin()) d = min(d, cities[i] - *(--it));
        ans = max(ans, d);
    }
    cout << ans << endl;
    return 0;
}
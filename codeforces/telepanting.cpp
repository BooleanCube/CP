// AC

#include <algorithm>
#include <bits/stdc++.h>
#include <utility>
#include <vector>
using namespace std;

#define int long long

const int MOD = 998244353 ;

signed main() {
    int n; cin >> n;
    unordered_map<int, pair<int, int>> p;
    vector<int> xs;
    for(int i=0; i<n; i++) {
        int x, y, a; cin >> x >> y >> a;
        p[x] = make_pair(y, a);
        xs.push_back(x);
    }

    sort(xs.begin(), xs.end());
    vector<int> dp(n+1);
    int cur = 0, ans = xs[n-1]+1;
    while(cur < xs[n-1]) {
        int pidx = distance(xs.begin(), upper_bound(xs.begin(), xs.end(), cur));
        int next = xs[pidx];
        int ncur = p[next].first;
        int npidx = distance(xs.begin(), lower_bound(xs.begin(), xs.end(), ncur));
        int nnext = xs[npidx];
        int step = (next-ncur+dp[pidx]-dp[npidx])%MOD;
        if(p[next].second) ans += step;
        dp[pidx+1] = (step+dp[pidx])%MOD;
        cur = next;
        ans %= MOD;
    }

    if(ans < 0) ans += MOD;

    cout << ans << endl;
    return 0;
}

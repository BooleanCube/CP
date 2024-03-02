#include <bits/stdc++.h>
using namespace std;

#define int long long
typedef vector<int> vi;
typedef vector<vi> vvi;

int n;
vvi memo;
vi a;

const int MOD = 1e9+7;

int DP(int idx, int mask) {
    if(idx >= n) return 1;
    if(memo[idx][mask] != -1) return memo[idx][mask];
    int ans = 0;
    for(int i=0; i<n; i++) {
        if((mask & (1 << i) & a[idx])) {
            ans += DP(idx+1, mask^(1<<i));
            ans %= MOD;
        }
    }
    return memo[idx][mask] = ans;
}

signed main() {
    cin >> n;
    a = vi(n);
    for(int i=0; i<n; i++) {
        int mask = 0;
        for(int j=n-1; j>=0; j--) {
            int bit; cin >> bit;
            if(bit) mask |= (1 << j);
        }
        a[i] = mask;
    }
    memo = vvi(n, vi((1 << n)+1, -1));
    cout << DP(0, (1 << n)-1) << endl;
    return 0;
}

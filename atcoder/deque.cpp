#include <bits/stdc++.h>
using namespace std;

#define int long long
typedef vector<int> vi;
typedef vector<vi> vvi;

vi a;
vvi memo; // add third state (t) if WA

int DP(int l, int r, int t) {
    if(l == r) return memo[l][r] = (t & 1 ? -1 : 1) * a[l];
    if(memo[l][r] != -69420) return memo[l][r];
    if(t & 1) {
        int mn = 1e15;
        mn = min(mn, DP(l+1, r, t+1)-a[l]);
        mn = min(mn, DP(l, r-1, t+1)-a[r]);
        return memo[l][r] = mn;
    } else {
        int mx = -1e15;
        mx = max(mx, DP(l+1, r, t+1)+a[l]);
        mx = max(mx, DP(l, r-1, t+1)+a[r]);
        return memo[l][r] = mx;
    }
}

signed main() {
    int n; cin >> n;
    a = vi(n);
    for(int &i : a) cin >> i;
    memo = vvi(n, vi(n, -69420));
    cout << DP(0, n-1, 0) << endl;
    return 0;
}

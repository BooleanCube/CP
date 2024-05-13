#include<bits/stdc++.h>
using namespace std;

#define int long long
#define all(x) (x).begin(), (x).end()
#define all2(x) (x).begin() + 1, (x).begin() + 1 + n
#define ls id << 1
#define rs id << 1 | 1
#define endl '\n'
const int N = 1010;
const int mod = 998244353;
const int inf = 1e9+10;

void solve() {
    int n, m; cin >> n >> m;
    vector<int>ver(n+5), h;
    for(int i=1; i<=n; i++) cin >> ver[i];
    int l, r, y;
    for(int i=1; i<=m; i++){
        cin >> l >> r >> y;
        if(l > 1) continue;
        h.push_back(r);
    }
    sort(all2(ver));
    ver[n+1] = 1e9;
    sort(all(h));
    int ans = h.size();
    for(int i=1, j=0; i<=n+1; i++) {
        int tmp = i-1;
        while(j < h.size() && ver[i] > h[j]) j++;
        tmp += h.size() - j;
        ans = min(ans, tmp);
    }
    cout << ans << endl;
}

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int T = 1;
    // cin >> T;
    while(T--) solve();
    return 0;
}
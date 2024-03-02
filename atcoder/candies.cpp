#include <bits/stdc++.h>
using namespace std;

#define ll long long
typedef vector<ll> vl;
typedef vector<vl> vvl;

const ll MOD = 1e9+7;

int main() {
    int n, k; cin >> n >> k;
    vl a(n);
    for(ll &i : a) cin >> i;
    if(k == 0) {
        cout << 1 << endl;
        return 0;
    }
    vvl DP(n+1, vl(k+1));
    for(int i=0; i<=k; i++) DP[0][i] = 1;
    for(int i=0; i<=n; i++) DP[i][0] = 1;
    for(int i=1; i<=n; i++) {
        for(int j=1; j<=k; j++) {
            DP[i][j] += DP[i-1][j];
            if(j-a[i-1] > 0) DP[i][j] -= DP[i-1][j-a[i-1]-1] - MOD;
            DP[i][j] += DP[i][j-1];
            DP[i][j] %= MOD;
        }
    }
    cout << (DP[n][k] - DP[n][k-1] + MOD) % MOD << endl;
    return 0;
}

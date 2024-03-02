#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define vl vector<ll>
#define vll vector<vl>

const ll V = 1e5;

int main() {
    int n, W; cin >> n >> W;
    vector<array<ll, 2>> items(n);
    for(int i=0; i<n; i++) cin >> items[i][0] >> items[i][1];
    vll DP(n+1, vl(V+1, 1e9+1));
    DP[0][0] = 0;
    for(int i=0; i<=n; i++) DP[i][0] = 0;
    for(int i=1; i<=n; i++) {
        int v = items[i-1][1];
        for(int j=1; j<=V; j++) {
            if(j >= v) DP[i][j] = min(DP[i][j], DP[i-1][j-v]+items[i-1][0]);
            else DP[i][j] = min(DP[i][j], items[i-1][0]);
            DP[i][j] = min(DP[i][j], DP[i-1][j]);
        }
    }
    ll ans = 0;
    for(int i=0; i<=V; i++)
        if(DP[n][i] <= W)
            ans = i;
    cout << ans << endl;
    return 0;
}

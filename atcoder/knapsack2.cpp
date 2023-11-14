#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define vl vector<ll>
#define vll vector<vl>

const ll V = 20+1;

ll conversion(ll n) {
    if(n == 0) return V+10;
    return n;
}

int main() {
    int n, W; cin >> n >> W;
    vector<array<int, 2>> items(n);
    for(int i=0; i<n; i++) cin >> items[i][0] >> items[i][1];
    vll DP(n+1, vl(V, V+10));
    for(int i=1; i<=n; i++)
        DP[i][items[i-1][0]] = items[i-1][1];
    for(int i=0; i<n; i++) {
        int v = items[i][1];
        for(int j=v; j<V; j++) {
            DP[i][j] = min(DP[i][j], DP[i-1][j-v]+items[i][0]);
        }
    }
    for(int i=0; i<n; i++) {
        for(int num : DP[i]) cout << num << " ";
        cout << endl;
    }
    int ans = 0;
    for(int i=0; i<V; i++)
        if(DP[n-1][i] <= W)
            ans = i;
    cout << ans << endl;
    return 0;
}
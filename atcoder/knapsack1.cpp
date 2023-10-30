#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define vl vector<ll>
#define vll vector<vl>

int main() {
    int n, W; cin >> n >> W;
    vector<array<int, 2>> items(n);
    for(int i=0; i<n; i++)
        cin >> items[i][0] >> items[i][1];
    vll DP(n, vl(W+1));
    for(int j=items[0][0]; j<=W; j++) DP[0][j] = items[0][1];
    for(int i=1; i<n; i++) {
        ll w = items[i][0], v = items[i][1];
        for(int j=0; j<=W; j++) {
            DP[i][j] = max(DP[i][j], DP[i-1][j]);
            if(j <= W-w) {
                DP[i][j+w] = max(DP[i][j+w], DP[i-1][j]+v);
                DP[i][j+w] = max(DP[i][j+w], DP[i][j+w-1]);
                DP[i][j+w] = max(DP[i][j+w], DP[i-1][j+w]);
            }
        }
    }
    cout << DP[n-1][W] << endl;
    return 0;
}

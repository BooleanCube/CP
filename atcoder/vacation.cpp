#include <bits/stdc++.h>
using namespace std;

#define vi vector<int>
#define vii vector<vi>

int main() {
    int n; cin >> n;
    vector<array<int, 3>> days(n);
    for(int i=0; i<n; i++)
        cin >> days[i][0] >> days[i][1] >> days[i][2];
    vii dp(n, vi(3));
    for(int i=0; i<3; i++) dp[0][i] = days[0][i];
    for(int i=1; i<n; i++) {
        for(int j=0; j<3; j++) {
            int mx = dp[i][j];
            for(int k=0; k<3; k++) {
                if(k == j) continue;
                mx = max(mx, dp[i-1][k]);
            }
            dp[i][j] = max(dp[i][j], mx+days[i][j]);
        }
    }
    int ans = -1;
    for(int i=0; i<3; i++) ans = max(ans, dp[n-1][i]);
    cout << ans << endl;
    return 0;
}

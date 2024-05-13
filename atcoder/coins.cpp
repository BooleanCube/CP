#include <bits/stdc++.h>
using namespace std;

#define ld long double
typedef vector<ld> vd;
typedef vector<vd> vvd;

int main() {
    cout << fixed << setprecision(10);
    int n; cin >> n;
    vd p(n); for(ld &i : p) cin >> i;
    vvd DP(n, vd(n+1)); DP[0][0] = (1 - p[0]); DP[0][1] = p[0];
    for(int i=1; i<n; i++) {
        DP[i][0] = DP[i-1][0] * (1-p[i]);
        for(int j=1; j<=i+1; j++)
            DP[i][j] = (DP[i-1][j] * (1-p[i])) + (DP[i-1][j-1] * p[i]);
    }
    ld ans = 0;
    for(int i=n/2+1; i<=n; i++) ans += DP[n-1][i];
    cout << ans << endl;
    return 0;
}
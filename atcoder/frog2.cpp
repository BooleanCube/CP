#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, k; cin >> n >> k;
    vector<int> h(n);
    for(int i=0; i<n; i++) cin >> h[i];
    int start = 0;
    vector<int> dp(n, 1e9);
    dp[0] = 0;
    for(int i=0; i<n; i++) {
        for(int j=1; j<=k; j++) {
            if(i+j<n) dp[i+j] = min(dp[i+j], dp[i]+abs(h[i]-h[i+j]));
            else break;
        }
    }
    cout << dp[n-1] << endl;
    return 0;
}

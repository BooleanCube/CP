#include <bits/stdc++.h>
using namespace std;

#define int long long

int maximizeA(const vector<int>& arr, int n) {
    vector<vector<int>> dp(2, vector<int>(n, -1e9));
    dp[0][0] = arr[0];
    for (int i=1; i<n; i++) {
        dp[i&1][0] = dp[(i+1)&1][0] + arr[i];
        for (int j=1; j<=i; j++) {
            dp[i&1][j] = max(dp[(i+1)&1][j-1] + (j+1)*arr[i], dp[(i+1)&1][j] + (j+1)*arr[i]);
        }
    }
    int maxA = LLONG_MIN;
    for (int j = 0; j < n; j++) {
        maxA = max(maxA, dp[(n-1)&1][j]);
    }
    return maxA;
}

signed main() {
    int tc; cin >> tc;
    while(tc--) {
        int n; cin >> n;
        vector<int> arr(n);
        for (int i = 0; i < n; i++) cin >> arr[i];
        cout << maximizeA(arr, n) << endl;
    }
    return 0;
}

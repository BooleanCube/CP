#include <bits/stdc++.h>
#include <utility>
using namespace std;

int main(int argc, char *argv[]) {
    int n, m; cin >> n >> m;
    vector<int> powers(n+1);
    for(int i=1; i<=n; i++) cin >> powers[i];
    vector<pair<int, int>> dp(n+1);
    for(int i=n; i>0; i--) {
        int p = powers[i];
        if(i+p > n) dp[i] = make_pair(i, 1);
        else dp[i] = make_pair(dp[i+p].first, dp[i+p].second+1);
    }
    for(int i=0; i<m; i++) {
        int type; cin >> type;
        if(type) {
            for(int i=1; i<=n; i++) cout << dp[i].first << " " << dp[i].second << endl;
            cout << "-----------" << endl;
            int idx; cin >> idx;
            cout << dp[idx].first << " " << dp[idx].second << '\n';
        } else {
            int idx, p; cin >> idx >> p;
            if(idx+p > n) {
                dp[idx].first = idx;
                dp[idx].second = 1;
            } else {
                dp[idx].first = dp[idx+p].first;
                dp[idx].second = dp[idx+p].second+1;
            }
        }
    }
    return 0;
}

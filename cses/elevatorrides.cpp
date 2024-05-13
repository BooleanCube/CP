#include <bits/stdc++.h>
 
using namespace std;
 
#define int long long
#define sp <<" "<<
 
const int MAX_N = 20;
int n, x;
vector<int> w;
vector<vector<int>> memo;
 
int DP(int mask, int capLeft) {
    if(mask == 0) return 0;
    if(memo[mask][capLeft] != -1) return memo[mask][capLeft];
    int flag = 1, ans = 1e12;
    for(int i=0; i<n; i++) {
        if((mask & (1 << i)) && w[i] >= capLeft) {
            flag = 0;
            ans = min(ans, DP(mask ^ (1 << i), capLeft - w[i]));
        }
    }
    if(flag) return memo[mask][capLeft] = 1 + DP(mask, capLeft);
    return memo[mask][capLeft] = ans + 1;
}
 
signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
 
    cin >> n >> x;
    w = vector<int>(n);
    memo = vector<vector<int>>(1 << n, vector<int>(20, -1));
    memo[0] = 0;
    for (int &i : w) cin >> i;
 
    cout << DP((1 << n) - 1, x) << endl;
    return 0;
}
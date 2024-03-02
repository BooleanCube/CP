#include <bits/stdc++.h>
using namespace std;

#define int long long
typedef vector<int> vi;
typedef vector<vi> vvi;

const int MOD = 1e9+7;

signed main() {
    int n, m; cin >> n >> m;
    vvi DP(n, vi(m)), graph(n, vi(m));
    for(int i=0; i<n; i++) {
        string line; cin >> line;
        for(int j=0; j<m; j++)
            graph[i][j] = line[j] == '#';
    }
    DP[0][0] = 1;
    for(int i=0; i<n; i++) {
        for(int j=0; j<m; j++) {
            if(graph[i][j]) continue;
            if(i) DP[i][j] += DP[i-1][j];
            if(j) DP[i][j] += DP[i][j-1];
            DP[i][j] %= MOD;
        }
    }
    cout << DP[n-1][m-1] << endl;
    return 0;
}

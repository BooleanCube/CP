#include <bits/stdc++.h>
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;

vvi graph;
vi DP;

int dfs(int cur) {
    if(DP[cur]) return DP[cur];
    int lp = 1;
    for(int nbr : graph[cur]) {
        if(DP[nbr]) lp = max(lp, DP[nbr]+1);
        else lp = max(lp, dfs(nbr)+1);
    }
    return DP[cur] = lp;
}

int main() {
    int n, m; cin >> n >> m;
    graph = vvi(n+1, vi(0));
    DP = vi(n+1);
    for(int i=0; i<m; i++) {
        int a, b; cin >> a >> b;
        graph[a].push_back(b);
    }
    int ans = 0;
    for(int i=1; i<=n; i++) ans = max(ans, dfs(i));
    cout << ans-1 << endl;
    return 0;
}

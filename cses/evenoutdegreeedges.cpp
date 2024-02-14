#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<set<int>> graph;
vector<int> vis, out;

void dfs(int cur) {
    if(vis[cur]) return;
}

int main() {
    cin >> n >> m;
    graph = vector<set<int>>(n+1);
    vis = vector<int>(n+1), out = vector<int>(n+1);
    for(int i=0; i<m; i++) {
        int a, b; cin >> a >> b;
        graph[a].insert(b);
    }
    return 0;
}
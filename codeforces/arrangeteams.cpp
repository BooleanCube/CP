#include <bits/stdc++.h>
using namespace std;

int ans = 0, n, m, t;
map<int, set<int>> nope;

pair<int, int> nextcoord(pair<int, int> coord) {
    int x = coord.first, y = coord.second;
    if(y+1 < m) return make_pair(x, y+1);
    return make_pair(x+1, 0);
}

bool valid(int x, int y) {
    return x >= 0 && y >= 0;
}

void backtrack(vector<vector<int>>& grid, set<int>& used, pair<int, int> coord) {
    int cx = coord.first, cy = coord.second;
    if(cx >= n) {
        if(used.size() == t) ans++;
        return;
    }
    int rem = t - used.size();
    if(rem > (n-cx)*m + (m-cy)) return;
    for(int i=1; i<=t; i++) {
        if(used.count(i)) continue;
        if(valid(cx-1, cy) && nope[i].count(grid[cx-1][cy])) continue;
        if(valid(cx, cy-1) && nope[i].count(grid[cx][cy-1])) continue;
        used.insert(i);
        grid[cx][cy] = i;
        backtrack(grid, used, nextcoord(coord));
        grid[cx][cy] = 0;
        used.erase(i);
    }
    backtrack(grid, used, nextcoord(coord));
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
    int tc; cin >> tc;
    while(tc--) {
        cin >> n >> m >> t;
        int p; cin >> p;
        nope = map<int, set<int>>();
        for(int i=0; i<p; i++) {
            int a, b; cin >> a >> b;
            nope[a].insert(b);
            nope[b].insert(a);
        }
        ans = 0;
        vector<vector<int>> grid(n, vector<int>(m));
        set<int> used;
        backtrack(grid, used, make_pair(0, 0));
        if(ans == 0) cout << "impossible" << "\n";
        else cout << ans << "\n";
    }
    return 0;
}
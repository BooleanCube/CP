#include <bits/stdc++.h>
#include <utility>
using namespace std;

#define all(x) begin(x),end(x)

struct cell {
    int x, y;
    cell() {}
    cell(int x, int y): x(x), y(y) {}
};

inline bool operator< (const cell& a, const cell& b) { return make_pair(a.x,a.y) < make_pair(b.x,b.y); }

int n, m;
vector<string> grid;
int adj[4] = { 1, -1, 0, 0 };
string dirs = "UDRL";

bool valid(int x, int y) {
    return x >= 0 && x < n && y >= 0 && y < m;
}

pair<string, string> bfs(cell start) {
    deque<pair<cell, string>> q; q.push_back(make_pair(start, ""));
    set<cell> vis; string fpath = "";
    bool a = 0, m = 0;
    while(!q.empty()) {
        auto [cur, path] = q.front(); q.pop_front();
        if(m || (a && path.size()>fpath.size())) break;
        if(vis.count(cur)) continue;
        vis.insert(cur);
        int cx = cur.x, cy = cur.y;
        if(grid[cx][cy] == 'A') a = 1, fpath = path;
        if(grid[cx][cy] == 'M') m = 1;
        for(int k=0; k<4; k++) {
            if(a) break;
            int nx = cx+adj[k], ny = cy+adj[3-k];
            string np = path+dirs[k];
            if(!valid(nx, ny)) continue;
            if(grid[nx][ny] == '#') continue;
            cell nc(nx, ny);
            if(vis.count(nc)) continue;
            q.push_back(make_pair(nc, np));
        }
    }
    reverse(all(fpath));
    return make_pair((a && !m ? "YES" : "NO"), fpath);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n >> m;
    grid = vector<string>(n);
    int ax, ay;
    for(int i=0; i<n; i++) {
        cin >> grid[i];
        int idx = grid[i].find('A');
        if(idx != -1) ax = i, ay = idx;
    }
    vector<cell> starts;
    deque<cell> q; q.push_back(cell(ax, ay));
    set<cell> vis;
    while(!q.empty()) {
        cell cur = q.front(); q.pop_front();
        if(vis.count(cur)) continue;
        vis.insert(cur);
        int cx = cur.x, cy = cur.y;
        if(cx == 0 || cx == n-1 || cy == 0 || cy == m-1) starts.push_back(cur);
        for(int k=0; k<4; k++) {
            int nx = cx+adj[k], ny = cy+adj[3-k];
            if(!valid(nx, ny)) continue;
            if(grid[nx][ny] != '.') continue;
            cell nc(nx, ny);
            if(vis.count(nc)) continue;
            q.push_back(nc);
        }
    }
    bool flag = 1;
    for(cell start : starts) {
        // cout << start.x << " " << start.y << endl;
        auto [res, path] = bfs(start);
        if(res == "YES") {
            flag = 0;
            cout << res << endl << path.size() << endl << path << endl;
            break;
        }
    }
    if(flag) cout << "NO" << endl;
    return 0;
}

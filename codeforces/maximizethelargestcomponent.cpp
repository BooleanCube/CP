#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using pii = pair<int, int>;
using vi = vector<int>;
using vvi = vector<vi>;

#define sp <<" "<<

const int MAXN = 1e5 + 5;
const ll MOD = 1e9 + 7;
const ll HMOD = 998244353;
const ll INF = 1e9;
const double PI = 3.14159265358979323846;
const double EPS = 1e-9;

struct UF {
    vi e;
    UF(int n) : e(n, -1) {}
    bool sameSet(int a, int b) { return find(a) == find(b); }
    int size(int x) { return -e[find(x)]; }
    int find(int x) { return e[x] < 0 ? x : e[x] = find(e[x]); }
    bool join(int a, int b) {
        a = find(a), b = find(b);
        if (a == b) return false;
        if (e[a] > e[b]) swap(a, b);
        e[a] += e[b]; e[b] = a;
        return true;
    }
};

int n, m;

int idx2id(int i, int j) { return i * m + j; }

pii id2idx(int idx) { return {idx / m, idx % m}; }

void solve() {
    cin >> n >> m;
    vvi grid(n, vi(m));
    for (int i = 0; i < n; ++i) {
        string s; cin >> s;
        for (int j = 0; j < m; ++j) grid[i][j] = (s[j] == '#');
    }

    UF dsu(n * m);
    int adj[] = {1, -1, 0, 0};
    auto valid = [&](int i, int j) { return 0 <= i && i < n && 0 <= j && j < m; };

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (!grid[i][j]) continue;
            for (int k = 0; k < 4; ++k) {
                int ni = i + adj[k], nj = j + adj[3 - k];
                if (valid(ni, nj) && grid[ni][nj]) {
                    dsu.join(idx2id(i, j), idx2id(ni, nj));
                }
            }
        }
    }

    vector<pair<set<int>, int>> rows(n);
    vector<pair<set<int>, int>> cols(m);

    for (int i = 0; i < n; ++i) {
        set<int> ds; 
        int cnt = 0;
        for (int j = 0; j < m; ++j) {
            int above = (i > 0) ? idx2id(i - 1, j) : -1;
            int under = (i < n - 1) ? idx2id(i + 1, j) : -1;
            int cur = idx2id(i, j);
            int fa = (above != -1) ? dsu.find(above) : -1;
            int fu = (under != -1) ? dsu.find(under) : -1;
            int fc = dsu.find(cur);
            cnt += !grid[i][j];
            if (grid[i][j]) ds.insert(fc);
            if (above != -1 && grid[i - 1][j]) ds.insert(fa);
            if (under != -1 && grid[i + 1][j]) ds.insert(fu);
        }
        rows[i] = {ds, cnt};
    }

    for (int j = 0; j < m; ++j) {
        set<int> ds;
        int cnt = 0;
        for (int i = 0; i < n; ++i) {
            int left = (j > 0) ? idx2id(i, j - 1) : -1;
            int right = (j < m - 1) ? idx2id(i, j + 1) : -1;
            int cur = idx2id(i, j);
            int fl = (left != -1) ? dsu.find(left) : -1;
            int fr = (right != -1) ? dsu.find(right) : -1;
            int fc = dsu.find(cur);
            cnt += !grid[i][j];
            if (grid[i][j]) ds.insert(fc);
            if (left != -1 && grid[i][j - 1]) ds.insert(fl);
            if (right != -1 && grid[i][j + 1]) ds.insert(fr);
        }
        cols[j] = {ds, cnt};
    }

    int ans = 0;
    for(int i=0; i<n; i++) {
        int row = 0;
        for(int x : rows[i].first) row += dsu.size(x);
        for(int j=0; j<m; j++) {
            int cnt = row + rows[i].second + cols[j].second - (grid[i][j] ^ 1);
            for(int x : cols[j].first) if(!rows[i].first.count(x)) cnt += dsu.size(x);
            // for(int x : tog) cout << x << " ";
            // cout << endl;
            // cout << i sp j sp cnt << endl;
            ans = max(ans, cnt);
        }
    }

    cout << ans << endl;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    int tc;
    cin >> tc;
    while (tc--) {
        solve();
    }

    return 0;
}


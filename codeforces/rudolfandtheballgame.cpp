#include <bits/stdc++.h>
using namespace std;

const int MOD = 1000000007;
const int HMOD = 998244353;
const int MAXN = 100005;
const double INF = 1e20;
const double EPS = 1e-9;

int calc(int x, int d, int n, char c) {
    if (c == '1') x = (x - d + n) % n;
    else x = (x + d) % n;
    if (x == 0) x = n;
    return x;
}

void solve() {
    int n, m, x;
    cin >> n >> m >> x;
    vector<pair<int, char>> r(m);
    for (int i = 0; i < m; ++i) {
        cin >> r[i].first >> r[i].second;
    }

    vector<int> tr;
    for (int i = 0; i < m; ++i) {
        int d = r[i].first;
        char t = r[i].second;
        if (t == '?') tr.push_back(d);
        else x = calc(x, d, n, t);
    }

    set<int> s;
    s.insert(x);
    for (int d : tr) {
        set<int> ns;
        for (int v : s) {
            ns.insert(calc(v, d, n, '0'));
            ns.insert(calc(v, d, n, '1'));
        }
        s = ns;
    }

    cout << s.size() << endl;
    for (int v : s) {
        cout << v << " ";
    }
    cout << endl;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int testcases;
    cin >> testcases;
    for (int c = 1; c <= testcases; ++c) {
        // cout << "Case " << c << ": ";
        solve();
    }

    return 0;
}


#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;
const long long HMOD = 998244353;
const int MAXN = 100005;
const double INF = 1e20;
const double EPS = 1e-9;

int getint() {
    int x;
    cin >> x;
    return x;
}

vector<int> getlist() {
    string line;
    getline(cin >> ws, line);
    stringstream ss(line);
    vector<int> result;
    int value;
    while (ss >> value) {
        result.push_back(value);
    }
    return result;
}

vector<char> getstr() {
    string s;
    getline(cin >> ws, s);
    vector<char> result(s.begin(), s.end());
    return result;
}

void solve() {
    vector<int> nq = getlist();
    int n = nq[0], q = nq[1];
    vector<vector<pair<vector<char>, map<char, int>>>> grid(n, vector<pair<vector<char>, map<char, int>>>(n));
    
    for (int i = 0; i < q; ++i) {
        int op; cin >> op;
        if (op == 0) {
            char l; int x, y;
            cin >> l >> x >> y;
            grid[x][y].first.push_back(l);
            grid[x][y].second[l]++;
        } else if (op == 1) {
            int x, y;
            cin >> x >> y;
            if(grid[x][y].first.empty()) continue;
            char l = grid[x][y].first.back();
            grid[x][y].first.pop_back();
            grid[x][y].second[l]--;
        } else if (op == 2) {
            char l; int x, y;
            cin >> l >> x >> y;
            cout << (grid[x][y].second[l] > (grid[x][y].first.size() / 2) ? "yes" : "no") << endl;
        }
    }
}

int main() {
    int testcases = 1;
    for (int c = 1; c <= testcases; ++c) solve();
    return 0;
}


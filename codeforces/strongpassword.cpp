#include <algorithm>
#include <bits/stdc++.h>
#include <unordered_map>
#include <utility>
using namespace std;

bool backtrack(map<pair<int, int>, bool>& memo, int elem, int cidx, int m, string l, string r) {
    pair<int, int> p = make_pair(elem, cidx);
    if(cidx == m-1) {
        memo[p] = 0;
        return 0;
    }
    if(memo.count(p) > 0) return memo[p];
    bool success = 0;
    memo[p] = success;
    return success;
}

int main() {
    int t; cin >> t;
    while(t--) {
        string s; cin >> s;
        int n = s.size();
        int m; cin >> m;
        string l, r; cin >> l >> r;
        unordered_map<int, vector<int>> indices;
        for(int i=0; i<n; i++) {
            int val = s[i] - '0';
            if(indices.count(val) == 0) indices[val] = vector<int>();
            indices[val].push_back(i);
        }
        map<pair<int, int>, bool> memo;
        bool ans = 0;
        for(int i=l[0]-'0'; i<=r[0]-'0'; i++) {
            if(indices.count(i) == 0) continue;
            ans = ans || backtrack(memo, i, indices[i][0], m, l, r);
        }
        cout << (ans ? "YES" : "NO") << "\n";
    }
    return 0;
}

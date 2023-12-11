#include <bits/stdc++.h>
using namespace std;

int main() {
    int tc; cin >> tc;
    while(tc--) {
        int m, n, x; cin >> m >> n >> x;
        priority_queue<pair<int, int>> h;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> t;
        vector<int> ans(m);
        bool w = 1;
        int sum = 0;
        for(int i=0; i<m; i++) {
            int hi; cin >> hi;
            sum += hi;
            h.push(make_pair(hi, i));
        }
        if(m == n) {
            for(int i=0; i<n; i++) ans[i] = i+1;
        }
        else {
            int target = sum/n;
            vector<int> towers(n);
            for(int i=0; i<n;) {
                if(h.size() == 0) break;
                pair<int, int> cur = h.top(); h.pop();
                // cout << cur.first << " " << cur.second << " " << i << " " << towers[i] << endl;
                vector<pair<int, int>> skipped;
                if(towers[i] + cur.first <= target) {
                    towers[i] += cur.first;
                    ans[cur.second] = i+1;
                } else {
                    skipped.emplace_back(cur);
                    while(h.size()) {
                        pair<int, int> curr = h.top(); h.pop();
                        if(towers[i] + curr.first <= target) {
                            towers[i] += curr.first;
                            ans[curr.second] = i+1;
                            break;
                        }
                        else skipped.emplace_back(curr);
                    }
                    if(h.empty() && towers[i] < target) i++;
                }
                for(auto const& p : skipped) h.push(p);
                if(i < n && towers[i] >= target) i++;
            }
            for(int i=0; i<n; i++) t.push(make_pair(towers[i], i));
            while(h.size()) {
                pair<int, int> cur = h.top(); h.pop();
                pair<int, int> bt = t.top(); t.pop();
                ans[cur.second] = bt.second + 1;
                t.push(make_pair(bt.first+cur.first, bt.second));
            }
            for(int i=1; i<n; i++) {
                if(abs(towers[i]-towers[i-1]) > x) {
                    w = 0;
                    break;
                }
            }
        }
        if(w) {
            cout << "YES\n";
            for(int i=0; i<m; i++) cout << ans[i] << " \n"[i==m-1];
        } else {
            cout << "NO\n";
        }
    }
    return 0;
}
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n; cin >> n;
    string s; cin >> s;
    map<char, vector<int>> idxs;
    set<char> chrset;
    for(int i=0; i<n; i++) {
        idxs[s[i]].push_back(i);
        chrset.insert(s[i]);
    }
    int ans = INT32_MAX;
    for(int i=0; i<n; i++) {
        int l = i, r = i;
        for(char c : chrset) {
            auto it = lower_bound(idxs[c].begin(), idxs[c].end(), i);
            int cidx = i, cdist = INT32_MAX;
            if(it != idxs[c].end() && *it - i < cdist) {
                cdist = *it-i;
                cidx = *it;
            }
            if(it != idxs[c].begin() && i - *(--it) < cdist) {
                cdist = *it-i;
                cidx = *it;
            }
            if(cidx < i) l = min(l, cidx);
            else r = max(r, cidx);
        }
        ans = min(ans, r-l+1);
    }
    cout << ans << endl;
    return 0;
}
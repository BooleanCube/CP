#include <algorithm>
#include <bits/stdc++.h>
#include <set>
#include <utility>
using namespace std;

int main() {
    int n,m; cin >> n >> m;
    vector<pair<int, int>> r(n);
    for(int i=0; i<n; i++) {
        int a,s; cin >> a >> s;
        r[i] = make_pair(a, s);
    }
    sort(r.begin(), r.end());
    multiset<int> open;
    int counter = 0;
    for(int i=0; i<n; i++) {
        int a=r[i].first, s=r[i].second;
        auto it = open.lower_bound(a-m);
        if(it == open.end()) {
            open.insert(a+s);
            counter++;
            continue;
        }
        int val = *(it);
        if(val > a) {
            open.insert(a+s);
            counter++;
        } else {
            open.erase(it);
            open.insert(a+s);
        }
    }
    cout << n-counter << endl;
    return 0;
}

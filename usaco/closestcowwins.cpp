#include <bits/stdc++.h>
#include <utility>
using namespace std;
using ll = long long;

int main() {
    int k,m,n; cin >> k >> m >> n;
    vector<pair<ll, ll>> patches(k);
    for(int i=0; i<k; i++) {
        int p,t; cin >> p >> t;
        patches.push_back(make_pair(t, p));
    }
    sort(patches.begin(), patches.end());
    unordered_set<ll> nhoj(m);
    for(int i=0; i<m; i++) {
        int f; cin >> f;
        nhoj.insert(f);
    }
    ll tasty = 0;
    ll counter = 0;
    for(int i=0; i<k; i++) {
        if(counter >= n) break;
        if(nhoj.count(patches[i].second)) {
            counter++;
            tasty += patches[i].first;
        }
    }
    cout << tasty << endl;
    return 0;
}

#include <bits/stdc++.h>
using namespace std;
 
using ll = long long;
 
void update(vector<ll>& tree, int l, int r, ll u) {
    if(l == r) {
        tree[l] += u;
        return;
    }
    if(l%2 == 1) {
        tree[l] += u;
        l++;
    }
    if(l == r) {
        tree[l] += u;
        return;
    }
    if(r%2 == 0) {
        tree[r] += u;
        r--;
    }
    update(tree, l>>1, r>>1, u);
}
 
ll point(vector<ll>& tree, int idx) {
    ll sum = tree[idx];
    while(idx > 0) {
        idx >>= 1;
        sum += tree[idx];
    }
    return sum;
}
 
int main() {
    int n, q; cin >> n >> q;
    vector<ll> tree(2*n);
    for(int i=n; i<2*n; i++) {
        ll val; cin >> val;
        tree[i] = val;
    }
    for(int i=0; i<q; i++) {
        int type; cin >> type;
        if(type == 1) {
            int a, b;
            ll u;
            cin >> a >> b >> u;
            update(tree, n+a-1, n+b-1, u);
        } else if(type == 2) {
            int idx; cin >> idx;
            cout << point(tree, n+idx-1) << '\n';
        }
    }
}

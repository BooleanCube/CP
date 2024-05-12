#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for (int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
using ll = long long;
using pii = pair<int, int>;
using pll = pair<ll, ll>;
using vi = vector<int>;
using vl = vector<ll>;
#define f first
#define s second

struct segtree {
    int n;
    vl tree, lazy;
    vector<pii> rng;
    segtree(int N) : n(N) {
        tree = vl(n<<1), lazy = vl(n<<1);
        rng = vector<pii>(n<<1);
        rng[0] = _construct(1);
    }
    pii _construct(int idx) {
        if(idx >= n) return rng[idx] = {idx-n, idx-n};
        int ch = idx << 1; // left child
        pii lh = _construct(ch);
        pii rh = _construct(ch+1);
        return rng[idx] = {lh.f, rh.s};
    }
    ll _value(int idx, ll val) {
        return val * (rng[idx].s - rng[idx].f + 1);
    }
    void incUpdate(int l, int r, ll val) { _incUpdate(l+n, r+n, val); }
    void _incUpdate(int l, int r, ll val) {
        if(l == r) return void(lazy[l] += _value(l, val));
        if(l & 1) {
            lazy[l] += _value(l, val);
            return void(_incUpdate(l+1, r, val));
        }
        if(!(r & 1)) {
            lazy[r] += _value(r, val);
            return void(_incUpdate(l, r-1, val));
        }
        return _incUpdate(l>>1, r>>1, val);
    }
    ll query(int l, int r) { return _queryLazy(l+n, r+n, 0) + _querySeg(l+n, r+n, 0); }
    ll _queryLazy(int l, int r, ll t) {
        ll idx = (l&1 ? l : r), cnt = 0;
        if((l==r) || (l&1) || !(r&1)) {
            while(idx) {
                cnt += lazy[idx];
                idx >>= 1;
            }
        }
        if(l == r) return lazy[l] + _value(l, cnt) + t;
        if(l & 1) return _queryLazy(l+1, r, t + _value(l, cnt));
        if(!(r & 1)) return _queryLazy(l, r-1, t + _value(r, cnt));
        return _queryLazy(l>>1, r>>1, t);
    }
    ll _querySeg(int l, int r, ll t) {
        if(l == r) return tree[l] + t;
        if(l & 1) return _querySeg(l+1, r, t + tree[l]);
        if(!(r & 1)) return _querySeg(l, r-1, t + tree[r]);
        return _querySeg(l>>1, r>>1, t);
    }
};
 
int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin.exceptions(cin.failbit);
    return 0;
}

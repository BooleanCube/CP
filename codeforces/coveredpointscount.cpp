#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
#define int ll
const ll MAXX = 1e9+1;

struct node {
    ll lo, hi, md;
    ll val, delta;
    node *l = nullptr, *r = nullptr;
    node(ll blt, ll trt) {
        lo = blt; hi = trt;
        val = delta = 0;
        md = ((lo + hi) >> 1);
    }
    void check() {
        if (l == nullptr) {
            l = new node(lo, md);
            r = new node(md+1, hi);
        }
    }
    void update(ll blt, ll trt, ll add) {
        if(blt > hi || trt < lo) return;
        if(lo >= blt && hi <= trt) return void(delta += add);
        check(); prop();
        l->update(blt, trt, add); r->update(blt, trt, add);
        val = l->value() + r->value();
    }
    void prop() {
        l->delta += delta; r->delta += delta;
        delta = 0;
    }
    ll value() {
        return val + delta*(hi-lo+1);
    }
    ll query(ll blt, ll trt) {
        if(blt > hi || trt < lo) return 0;
        if(lo >= blt && hi <= trt) return value();
        check(); prop();
        val = l->value() + r->value();
        return l->query(blt, trt) + r->query(blt, trt);
    }
};

signed main() {
    cin.tie(0)->sync_with_stdio(0);
	cin.exceptions(cin.failbit);
    int n; cin >> n;
    node tree(-1, MAXX);
    vector<array<int, 2>> segs;
    set<int> coords;
    for(int i=0; i<n; i++) {
        int a, b; cin >> a >> b;
        coords.insert(a); coords.insert(b);
        segs.push_back({a, b});
    }
    map<int, int> cc; int id = 0;
    for(int e : coords) {
        cc[e] = id;
        id += 2;
    }
    for(auto seg : segs)
        tree.update(cc[seg[0]], cc[seg[1]], 1);
    vector<int> ans(n+1);
    int l = *coords.begin();
    ans[tree.query(cc[l], cc[l])]++;
    for(auto it = ++coords.begin(); it != coords.end(); it++) {
        int r = *it;
        ans[tree.query(cc[r], cc[r])]++;
        ans[tree.query(cc[r]-1, cc[r]-1)] += (r - l - 1);
        l = r;
    }
    for(int i=1; i<=n; i++) cout << ans[i] << " \n"[i==n];
    return 0;
}
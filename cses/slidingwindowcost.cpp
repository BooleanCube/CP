#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#include <ios>

using namespace std;
using namespace __gnu_pbds;

#define ll long long
#define int ll
#define sp <<" "<<

typedef pair<ll, ll> pll;
#define f first
#define s second
#define all(x) x.begin(),x.end()

struct ost_multiset {
    typedef pair<int, unsigned> pii;
    typedef tree<
        pii,
        null_type,
        less<pii>,
        rb_tree_tag,
        tree_order_statistics_node_update
    > ost;

    ost s;
    unsigned cnt = 0;

    ost_multiset() = default;
    ost_multiset(initializer_list<int> l) {
        for (int x : l) insert(x);
    }
    void insert(int x) { s.insert({x, cnt++}); }
    ost::iterator find_by_order(int k) { return s.find_by_order(k); }
    void erase(int x) {
        auto it = s.lower_bound({x, 0});
        erase(it); // erases only 1 element
        // while(it != s.end() && it->first == x) erase(it++);
    }
    void erase(ost::iterator it) { s.erase(it); }
    size_t size() const { return s.size(); }
};

const int MAXN = 2e5+2;

ost_multiset ost;
vector<pll> seg(MAXN<<1);
int n, k, id;
vector<int> ans, ccr(MAXN);
map<int, int> cc;


pll op(pll a, pll b) { return {a.f + b.f, a.s + b.s}; }

pll query(int l, int r, pll t) {
    if(l == r) return op(seg[l], t);
    if(l & 1) return query(l+1, r, op(t, seg[l]));
    if((r+1) & 1) return query(l, r-1, op(t, seg[r]));
    return query(l>>1, r>>1, t);
}

pll query(int l, int r) { return query(MAXN+l, MAXN+r, {0, 0}); }

void update(int idx, pll val) {
    idx += MAXN;
    while(idx) {
        seg[idx] = op(seg[idx], val);
        idx >>= 1;
    }
}

int cost() {
    int median = ost.find_by_order((k-1)>>1)->first;
    pll lc = query(0, median-1), rc = query(median+1, MAXN);
    // cout << lc.f sp lc.s sp " " sp rc.f sp rc.s << endl;
    // cout << st.query(0, median-1) sp st.query(median+1, 1e9) << endl;
    return (ccr[median]*lc.s - lc.f) + (rc.f - ccr[median]*rc.s);
}

signed main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    cin >> n >> k;
    int len = n-k+1;

    vector<int> nums(n);
    for(int &i : nums) cin >> i;
    set<int> snums; for(int num : nums) snums.insert(num);
    for(int num : snums) ccr[++id] = num, cc[num] = id;

    for(int i=0; i<k; i++) {
        ost.insert(cc[nums[i]]);
        update(cc[nums[i]], {nums[i], 1});
    }
    ans = vector<int>(len); ans[0] = cost();
    for(int i=k; i<n; i++) {
        int sz = ost.size();
        ost.erase(cc[nums[i-k]]); update(cc[nums[i-k]], {-nums[i-k], -1});
        ost.insert(cc[nums[i]]); update(cc[nums[i]], {nums[i], 1});
        ans[i-k+1] = cost();
    }

    for(int i=0; i<len; i++) cout << ans[i] << " \n"[i == len-1];
    return 0;
}

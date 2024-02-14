#include <bits/stdc++.h>
using namespace std;

template <int N> struct implicit_seg_tree {
    using dt = long long; /**< min, number of mins */
    static dt op(const dt& le, const dt& ri) {
        return le + ri;
    }
    static constexpr dt unit = 0;
    struct node {
        dt val;
        long long lazy = 0;
        int lch = -1, rch = -1;
    } tree[N];
    int ptr = 0, root_l, root_r; /**< [root_l, root_r) defines range of root node; handles negatives */
    implicit_seg_tree(int le, int ri) : root_l(le), root_r(ri) {
        tree[ptr++].val = 0;
    }
    inline void apply(int le, int ri, long long add, int u) {
        tree[u].val += add * (ri-le);
        tree[u].lazy += add;
    }
    inline void push(int tl, int tm, int tr, int u) {
        if (tr - tl > 1 && tree[u].lch == -1) {
            assert(ptr + 1 < N);
            tree[u].lch = ptr;
            tree[ptr++].val = 0;
            tree[u].rch = ptr;
            tree[ptr++].val = 0;
        }
        if (tree[u].lazy) {
            apply(tl, tm, tree[u].lazy, tree[u].lch);
            apply(tm, tr, tree[u].lazy, tree[u].rch);
            tree[u].lazy = 0;
        }
    }
    /**
     * @param le,ri defines range [le, ri)
     */
    void update(int le, int ri, long long add) {update(le, ri, add, root_l, root_r, 0);}
    void update(int le, int ri, long long add, int tl, int tr, int u) {
        if (ri <= tl || tr <= le)
            return;
        if (le <= tl && tr <= ri)
            return apply(tl, tr, add, u);
        int tm = tl + (tr - tl) / 2;
        push(tl, tm, tr, u);
        update(le, ri, add, tl, tm, tree[u].lch);
        update(le, ri, add, tm, tr, tree[u].rch);
        tree[u].val = op(tree[tree[u].lch].val,
                         tree[tree[u].rch].val);
    }
    void clear() {clear(root_l, root_r, 0); ptr = 1;}
    void clear(int tl, int tr, int u) {
        bool has_lch = tree[u].lch != -1;
        bool has_rch = tree[u].rch != -1;
        int tm = tl + (tr - tl) / 2;
        if(has_lch) clear(tl, tm, tree[u].lch);
        if(has_rch) clear(tm, tr, tree[u].rch);
        tree[u].val = 0;
        tree[u].lazy = 0;
        tree[u].lch = -1;
        tree[u].rch = -1;
    }
    /**
     * @param le,ri defines range [le, ri)
     */
    dt query(int le, int ri) {return query(le, ri, root_l, root_r, 0);}
    dt query(int le, int ri, int tl, int tr, int u) {
        if (ri <= tl || tr <= le)
            return unit;
        if (le <= tl && tr <= ri)
            return tree[u].val;
        int tm = tl + (tr - tl) / 2;
        push(tl, tm, tr, u);
        return op(query(le, ri, tl, tm, tree[u].lch),
                  query(le, ri, tm, tr, tree[u].rch));
    }
};

implicit_seg_tree<10000000> ist(-(1e9+1), 1e9+1);

#define ll long long

int main() {
    int tc; cin >> tc;
    while(tc--) {
        int n; cin >> n;
        vector<array<int, 2>> ppl(n);
        for(int i=0; i<n; i++) {
            int a, b; cin >> a >> b;
            ppl[i] = {b, a};
        }
        sort(ppl.begin(), ppl.end());
        ll ans = 0;
        for(int i=0; i<n; i++) {
            auto [b, a] = ppl[i];
            // cout << i << " " << ist.query(a, b) << endl;
            ans += ist.query(a, b+1);
            ist.update(a, a+1, 1);
        }
        cout << ans << endl;
        ist.clear();
    }
    return 0;
}
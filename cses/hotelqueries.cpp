#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

struct node {
    ll lo, hi, md;
    set<int> val, delta;
    node *l = nullptr, *r = nullptr;
    set<int> op(set<int> &a, set<int> &b) {
        if(*a.begin() > *b.begin()) return b;
        else return a;
    }
    node(ll blt, ll trt) {
        lo = blt; hi = trt;
        md = ((lo + hi) >> 1);
    }
    void check() {
        if (l == nullptr) {
            l = new node(lo, md);
            r = new node(md+1, hi);
        }
    }
    void update(ll blt, ll trt, set<int> add) {
        if(blt > hi || trt < lo) return;
        if(lo >= blt && hi <= trt) return void(delta.insert(add.begin(), add.end()));
        check(); prop();
        l->update(blt, trt, add); r->update(blt, trt, add);
        val = op(l->value(), r->value());
    }
    void prop() {
        l->delta.insert(delta.begin(), delta.end()); r->delta.insert(delta.begin(), delta.end());
        delta.clear();
    }
    set<int> value() {
        return op(val, delta);
    }
    set<int> query(ll blt, ll trt) {
        if(blt > hi || trt < lo) return set<int>();
        if(lo >= blt && hi <= trt) return value();
        check(); prop();
        val = op(l->value(), r->value());
        return op(l->query(blt, trt), r->query(blt, trt));
    }
};

int main() {
    return 0;
}

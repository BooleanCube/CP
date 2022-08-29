#include <algorithm>
#include <iostream>
#include <climits>
#include <vector>
using namespace std;
typedef long long ll;

void update(vector<ll>& seg, int idx) {
    ll p = seg[idx];
    while(idx > 1) {
        idx >>= 1;
        seg[idx] = min(p, seg[idx]);
    }
}

ll getMin(vector<ll>& seg, int f, int l, ll m) {
    if(f == l) return min(seg[f], m);
    if(f%2 == 1) { m = min(m, seg[f]); f++; }
    if(f == l) return min(seg[f], m);
    if(l%2 == 0) { m = min(seg[l], m); l--; }
    return getMin(seg, f>>1, m>>1, m);
}

int main (int argc, char *argv[]) {
    cin.tie(0)->sync_with_stdio(0);
    int n,q; cin >> n >> q;
    vector<ll> seg(2*n, LLONG_MAX);
    for(int i=n; i<2*n; i++) { cin >> seg[i]; update(seg, i); }
    for(int i=0; i<q; i++) {
        int t, f, l; cin >> t >> f >> l;
        if(t == 1) { seg[f+n-1] = l; update(seg, f+n-1); }
        if(t == 2) cout << getMin(seg, f+n-1, l+n-1, LLONG_MAX) << "\n";
    }
    return 0;
}

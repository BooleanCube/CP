#include <bits/stdc++.h>
using namespace std;

using ll = long long;

void increment(vector<ll>& lazy, int l, int r, ll val) {
	if(l == r) { lazy[l] += val; return; }
	if(l%2 == 1) { lazy[l] += val; l++; }
	if(l == r) { lazy[r] += val; return; }
	if(r%2 == 0) { lazy[r] += val; r--; }
	increment(lazy, l>>1, r>>1, val);
}

void setupdate(vector<ll>& lazy, vector<ll>& tree, int l, int r, ll val) {
	if(l == r) { lazy[l] = val-tree[l]; return; }
	if(l%2 == 1) { lazy[l] = val-tree[l]; l++; }
	if(l == r) { lazy[r] = val-tree[r]; return; }
	if(r%2 == 0) { lazy[r] = val-tree[r]; r--; }
	setupdate(lazy, tree, l>>1, r>>1, val);
}

ll sum(vector<ll>& tree, vector<ll>& lazy, int l, int r, ll m) {
	
}

int main() {
	int n, q; cin >> n >> q;
	vector<ll> tree(2*n, 0);
	vector<ll> lazy(2*n, 0);
	for(int i=n; i<2*n; i++) {
		cin >> tree[i];
		int b = i;
		while(b>1) {
			b>>=1;
			tree[b] += tree[i];
		}
	}
	for(int i=0; i<q; i++) {
		int type; cin >> type;
		if(type == 1) {
			int l, r; cin >> l >> r;
			ll val; cin >> val;
			increment(lazy, l, r, val);
		} else if(type == 2) {
			int l, r; cin >> l >> r;
			ll val; cin >> val;
			setupdate(lazy, tree, l, r, val);
		} else if(type == 3) {
			int l, r; cin >> l >> r;
			cout << sum(tree, lazy, n+l-1, n+r-1, 0) << '\n';
		}
	}
	return 0;
}

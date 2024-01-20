// Source: https://usaco.guide/general/io

#include <bits/stdc++.h>
using namespace std;

auto rng = std::default_random_engine {};

struct dsu {
	vector<int> par, sz;
	dsu(int n) {
		sz = par = vector<int>(n, 1);
		iota(par.begin(), par.end(), 0);
	}
	int find(int u) { if(par[u] != u) par[u] = find(par[u]); return par[u]; }
	bool join(int u, int v) {
		u = find(u); v = find(v); if(u == v) return 0;
		if(sz[u] < sz[v]) swap(u, v);
		par[v] = u; sz[u] += sz[v]; return 1;
	}	
};

int main() {
	freopen("wormsort.in", "r", stdin);
	freopen("wormsort.out", "w", stdout);
	int n, m; cin >> n >> m;
	vector<int> p(n);
	for(int i=0; i<n; i++) { cin >> p[i]; p[i]--; }
	vector<int> mismatched;
	for(int i=0; i<n; i++) {
		if(p[i] != i) {
			mismatched.push_back(i);
			// cout << i << endl;
		}
	}
	vector<array<int, 3>> edges(m);
	for(int i=0; i<m; i++) {
		cin >> edges[i][1] >> edges[i][2] >> edges[i][0];
		edges[i][1]--; edges[i][2]--;
	}
	if(mismatched.size() == 0) {
		cout << -1 << endl;
		return 0;
	}
	shuffle(mismatched.begin(), mismatched.end(), rng);
	sort(edges.begin(), edges.end());
	reverse(edges.begin(), edges.end());
	dsu DSU(n);
	int ans = 0;
	for(int i=0; i<m; i++) {
		auto [w, a, b] = edges[i];
		if(DSU.join(a, b)) ans = w;
		int s = DSU.find(mismatched[0]), f = 1;
		for(int j=1; j<mismatched.size(); j++) {
			if(DSU.find(mismatched[j]) != s) {
				f = 0;
				break;
			}
		}
		if(f) break;
	}
	cout << ans << endl;
}

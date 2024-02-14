#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

const ll inf = 1e18;
struct Ed { int a, b, w, s() { return a < b ? a : -a; }};
struct Node { ll dist = inf; int prev = -1; };

void bellmanFord(vector<Node>& nodes, vector<Ed>& eds, int s) {
	nodes[s].dist = 0;
	sort(all(eds), [](Ed a, Ed b) { return a.s() < b.s(); });

	int lim = sz(nodes) / 2 + 2; // /3+100 with shuffled vertices
	rep(i,0,lim) for (Ed ed : eds) {
		Node cur = nodes[ed.a], &dest = nodes[ed.b];
		if (abs(cur.dist) == inf) continue;
		ll d = cur.dist + ed.w;
		if (d < dest.dist) {
			dest.prev = ed.a;
			dest.dist = (i < lim-1 ? d : -inf);
		}
	}
	rep(i,0,lim) for (Ed e : eds) {
		if (nodes[e.a].dist == -inf)
			nodes[e.b].dist = -inf;
	}
}
 
int main() {
    cin.tie(0)->sync_with_stdio(0);
	cin.exceptions(cin.failbit);
    int tc; cin >> tc;
    while(tc--) {
        int n, m; cin >> n >> m;
        vector<pair<int, int>> adj[n];
        // vector<Node> nodes(n, Node()); vector<Ed> edges;
        for(int i=0; i<m; i++) {
            int u, v, w; cin >> u >> v >> w;
            // edges.push_back(Ed(--u, --v, w));
            // edges.push_back(Ed(v, u, w));
            adj[--u].emplace_back(--v, w);
            adj[v].emplace_back(u, w);
        }
        vector<int> s(n);
        for(int i=0; i<n; i++) cin >> s[i];

        vector<vector<ll>> dist(n, vector<ll>(1001, inf));
        vector<vector<bool>> vis(n, vector<bool>(1001, false));
        
        dist[0][s[0]] = 0;
        priority_queue<array<ll, 3>> q;
        q.push({0, 0, s[0]});
        while(!q.empty()) {
            int u = q.top()[1], k = q.top()[2];
            q.pop();
            if(vis[u][k] || dist[u][k] == inf) continue;
            vis[u][k] = true;
            for(auto x: adj[u]) {
                int v = x.first, w = x.second;
                int c = min(s[v], k);
                if(dist[v][c] > dist[u][k] + 1LL * w * k) {
                    dist[v][c] = dist[u][k] + 1LL * w * k;
                    q.push({-dist[v][c], v, c});
                }
            }
        }
        ll ans = inf;
        for(int k=1; k<1001; k++) ans = min(ans, dist[n-1][k]);
        cout << ans << "\n";
    }
}
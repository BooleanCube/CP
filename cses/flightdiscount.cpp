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
#define sp <<" "<<
#define endl "\n" // remove when debugging

const pll INF = {1e16, 1e16};

int main() {
    int n, m; cin >> n >> m;
    vector<vector<pll>> graph(n);
    rep(i, 0, m) {
        ll a, b, w; cin >> a >> b >> w;
        a--, b--;
        graph[a].push_back({b, w});
    }
    vector<pll> dist(n, INF);
    priority_queue<array<ll, 3>, vector<array<ll, 3>>, greater<array<ll, 3>>> pq;
    pq.push({0, 0, 0});
    while(!pq.empty()) {
        auto [psm, pmx, cur] = pq.top(); pq.pop();
        pll nxt = {psm, pmx};
        if(dist[cur] <= nxt) continue;
        dist[cur] = nxt;
        for(auto [nbr, wt] : graph[cur]) {
            ll npsm = psm, npmx = pmx;
            if(wt > pmx && pmx) {
                npsm -= (npmx >> 1) - (npmx) - (wt >> 1);
                npmx = wt;
            } else if(-1 < pmx && !pmx) {
                npsm += (wt >> 1);
                npmx = wt;
            } else npsm += wt;
            pll nxt = {npsm, npmx};
            if(dist[nbr] <= nxt) continue;
            pq.push({nxt.f, nxt.s, nbr});
        }
    }
    for(pll p : dist) {
        cout << "{" << p.f << " " << p.s << "}" << endl;
    }
    cout << dist[n-1].f << endl;
    return 0;
}
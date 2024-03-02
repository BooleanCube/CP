#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<ll> vl;
typedef vector<vl> vvl;
#define sp <<" "<<

const ll MOD = 1e9+7;

vvl graph;
vvl memo;

int DP(int cur, int par, int pCol) {
    if(pCol) {
        if(memo[cur][1] != -1 && memo[cur][0] != -1)
            return (memo[cur][1] + memo[cur][0]) % MOD;
        int f = 1;
        memo[cur][0] = 1; memo[cur][1] = 1;
        for(int nbr : graph[cur]) {
            if(nbr == par) continue;
            f = 0;
            memo[cur][0] *= DP(nbr, cur, 0);
            memo[cur][0] %= MOD;
            memo[cur][1] *= DP(nbr, cur, 1);
            memo[cur][1] %= MOD;
        }
        if(f) return 2;
        else return (memo[cur][0] + memo[cur][1]) % MOD;
    } else {
        if(memo[cur][1] != -1) return memo[cur][1];
        int f = 1;
        memo[cur][1] = 1;
        for(int nbr : graph[cur]) {
            if(nbr == par) continue;
            f = 0;
            memo[cur][1] *= DP(nbr, cur, 1);
            memo[cur][1] %= MOD;
        }
        if(f) return 1;
        else return (memo[cur][1]) % MOD;
    }
}

int main() {
    int n; cin >> n;
    graph = vvl(n, vl(0));
    memo = vvl(n, vl(2, -1));
    for(int i=0; i<n-1; i++) {
        int a, b; cin >> a >> b;
        a--; b--;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }
    cout << DP(0, 0, 1) << endl;
    return 0;
}

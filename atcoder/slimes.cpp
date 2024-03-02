#include <bits/stdc++.h>
using namespace std;

#define ll long long
typedef vector<ll> vl;
typedef vector<vl> vvl;
typedef pair<ll, ll> pll;
typedef vector<pll> vpl;
typedef vector<vpl> vvpl;
#define f first
#define s second

vl a;
vvpl memo;

// only if you could combine 2 starting or ending elements
pll DPF(int l, int r) {
    if(l+1 == r) return memo[l][r] = {a[l]+a[r], a[l]+a[r]};
    if(memo[l][r].f != -69420) return memo[l][r];
    pll left = DPF(l+1, r), right = DPF(l, r-1);
    pll mn = {left.f+left.s+a[l], left.s+a[l]};
    mn = min(mn, {right.f+right.s+a[r], right.s+a[r]});
    return memo[l][r] = mn;
}

int main() {
    int n; cin >> n;
    a = vl(n); for(ll &i : a) cin >> i;
    // memo = vvpl(n, vpl(n, {-69420, 0}));
    vvpl DP(n, vpl(n, {1e16, 1e16}));
    for(int i=0; i<n; i++) DP[i][i] = {0, a[i]};
    for(int l=1; l<n; l++) {
        for(int i=0; i<n-l; i++) {
            int j = i+l;
            for(int k=i; k<j; k++) {
                ll sm = DP[i][k].s + DP[k+1][j].s;
                pll np = {DP[i][k].f+DP[k+1][j].f+sm, sm};
                DP[i][j] = min(DP[i][j], np);
            }
        }
    }
    cout << DP[0][n-1].f << endl;
    return 0;
}


#include <bits/stdc++.h>
using namespace std;

#define int long long
typedef vector<int> vi;
typedef vector<vi> vvi;

void solve() {
    int n, m; cin >> n >> m;
    vvi a(n, vi(m));
    for(int i=0; i<n; i++)
        for(int j=0; j<m; j++)
            cin >> a[i][j];
    int los = 0, his = min(n, m);
    while(los < his) {
        int s = los + (his - los + 1) / 2;
        vvi pref(n+1, vi(m+1));
        for(int i=0; i<n; i++) {
            for(int j=0; j<m; j++) {
                if(a[i][j] >= s) pref[i+1][j+1]++;
                pref[i+1][j+1] += pref[i][j+1] + pref[i+1][j] - pref[i][j];
            }
        }
        bool w = 0;
        for(int i=0; i<=n-s; i++) {
            if(w) break;
            for(int j=0; j<=m-s; j++) {
                int val = pref[i+s][j+s] - pref[i][j+s] - pref[i+s][j] + pref[i][j];
                if(val >= s*s) {
                    w = 1;
                    break;
                }
            }
        }
        if(w) los = s;
        else his = s-1;
    }
    cout << los << endl;
}

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t; cin >> t;
    while(t--) solve();
    return 0;
}
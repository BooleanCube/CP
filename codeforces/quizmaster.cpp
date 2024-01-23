#include <bits/stdc++.h>
using namespace std;

#define all(v) v.begin(), v.end()
#define var(x, y, z) cout << x << " " << y << " " << z << endl;
#define ll long long
#define pii pair<ll, ll>
#define pb push_back
#define f first
#define s second

ll n, m;
const ll inf = 1e17;
const ll MAXM = 1e5;
vector<ll> facts[MAXM + 5];

void getfacts() {
    for(ll i=1; i<=MAXM; i++)
        for(ll j=i; j<=MAXM; j+=i)
            facts[j].pb(i);
}

void solve() {
    cin >> n >> m;
    vector<pii> vec;
    for(ll i=0; i<n; i++) {
        ll value; cin >> value;
        vec.pb({value, i});
    }
    sort(all(vec));
    vector<ll> fq(m + 5, 0);
    ll ccnt = 0, j = 0, ans = inf;
    for(ll i=0; i<n; i++) {
        for(auto x : facts[vec[i].f]) {
            if (x > m) break;
            if (!fq[x]++) ccnt++;
        }
        while(ccnt == m) {
            ll cans = vec[i].f - vec[j].f;
            if(cans < ans) ans = cans;
            for(auto x : facts[vec[j].f]) {
                if (x > m) break;
                if (--fq[x] == 0) ccnt--;
            }
            j++;
        }
    }
    cout << (ans >= inf ? -1 : ans) << "\n";
}

int main() {
    getfacts();
    ll t; cin >> t;
    while(t--) solve();
    return 0;
}
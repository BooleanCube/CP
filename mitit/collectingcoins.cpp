#include <bits/stdc++.h>
using namespace std;


/* TYPES  */
#define ll long long
#define int ll
#define ld long double
#define pii pair<int, int>
#define pll pair<long long, long long>
#define vi vector<int>
#define vll vector<long long>
#define mii map<int, int>
#define si set<int>
#define sc set<char>

/* CONSTANTS */
#define f first
#define s second
#define sp <<" "<<
#define endl '\n'
const int MAXN = 1e5+5;
const ll MOD = 1e9+7;
const ll HMOD = 998244353;
const ll INF = 1e9;
const ld PI = 3.1415926535897932384626433832795;
const ld EPS = 1e-9;

/* UTILS */
#define read(type) readInt<type>()
ll min(ll a,int b) { if (a<b) return a; return b; }
ll max(ll a,int b) { if (a>b) return a; return b; }
ll gcd(ll a,ll b) { if (b==0) return a; return gcd(b, a%b); }
ll lcm(ll a,ll b) { return a/gcd(a,b)*b; }
string to_upper(string a) { for (int i=0;i<(int)a.size();++i) if (a[i]>='a' && a[i]<='z') a[i]-='a'-'A'; return a; }
string to_lower(string a) { for (int i=0;i<(int)a.size();++i) if (a[i]>='A' && a[i]<='Z') a[i]+='a'-'A'; return a; }
bool prime(ll a) { if (a==1) return 0; for (int i=2;i<=round(sqrt(a));++i) if (a%i==0) return 0; return 1; }
void yes() { cout<<"YES\n"; }
void no() { cout<<"NO\n"; }

/* FUNCTIONS */
#define sz(a) ((int)a.size())
#define all(a) (a).begin(), (a).end()
#define fr(i,s,e) for(int i=(s);i<(e);i++)
#define frn(i,n) fr(i,0,(n))
#define cfr(i,s,e) for(int i=(s);i<=(e);i++)
#define rfr(i,e,s) for(long long int i=(e)-1;i>=(s);i--)
#define afr(a) for(auto u:a)
#define pb push_back
#define eb emplace_back

/* DEBUGGING && PRINTING */
#define printv(a) {for(auto u:a) cout<<u<<" "; cout<<endl;}
#define printm(a) {for(auto u:a) cout<<u.f sp u.s<<endl;}

/*  All Required define Pre-Processors and typedef Constants */

int n, m;
vector<vector<array<int, 3>>> grid;

bool good(ll k) {
    // cout << "init mones: " << k << endl;
    deque<array<ll, 2>> q; q.push_back({0, k});
    vector<int> vis(n);
    while(!q.empty()) {
        auto [cur, mon] = q.front(); q.pop_front();
        // cout << cur sp mon << endl;
        if(vis[cur]) continue;
        vis[cur] = 1;
        if(cur == n-1) return 1;
        for(auto [nbr, c, r] : grid[cur]) {
            if(c > mon) continue;
            if(r > c) return 1;
            if(vis[nbr]) continue;
            q.push_back({nbr, mon-c+r});
        }
    }
    return 0;
}

void solve() {
    cin >> n >> m;
    grid = vector<vector<array<int, 3>>>(n);
    frn(i, m) {
        int a, b, c, r; cin >> a >> b >> c >> r;
        a--; b--;
        grid[a].push_back({b, c, r});
        grid[b].push_back({a, c, r});
    }

    ll l = 0, r = 1e18, mid = 0;
    while(l < r) {
        mid = l+((r-l)>>1);
        if(good(mid)) r = mid;
        else l = mid+1;
    }
    cout << (good(l) ? l : r) << endl;
}

signed main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    int tc = 1;
    // cin >> tc;
    cfr(t, 1, tc) {
        // cout << "Case #" << t << ": ";
        solve();
    }
}


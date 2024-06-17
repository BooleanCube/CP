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
#define rall(a) (a).rbegin(), (a).rend()
#define fr(i,s,e) for(int i=(s);i<(e);i++)
#define frn(i,n) fr(i,0,(n))
#define cfr(i,s,e) for(int i=(s);i<=(e);i++)
#define rfr(i,e,s) for(int i=(e)-1;i>=(s);i--)
#define afr(a) for(auto &u:a)
#define pb push_back
#define eb emplace_back

/* DEBUGGING && PRINTING */
#define printv(a) {for(auto u:a) cout<<u<<" "; cout<<endl;}
#define printm(a) {for(auto u:a) cout<<u.f sp u.s<<endl;}


vector<vi> tree;
vi score;
vector<mii> memo;

ll dp(int u, int k) {
    if(k == 0) return 0;
    if(memo[u].count(k)) return memo[u][k];

    ll ans = k * score[u];
    if(!sz(tree[u])) return memo[u][k] = ans;

    int s = sz(tree[u]);
    int q = k / s, m = k % s;
    vll diff(s);
    frn(i, s) {
        ll v1 = dp(tree[u][i], q);
        ll v2 = m ? dp(tree[u][i], q+1) : v1;
        diff.pb(v2 - v1);
        ans += v1;
    }
    sort(rall(diff));
    frn(i, m) ans += diff[i];

    return memo[u][k] = ans;
}

void solve() {
    int n, k; cin >> n >> k;
    tree = vector<vi>(n);
    memo = vector<mii>(n);
    fr(i, 1, n) {
        int p; cin >> p; p--;
        tree[p].pb(i);
    }
    score = vi(n); afr(score) cin >> u;
    cout << dp(0, k) << endl;
}

signed main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    int tc = 1;
    cin >> tc;
    cfr(t, 1, tc) {
        // cout << "Case #" << t << ": ";
        solve();
    }
}


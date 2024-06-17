#include <bits/stdc++.h>
using namespace std;


/* TYPES  */
#define ll long long
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
ll min(int a,ll b) { if (a<b) return a; return b; }
ll max(ll a,int b) { if (a>b) return a; return b; }
ll max(int a,ll b) { if (a>b) return a; return b; }
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
#define cfr(i,s,e) for(long long int i=(s);i<=(e);i++)
#define rfr(i,e,s) for(int i=(e)-1;i>=(s);i--)
#define afr(a) for(auto &u:a)
#define pb push_back
#define eb emplace_back

/* DEBUGGING && PRINTING */
#define printv(a) {for(auto u:a) cout<<u<<" "; cout<<endl;}
#define printm(a) {for(auto u:a) cout<<u.f sp u.s<<endl;}

/*  All Required define Pre-Processors and typedef Constants */
typedef long int int32;
typedef unsigned long int uint32;
typedef long long int int64;
typedef unsigned long long int uint64;


#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;

struct multiost {
    typedef tree<
        pii,
        null_type,
        less<pii>,
        rb_tree_tag,
        tree_order_statistics_node_update
    > ost;

    ost s;

    multiost() = default;
    void insert(int x, int idx) { s.insert({x, idx}); }
    ost::iterator find_by_order(int k) { return s.find_by_order(k); }
    int order_of_key(int k) { return s.order_of_key({k, 0}); }
    void erase(int x) {
        auto it = s.lower_bound({x, 0});
        // erase(it); // erases only first element
        while(it != s.end() && it->first == x) erase(it++); // erases all elements
    }
    void erase(ost::iterator it) { s.erase(it); }
    auto lb(int x, int idx) { return s.lower_bound({x, idx}); }
    size_t size() const { return s.size(); }
};

void solve() {
    int n, m; cin >> n >> m;
    vi a(n); afr(a) { cin >> u; u ^= 1; }
    multiost ost; frn(i, n) ost.insert(a[i], i);
    frn(i, m) {
        int op, v; cin >> op >> v;
        if(op - 1) cout << ost.find_by_order(v)->s << endl;
        else {
            ost.erase(ost.lb(a[v], v));
            a[v] ^= 1;
            ost.insert(a[v], v);
        }
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    int tc = 1;
    // cin >> tc;
    cfr(t, 1, tc) {
        // cout << "Case #" << t << ": ";
        solve();
    }
}

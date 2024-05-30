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
#define cfr(i,s,e) for(int i=(s);i<=(e);i++)
#define rfr(i,e,s) for(long long int i=(e)-1;i>=(s);i--)
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


#define int ll

void solve() {
    int n, m; cin >> n >> m;
    vi pi(n+m+1), ti(n+m+1);
    afr(pi) cin >> u; afr(ti) cin >> u;
    int tbp = 0, pbt = 0;
    vi ans(n+m+1);
    vector<pair<int, pii>> pgm, tst;
    vector<pii> side(n+m+1);
    frn(i, n+m+1) {
        if(pi[i] > ti[i]) pgm.pb({i, {pi[i], ti[i]}}), side[i] = {0, sz(pgm)-1};
        else tst.pb({i, {ti[i], pi[i]}}), side[i] = {1, sz(tst)-1};
    }
    vi pspp(1), pspt(1), pstp(1), pstt(1);
    afr(pgm) {
        pspp.pb(pspp.back() + u.s.f);
        pspt.pb(pspt.back() + u.s.s);
    }
    afr(tst) {
        pstt.pb(pstt.back() + u.s.f);
        pstp.pb(pstp.back() + u.s.s);
    }
    frn(i, n+m+1) {
        int cur = 0;
        if(side[i].f) {
            auto it = tst.begin() + side[i].s;
            if(n > sz(pgm)) cur += pspp.back();
            else cur += pspp[n] + (pspt.back() - pspt[n]);
            if(m >= sz(tst)) cur += pstt.back() - it->s.f;
            else if(side[i].s < m) cur += (pstt[m+1] - it->s.f) + (pstp.back() - pstp[m+1]);
            else cur += pstt[m] + (pstp.back() - pstp[m]) - it->s.s;
        } else {
            auto it = pgm.begin() + side[i].s;
            if(m > sz(tst)) cur += pstt.back();
            else cur += pstt[m] + (pstp.back() - pstp[m]);
            if(n >= sz(pgm)) cur += pspp.back() - it->s.f;
            else if(side[i].s < n) cur += (pspp[n+1] - it->s.f) + (pspt.back() - pspt[n+1]);
            else cur += pspp[n] + (pspt.back() - pspt[n]) - it->s.s;
        }
        ans[i] = cur;
    }
    printv(ans);
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


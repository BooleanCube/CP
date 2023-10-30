#include <algorithm>
#include <bits/stdc++.h>
#include <cmath>
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
#define fr(i,s,e) for(long long int i=(s);i<(e);i++)
#define frn(i,n) fr(i,0,(n))
#define cfr(i,s,e) for(long long int i=(s);i<=(e);i++)
#define rfr(i,e,s) for(long long int i=(e)-1;i>=(s);i--)
#define afr(a) for(auto u:a)
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

vector<ll> powers;

ll g(ll x) {
    return (ll)log(x)/((ll)log((ll)log2(x)));
}

ll hpow(ll a, ll b) {
    ll res = 1;
    for(int i=0; i<b; i++) res *= a;
    return res;
}

void solve() {
    ll l, r; cin >> l >> r;
    ll ans = 0;
    ll sl = g(l), el = g(r);
    int lidx = lower_bound(all(powers), l)-powers.begin();
    int ridx = lower_bound(all(powers), r)-powers.begin();
    vector<ll> pts;
    ll cl = sl;
    for(int i=lidx; i<min(powers.size()-1, ridx); i++) {
        ll nextlog = powers[i+1];
        vector<ll> npows;
        ll num = 1;
        while(num < 1e18+1 && num > 0) {
            npows.emplace_back(num);
            num *= (cl+1);
        }
        ll intersection = *lower_bound(all(npows), powers[i]);
        if(intersection < powers[i+1]) pts.emplace_back(intersection);
        pts.emplace_back(powers[i]);
        ll cl = g(powers[i]);
    }
    if(pts.size()) {
        ans += sl*(pts[0]-l);
        ans %= MOD;
    }
    for(int i=0; i<pts.size(); i++) {
        ll cl = g(pts[i]);
        ans += cl*(pts[i+1]-pts[i]);
        ans %= MOD;
    }
    if(pts.size()) {
        ll cl = g(pts[pts.size()-1]);
        ans += cl*(r-pts[pts.size()-1]+1);
        // if WA check for if the last in the range is also an intersection point
        ans %= MOD;
    }
    if(pts.size() == 0) {
        ans = cl*(r-l+1);
        ans %= MOD;
    }
    cout << ans << endl;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    ll num = 1;
    while(num < 1e18+1 && num > 0) {
        powers.push_back(num);
        num *= 2;
    }

    int tc = 1;
    cin >> tc;
    cfr(t, 1, tc) {
        // cout << "Case #" << t << ": ";
        solve();
    }
}


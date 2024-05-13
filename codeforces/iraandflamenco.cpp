#include <bits/stdc++.h>
using namespace std;

const int MOD = int(1e9) + 7;
 
struct mint {
    int val;
 
    mint(int64_t v = 0) {
        v %= MOD;
        if (v < 0) v += MOD;
        val = v;
    }
 
    mint& operator+=(const mint& other) {
        val += other.val;
        if (val >= MOD) val -= MOD;
        return *this;
    }
 
    mint& operator-=(const mint& other) {
        val += MOD - other.val;
        if (val >= MOD) val -= MOD;
        return *this;
    }
 
    mint& operator*=(const mint& other) {
        val = (int64_t)val * other.val % MOD;
        return *this;
    }
 
    mint& operator/=(const mint& other) {
        return *this *= other.inv();
    }
 
    friend mint operator+(mint a, const mint& b) { return a += b; }
    friend mint operator-(mint a, const mint& b) { return a -= b; }
    friend mint operator*(mint a, const mint& b) { return a *= b; }
    friend mint operator/(mint a, const mint& b) { return a /= b; }
 
    mint pow(int64_t exp) const {
        mint a = *this, res = 1;
        while (exp > 0) {
            if (exp & 1)
                res *= a;
            a *= a;
            exp >>= 1;
        }
        return res;
    }
 
    mint inv() const {
        assert(val != 0);
        return pow(MOD - 2);
    }
 
    friend ostream& operator<<(ostream& os, const mint& m) {
        return os << m.val;
    }
};

void solve() {
    int n, m; cin >> n >> m;

    map<int, int> cnt;
    for (int i = 0; i < n; i++) {
        int a; cin >> a;
        cnt[a]++;
    }
    
    int k = cnt.size();
    vector<pair<int, int>> a(cnt.begin(), cnt.end());

    mint ans = 0, p = 1;
    for (int i = 0; i < min(k, m - 1); i++)
        p *= a[i].second;
    for (int i = m - 1; i < k; i++) {
        p *= a[i].second;
        if (a[i].first == a[i - m + 1].first + m - 1) ans += p;
        p /= a[i - m + 1].second;
    }
    cout << ans << '\n';
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t; cin >> t;
    while (t--) solve();
}
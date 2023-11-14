#include <bits/stdc++.h>
using namespace std;

#define ll long long

const ll MOD = 1e9+7;

int main() {
    ll x; cin >> x;
    ll ans = 0;
    for(int i=1; i*i<x; i++) {
        if(x%i == 0) {
            ans += i;
            ans += x/i;
        }
        ans %= MOD;
    }
    ll sq = (int)sqrt(x);
    if(sqrt(x) == sq && (x % sq) == 0) ans += (int)sqrt(x);
    ans %= MOD;
    cout << ans << endl;
    return 0;
}
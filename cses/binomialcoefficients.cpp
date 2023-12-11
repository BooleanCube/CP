#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
const int N = 1e6;
const ll MOD = 1e9+7;

int n, a, b;
ll fact[N+1], inv[N+1];

ll mod_inverse(ll x){
    ll res = 1;
    ll expo = MOD-2;
    while(expo > 0){
        if(expo&1)
            res = (res * x) % MOD;
        x = (x * x) % MOD;
        expo >>= 1;
    }
    return res;
}

int main() {
    fact[0] = inv[0] = 1;
    for(int i = 1; i <= N; i++){
        fact[i] = i * fact[i-1] % MOD;
        inv[i] = mod_inverse(fact[i]);
    }
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> a >> b;
        cout << fact[a] * inv[b] % MOD * inv[a-b] % MOD;
    }
}

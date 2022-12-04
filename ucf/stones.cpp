#include <bits/stdc++.h>
using namespace std;

long long fpow(long long a, long long b, long long m) {
    a %= m;
    long long res = 1;
    while (b > 0) {
        if (b & 1)
            res = res * a % m;
        a = a * a % m;
        b >>= 1;
    }
    return res;
}

int main() {
    int t; cin >> t;
    while(t--) {
        int y; cin >> y;
        vector<long long> alice(y);
        for(int i=0; i<y; i++) cin >> alice[i];
        int z; cin >> z;
        vector<long long> bob(z);
        for(int i=0; i<z; i++) cin >> bob[i];
        long long as = 0;
        for(long long i : alice) as += fpow(2,i,1000000007);
        long long bs = 0;
        for(long long i : bob) bs += fpow(2,i,1000000007);
        if(as==bs) cout << "Tie!\n";
        else if (as>bs) cout << "Alive will have more fun!\n";
        else cout << "Bob will have more fun!\n";
    }
}
